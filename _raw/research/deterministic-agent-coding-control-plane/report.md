---
title: "Deterministic Agent Coding Control Plane"
type: raw-research-report
tags: [research, coding-agents, github-actions, github-copilot, codex, cloud, governance]
origin: research-workflow
created: 2026-09-12
---

# Deterministic Agent Coding Control Plane

## Conclusion

Coding-agent work itself cannot be deterministic: the model can choose a
different plan or produce different code for equivalent input. The viable goal
is a **deterministic control plane around a bounded agent step**. It should
deterministically decide which tasks may start, what resources the agent may
use, what evidence is required, and whether a change may merge or deploy.

For a GitHub-centred environment with Codex, Copilot, GitHub Actions, and
multiple inference APIs, start with **GitHub Issues → one cloud agent → draft
PR → deterministic CI/policy checks → human merge**. GitHub Copilot cloud
agent or a permitted third-party agent such as Codex is the simplest execution
lane: it works asynchronously on an issue or prompt and returns a pull request
for review. GitHub Agentic Workflows are a promising second lane for
repository-maintenance tasks, but remain public preview; keep their first use
read-only or limited to safe outputs such as issues and comments.^1 ^2

Do not start by building a multi-agent supervisor. A model "overseer" can
notice suspicious scope or weak tests, but it is probabilistic and can share
the same blind spots as the implementer. Make the authority-bearing overseer
ordinary controls: rules-as-code, permissions, ephemeral runners, protected
branches, required checks, independent human approval, time/cost ceilings, and
an immediate revocation/cancellation path. Add a read-only reviewer agent only
as an advisory check.

## The operating model

### Deterministic shell, agentic kernel

Use this fixed state machine. Each transition is an auditable GitHub event;
only the **Implement** state is model-driven.

```text
Issue / task contract
        │ deterministic admission policy
        ▼
Ready ──► bounded cloud implementer ──► draft PR
                                        │
                              deterministic CI + policy checks
                                        │
                         advisory read-only reviewer (optional)
                                        │
                    human / CODEOWNER review + protected merge queue
                                        │
                         separate deploy workflow + environment gate
                                        ▼
                                   production change
```

The agent receives a scoped task contract, not a vague instruction such as
"make the app better." A small Markdown issue template is enough initially.
Require these fields:

| Field | Admission rule |
| --- | --- |
| Goal and acceptance tests | Explicit, testable outcome |
| Allowed paths / forbidden paths | Reject broad or security-sensitive scope |
| Allowed commands and services | Default: test/lint/build only |
| Dependencies and network | No new dependency or egress without a named approval |
| Max changed files / diff size | Fail or require escalation above the threshold |
| Expected PR output | Draft PR, evidence, known limitations; never merge/deploy |
| Risk class | `docs`, `low-code`, `standard`, `sensitive` |

Keep the admission policy deliberately boring. A task is eligible only when it
has an `agent:ready` label, a bounded risk class, an assignee/owner, and a
machine-readable completion definition. Start with documentation, tests, lint
fixes, and local refactors. Explicitly exclude authentication, permissions,
secrets, infrastructure, production configuration, destructive migrations, and
dependency upgrades until individual policies and reviewers exist.

## Cloud execution choices

| Option | What starts the work | Control strengths | Limits / best use |
| --- | --- | --- | --- |
| Copilot cloud agent | Assign an issue or `/task`; agent opens a PR | Native issue/PR trail; custom agent profiles; GitHub review gates | Lowest setup effort; use for bounded implementation, not autonomous delivery |
| GitHub Agentic Workflows | Event/schedule/manual workflow compiled to locked Actions workflow | Declared permissions, safe outputs, isolated agent environment, per-run AI-credit cap | Public preview; best first for triage, CI investigation, reports, docs, PR review assistance |
| GitHub Actions plus direct model API | Workflow dispatch invokes a chosen provider/API or container agent | Complete provider and tool choice; deterministic wrapper is yours | You own prompt-injection defence, secret isolation, retries, audit schema, and cancellation semantics |
| Cloud workflow orchestrator plus disposable workers | GitHub webhook starts Step Functions, Google Workflows, Durable Functions, or equivalent; it creates a short-lived container job | Strong state machine, queues, IAM boundaries, retries, explicit pause/cancel APIs | Appropriate only after GitHub-native flow has real limits: cross-repo queues, long running jobs, private network resources, or high throughput |
| Self-hosted/persistent agent runtime | Local or private runner receives a task | Useful for private hardware or local tools | Highest blast radius; do not give it production credentials or a main-branch write path |

GitHub supports starting Copilot cloud work from a task prompt or existing
issue, then creates a branch and PR and requests review when it finishes. It
also supports repository/organization custom agent profiles, including a
selected model, prompts and tools.^3 ^4 This makes Copilot a suitable first
implementation engine. GitHub's third-party coding-agent integration also
allows Codex alongside Copilot, but is public preview; treat the exact provider
availability and policy controls as a pilot validation item.^2

GitHub Agentic Workflows are the closest match to a "deterministic launch
flow" in the cloud. Their Markdown frontmatter declares triggers, permissions,
network/tool settings, and the safe write outputs; GitHub compiles it to a
locked Actions workflow. The platform states that agents are read-only by
default, writes must be declared as safe outputs, and secrets stay in isolated
downstream jobs.^1 That makes it materially safer than installing a CLI and
letting it operate in a broadly privileged generic workflow. GitHub itself
recommends Agentic Workflows rather than calling Copilot CLI directly in most
automations; direct CLI invocation has broad access to the workflow environment
and is especially risky for fork-originated pull requests.^5

For a custom provider layer, use a durable cloud workflow only when a real
control-plane need appears. Google Workflows, for example, supports execution
creation, inspection and cancellation with a distinct `workflows.executions.cancel`
permission and audit logs.^6 AWS Step Functions and Azure Durable Functions
also expose stop/terminate management APIs. Azure documents an important
caveat: terminating the orchestration does not necessarily stop already-running
activity functions, so each worker needs its own deadline and cooperative stop
mechanism.^7 This is a general design lesson: cancelling the coordinator is not
the same as revoking a worker's credentials or network access.

## The overseer: controls that actually stop a runaway agent

### 1. Admission controller — before work begins

Implement this as a deterministic GitHub Action or GitHub App, not an LLM.
It reads only the task contract and repository policy and either creates the
work request or refuses it with reasons. Useful rules include:

- Allowlisted repositories, branches and event types. Do not start an agent
  from arbitrary issue comments, PR bodies, commit messages, or fork events.
- A task schema and risk label are mandatory. `sensitive` tasks require a
  human-created branch and no cloud agent.
- A static path allowlist rejects changes under `.github/`, deployment/IaC,
  identity, secrets, lockfiles, and package manifests unless a named policy
  allows them.
- One active implementation task per repository or service. GitHub Actions
  concurrency groups can keep one run and cancel an in-progress predecessor.
  This prevents a feedback loop from creating an agent swarm.^8
- A single run budget: maximum wall time, token/credit ceiling, diff/file
  ceiling, API/tool-call ceiling and retry ceiling. Agentic Workflows supports
  `max-ai-credits`; GitHub reports duration, token usage, and estimated AIC
  through `gh aw logs` and `gh aw audit`.^1

### 2. Capability boundary — while it works

The implementer must have enough permission to push only its own branch and
open/update its own PR. It must not merge, administer repository settings,
read production secrets, alter workflow policies, or reach production.

- Use a disposable GitHub-hosted runner or disposable container/VM. Avoid a
  shared self-hosted runner for untrusted agent work; GitHub warns that
  self-hosted runners are not isolated containers, even when environments are
  used.^9
- Declare `permissions:` explicitly at workflow and job scope. Pin third-party
  Actions to full commit SHAs and restrict which Actions may run. GitHub cites
  both as workflow hardening measures.^10
- Treat every GitHub context value and repository text consumed by the agent as
  untrusted. Issue bodies, PR text, branch names, README content and tool
  output can carry prompt-injection or shell-injection payloads. Never inject
  them into shell scripts; do not use `pull_request_target` to run agent code
  from a fork; make the agent treat repository instructions as data unless they
  are in an allowlisted policy file.^11
- Keep production credentials outside the agent job. A separate deployment job
  receives short-lived cloud credentials through GitHub OIDC after protected
  checks and environment approval. Scope the cloud trust policy to repository,
  branch, environment, and ideally reusable-workflow identity; GitHub documents
  that OIDC can exchange a job token for a short-lived cloud token without a
  long-lived GitHub secret.^12
- Default external network access to the minimum necessary. Codex cloud
  environments have internet access off by default and can restrict allowed
  domains and methods where that control is available; validate the workspace
  plan-specific setting before relying on it.^13

### 3. Independent verification — after a PR, before merge

No agent's prose about its own result is evidence. Require normal CI to run
tests, lint, type checks, build, dependency/license scan and any repository
specific contract tests. Add deterministic policy checks for changed paths,
diff size, forbidden files, lockfile changes, generated code, and required
test additions.

An optional **reviewer agent** runs read-only against the PR and returns a
structured finding: `approve`, `needs-human-review`, or `reject`, with affected
paths and concrete evidence. It has no write token and cannot merge, label,
or re-dispatch the implementer. Run a different model/provider from the
implementer when that reduces correlated failure, but do not make it a required
authority until measured on real PRs. The authority remains protected branches,
CODEOWNERS, required checks and a human approval.

Protected branches can require successful status checks, code-owner review,
review count, and merge queue behaviour. GitHub notes that a required check can
be tied to a particular GitHub App, avoiding acceptance of a same-named status
from any writer.^14 For releases, build after merge from the protected commit;
do not deploy the agent's PR branch. Generate and verify artifact attestations
when releasing binaries or images to establish build provenance.^15

### 4. Emergency brake — immediate and durable

An operator needs three distinct controls:

| Need | Control | Expected effect |
| --- | --- | --- |
| Stop this execution | Cancel the GitHub Actions run; force-cancel if ordinary cancellation is stuck | Stops queued/running GitHub jobs; record run ID and reason |
| Stop new executions | Disable the workflow; remove the `agent:ready` admission label/policy; disable the GitHub App/agent policy | Prevents re-entry and webhook loop retries |
| Remove capability | Revoke the cloud role/session, disable environment access, rotate/revoke provider key if one was exposed | Stops access even if an external subprocess survives cancellation |
| Block delivery | Branch protection, merge queue and protected environments have no bypass for the agent | A bad PR cannot reach main or production |

GitHub exposes both normal and force cancellation endpoints for workflow runs,
and workflow disabling through the UI, API or CLI.^16 Run cancellation must be
paired with credential revocation for external workers. A stop button that only
cancels a coordinator is insufficient.

For deployments, use a distinct `production` environment: allowed release
branches only, no administrator bypass, a non-initiator reviewer, and secrets
available only after the gate. GitHub environments can require reviewers,
restrict deploy branches and use custom protection rules; plan availability
depends on repository visibility and GitHub plan, so verify it for the intended
private repositories before designing around reviewer gates.^9 A deployment
workflow may also have a pre-deploy health/approval service, but that service
should be deterministic and fail closed, not an LLM judge.

## Recommended starter architecture

### Phase 0 — controls before autonomy

1. Protect `main`: PR only, required CI, required review/CODEOWNERS, dismiss
   stale approvals, no agent bypass, and merge queue if supported.
2. Create `agent:ready`, `agent:blocked`, `risk:low`, and `risk:sensitive`
   labels plus a short issue template/task contract.
3. Add an `agent-admission` check. At first it only validates labels, owner,
   task fields, path/risk policy and a one-active-task concurrency key.
4. Put a `production` environment behind a separate workflow. The agent PR
   never invokes it and never reads its secrets.
5. Write a one-page runbook: cancel run; disable workflow; revoke cloud role;
   close the PR; preserve logs; file an incident issue. Test this on a harmless
   task.

### Phase 1 — one implementer, PR-only

Use Copilot cloud agent first for a manually selected, `risk:low` issue. Its
custom profile should state: work only in the permitted paths; never change
workflow/IaC/credential files; never merge or deploy; use stated commands;
open a **draft** PR with test evidence; stop and request clarification if the
scope changes. Codex can be trialled as the alternative engine for identical
task contracts, one at a time, so output quality, cost, and review burden can
be compared fairly.

The human selects the task and starts it. Do not yet auto-start from a label,
schedule or comment. Measure: completed PRs, review rework, failed checks,
time-to-cancel, diff-size distribution, cost, and any policy violation.

### Phase 2 — policy-driven launch and advisory reviewer

Allow `agent:ready` to trigger one implementation session only after the
admission check passes. Add a read-only reviewer workflow that posts findings
but cannot approve/merge. GitHub Agentic Workflows are a good experimental
implementation for recurring, low-risk oversight: daily PR/CI digest, issue
triage, or CI-failure explanation with only `create-issue`/`add-comment` safe
outputs. Keep a plain deterministic Action as the enforcement layer.

### Phase 3 — cloud worker control plane only when necessary

Move to a cloud workflow service when GitHub cannot express a need, for example
per-tenant queues, work that exceeds runner limits, private VPC-only test
systems, long-lived approvals, or a provider-independent task broker. The
orchestrator owns state, a queue, explicit deadlines, audit records and a
per-task worker identity. Each worker gets a fresh container, source checkout,
short-lived token, egress policy and a lease that expires. The only allowed
output remains a branch/PR or immutable artifact, never direct production
mutation.

## Design decisions and trade-offs

| Decision | Recommendation | Reason |
| --- | --- | --- |
| "Overseer" type | Deterministic policy engine first; agent reviewer second | An LLM cannot reliably enforce security or cost boundaries |
| First cloud executor | Copilot cloud agent, then a small Codex comparison | Native GitHub issue→PR lifecycle; no custom agent platform yet |
| Automation trigger | Manual at first; label-triggered after evidence | Prevents prompt/comment and retry loops before controls are proven |
| Model strategy | One implementer; different read-only reviewer only after baseline | Avoids a costly agent swarm and gives useful comparative data |
| Deployment | Separate, protected post-merge workflow | Removes production authority from the agent's task |
| Credentials | GitHub OIDC and short-lived, scoped cloud roles | Limits persistence and makes emergency revocation meaningful |
| Custom API platform | Defer | Flexibility is valuable only after it solves a demonstrated GitHub-native gap |

## Non-negotiable red lines

- No agent may merge to a protected branch or deploy to production.
- No agent run starts on untrusted external text without an explicit admission
  step; never run a privileged agent on fork code.
- No production secret or broad cloud credential enters an agent runtime.
- No self-hosted shared runner executes untrusted agent tasks with durable
  credentials.
- No "AI approval" substitutes for required checks and human approval.
- No automatic retry loop after policy failure; only a named human can
  re-admit a blocked task.

## Open questions

1. Which GitHub plan and repository visibility apply to the intended private
   repositories? Environment reviewer and custom-protection availability varies
   by plan and visibility.
2. Which repositories are safe initial pilots, and what command/path policy do
   their test suites support?
3. Is a cloud provider already the preferred home for private integration tests
   or deployment targets? That determines whether an eventual orchestrator
   should be GitHub-only, AWS, GCP, or Azure.
4. What monthly budget and maximum run duration should trigger automatic block
   and human escalation?

## Evidence

The factual product and platform claims in this report are supported by the
official sources below. Architecture recommendations are analytical judgments
derived from those capabilities and the stated goal of minimizing an agent's
blast radius.

## Trade-offs and risks

- GitHub Agentic Workflows and third-party coding-agent integrations are public
  preview, so syntax, availability and billing can change. Pilot them behind
  review; do not make them a production critical control.
- GitHub cancellation is a vital operational brake, not a complete containment
  boundary for a subprocess that has already obtained external access. Use
  short-lived credentials, egress limits, resource quotas and revocation.
- A PR-only model adds review latency. That is intentional at first; expand
  automation only when measured false-positive and rework rates are acceptable.
- Cloud-hosted agents require source access. Confirm provider data handling,
  network, retention and workspace controls for each repository before enabling
  it.

## Sources

1. GitHub. "[About GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows)." Accessed September 12, 2026.
2. GitHub. "[About third-party coding agents](https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents)." Accessed September 12, 2026.
3. GitHub. "[Using Copilot cloud agent on GitHub](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github)." Accessed September 12, 2026.
4. GitHub. "[About custom agents](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents)." Accessed September 12, 2026.
5. GitHub. "[Using Copilot CLI in GitHub Actions with GITHUB_TOKEN](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions)." Accessed September 12, 2026.
6. Google Cloud. "[Workflow Executions API](https://docs.cloud.google.com/workflows/docs/reference/executions/rest)." Accessed September 12, 2026.
7. Microsoft. "[Manage Orchestration Instances in Durable Functions and Durable Task SDKs](https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-instance-management)." Accessed September 12, 2026.
8. GitHub. "[Control the concurrency of workflows and jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)." Accessed September 12, 2026.
9. GitHub. "[Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)." Accessed September 12, 2026.
10. GitHub. "[Protecting against security threats](https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)." Accessed September 12, 2026.
11. GitHub. "[Script injections](https://docs.github.com/en/actions/concepts/security/script-injections)." Accessed September 12, 2026.
12. GitHub. "[Configuring OpenID Connect in cloud providers](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers)." Accessed September 12, 2026.
13. OpenAI. "[Codex Changelog](https://help.openai.com/en/articles/11428266-codex-changelog/)." June 3, 2025 entry, accessed September 12, 2026.
14. GitHub. "[About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)." Accessed September 12, 2026.
15. GitHub. "[Artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations)." Accessed September 12, 2026.
16. GitHub. "[REST API endpoints for workflow runs](https://docs.github.com/en/rest/actions/workflow-runs)." Accessed September 12, 2026.
