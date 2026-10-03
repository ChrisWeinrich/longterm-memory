---
title: "Deterministic Agent Coding Control Plane"
type: raw-research-report
tags: [research, coding-agents, github-actions, github-copilot, codex, cloud, governance, security]
origin: research-workflow
created: 2026-09-13
---

# Deterministic Agent Coding Control Plane

## Executive conclusion

Coding-agent work cannot be deterministic in the sense that a language model
will always choose identical plans or patches. The achievable and useful goal
is a **deterministic control plane around a bounded, probabilistic execution
step**. It admits only a typed low-risk task, grants a short-lived and narrow
capability set, records evidence, and permits only a pull request as output.
Normal CI, protected branches and a human remain the delivery authority.

For an engineering owner with GitHub Copilot cloud access and OpenAI/Codex API
access, the first implementation should be **GitHub Agentic Workflows**, first
with Copilot and then with Codex under the *same* task contract. GitHub supports
both engines in the same frontmatter format, compiles the Markdown definition
to a hardened lockfile, starts read-only by default, limits writes to declared
safe outputs, keeps secrets in downstream jobs, and records estimated usage.
This is the smallest control system that makes an engine comparison meaningful.
[^1]

Do not begin with an autonomous dispatcher, multi-agent supervisor or a custom
agent platform. Begin with manual dispatch of four narrow tasks and a draft-PR
only output. Add automatic label-triggered admission only after the evidence
shows low policy-violation and review-rework rates. A custom GitHub Actions
wrapper with the Codex SDK/API is the next choice only when the GitHub-native
workflow demonstrably cannot express a required policy, provider route, or
private execution environment. Durable systems such as Temporal or Azure
Durable Functions are later-stage lifecycle infrastructure, not a substitute
for worker containment.

## What “deterministic” means here

The agentic kernel is intentionally nondeterministic. The surrounding system
must be deterministic about the following questions:

| Question | Deterministic owner | Required rule |
| --- | --- | --- |
| May this task start? | Admission workflow | Typed schema, owner, risk class, path/command allowlist, one active run |
| What may it access? | GitHub permissions + disposable worker | Read-only by default; branch/PR-only write; no production secrets |
| What counts as output? | Safe-output / PR contract | Draft PR plus machine-readable evidence; never merge or deploy |
| Is the patch acceptable? | CI, policy checks, CODEOWNERS | Required checks and review, tied to expected GitHub Apps |
| May it reach production? | Separate deployment workflow | Post-merge artifact, protected environment and narrowly scoped OIDC role |
| How is it stopped? | Operator runbook | Disable entry, cancel/force-cancel, revoke worker identity, preserve logs |

This distinction is security-critical. AgentDojo, a NeurIPS benchmark for
tool-using agents over untrusted data, notes that a model has no formal way to
separate instructions from data. Its 97 realistic tasks and 629 security cases
show both task failures without attacks and security failures under indirect
prompt injection. [^10] Therefore prompts and model self-review are useful
quality measures, but cannot be authorization boundaries.

## Options compared

| Option | What is controlled out of the box | What is still yours | Recommendation |
| --- | --- | --- | --- |
| Copilot cloud agent alone | Issue/PR lifecycle and a GitHub-hosted executor | Admission, automatic-start policy, cost/diff limits, evidence schema | Useful manual baseline, but not enough control-plane surface on its own |
| Agentic Workflows + Copilot | Trigger, declared permissions, safe outputs, isolated execution, lockfile, usage/audit | Task schema, path policy, CI, branch/deploy gates | **First pilot** |
| Agentic Workflows + Codex | Same control shell; engine changes to Codex | Same controls, plus third-party credential and invoice handling | **Second pilot, identical task corpus** |
| GitHub Actions + Codex SDK/API | Actions primitives and every policy explicitly encoded | Full lifecycle, sandbox, cancellation, telemetry, prompt-injection handling | Add only for a concrete GitHub-native gap |
| Temporal/Azure Durable + isolated executor | Persistent workflow state, retries, pause/resume, status APIs | Worker kill/revocation, isolation, PR gating, all agent policy | Add for long waits, queues, VPC systems or cross-repo scheduling |
| LangGraph/LangSmith + executor | Stateful graph, checkpoints, human interrupts, tracing | GitHub delivery controls and a separate operating/data surface | Use when building an agent product, not an internal coding queue |
| Generic coding CLIs/harnesses | Model-specific editing/tool loop | Everything listed above | Executors only; not control planes |

### GitHub Agentic Workflows: preferred first shell

GitHub Agentic Workflows executes Markdown instructions and compiles them into
a `.lock.yml` Actions workflow. Its frontmatter governs trigger, permissions,
network, tool access, safe outputs and engine. It supports Copilot, Codex,
Claude and Gemini; Copilot is the default when no engine is named. [^1]

This is materially different from calling a CLI in a broad, normal Actions job.
The documented workflow model is read-only by default, validates declared write
outputs, uses an isolated firewalled environment, and places sensitive
credentials in downstream jobs rather than the agent runtime. A per-run
`max-ai-credits` cap plus `gh aw logs`/`gh aw audit` provides a usable initial
cost and activity record. AIC is an estimate and must be reconciled with the
provider invoice for any third-party engine. [^1]

For organization-owned repositories with a Copilot plan, GitHub documents a
`GITHUB_TOKEN` billing path using `copilot-requests: write`; it avoids storing
a Copilot PAT. Personal repositories and third-party engines require a managed
secret/API key, so the secret lifecycle is part of the pilot acceptance test.
[^2]

**Judgment:** this option directly fits the stated environment. It permits an
apples-to-apples Copilot-versus-Codex trial without first inventing an
orchestrator. Its limits are intentional: feature/plan availability, workflow
syntax and provider credentials must be verified in the target organization
before treating them as production controls.

### Custom GitHub Actions plus Codex SDK/API: the escape hatch

The Codex TypeScript SDK wraps the Codex CLI, supports thread continuation,
structured event streaming, JSON-schema output, an explicit working directory
and a controlled child-process environment. [^3] The Responses API supports
typed custom tools, a selectable tool set and JSON-schema Structured Outputs;
the application executes the custom tool rather than delegating its authority
to the model. [^4][^5]

This makes a custom wrapper powerful: an admission action can validate a JSON
task object, create a short-lived worker, request an explicit `plan` schema,
allow only a named test/edit tool set, and accept only a `draft-pr` result
schema. It can route `risk:docs` to a small model and `risk:standard` to Codex,
or run a deterministic diff checker before allowing a PR creation call.

It also makes the team responsible for every sharp edge: queue leases,
idempotency keys, model/API failures, orphan workers, cancellation propagation,
usage ledger, secret injection, sandbox configuration and prompt-injection
defense. This is not a small extension of GitHub Actions; it is an internal
product. Build it after a measured need, not as a prerequisite for the first
four tasks.

### Durable orchestrators: lifecycle, not judgment

Temporal and cloud-native durable workflow services are good at an explicit
state machine with timers, retries, durable state and human wait points. Azure
Durable Functions, for example, manages state, checkpoints, retries and
recovery for long-running workflows. [^6]

However, coordinator cancellation is not equivalent to worker containment.
Azure explicitly documents that terminating an orchestration does not propagate
to activity functions or sub-orchestrations; activities may run to completion.
[^7] The architecture must therefore combine three mechanisms: (1) cancel the
coordinator, (2) cancel/kill the worker and expire its lease, and (3) revoke
the worker's credentials or egress path. This applies equally to container
workers launched by Temporal, Step Functions or a CI system.

Adopt a durable orchestrator only when there is a concrete non-GitHub need:
cross-repository fairness queues, work exceeding Actions limits, private VPC
test systems, resumable approval waits, or provider-independent worker pools.
Until then it adds operations without making a PR safer.

### LangGraph/LangSmith: an agent-service framework

LangGraph explicitly supports mixing deterministic nodes with LLM-driven nodes,
persistence and human-in-the-loop interruption. [^8] That is well suited to a
customer-facing or internal agent product where a custom state machine and
operator UI are requirements. It is not an advantage merely because it is more
agent-oriented: it introduces state storage, deployment, monitoring and a new
control-plane boundary. Keep it out of the first coding-agent experiment.

## Recommended target architecture

```text
maintainer workflow_dispatch
        |
        v
deterministic admission check
  - typed task contract
  - risk/path/command policy
  - one active task / repository
        |
        v
Agentic Workflow: engine = copilot | codex
  - isolated environment
  - read scope + named tools
  - safe output: draft PR only
  - time / AIC ceiling
        |
        v
PR evidence + deterministic CI/policy suite
        |
        +--> optional read-only model review (advisory)
        |
        v
CODEOWNER/human review -> protected merge queue
        |
        v
separate post-merge deploy -> protected environment -> OIDC role
```

The agent must not hold deploy authority. GitHub branch protection can require
status checks, CODEOWNER reviews and merge queue behavior. Required checks can
be restricted to a specific GitHub App, preventing an arbitrary writer from
satisfying a same-named check. [^9] Build and deploy from the protected merged
commit or verified artifact—not the agent branch.

For a deployment workflow, GitHub OIDC supports cloud trust conditions for
specific repository, branch, pull-request event or environment claims. GitHub
requires at least one condition to prevent untrusted repositories from
obtaining a cloud token. [^12] Use a separate `production` environment and an
OIDC role which the agent workflow cannot assume.

## Minimum viable policy

### Task contract

Require all fields before a run starts:

| Field | Initial rule |
| --- | --- |
| Goal and acceptance checks | Explicit and testable; reject prose-only "improve" tasks |
| Owner and risk class | `docs`, `low-code`, `standard`, `sensitive`; only first two initially |
| Allowed / forbidden paths | Forbid `.github/`, deployment, IaC, auth, secrets, lockfiles and manifests initially |
| Commands | Explicit test/lint/build allowlist; no arbitrary shell or new network dependency |
| Diff ceiling | Max changed files and changed lines; overage blocks and asks a human |
| Output | Draft PR, command evidence, limitations and next action |
| Budget | Maximum duration, AIC/API token budget, retries and tool calls |

### Executor profile

Use a dedicated `agent-low-risk` profile. GitHub custom-agent configuration can
provide an explicit tool allowlist; omission enables all available tools.
`disable-model-invocation: true` makes selection manual, and custom-agent
profiles are versioned by the Git commit SHA used for the session. [^13] Treat
the profile as code: review it, pin it in the task evidence, and do not grant
MCP tools by default.

### Deterministic policy checks after the run

- Reject forbidden paths and unapproved generated/lockfile changes.
- Require the declared test/lint/build commands and capture exit status.
- Require an updated test for behavior changes, unless the contract records an
  explicit exception.
- Fail a patch whose diff/file budget exceeds the contract.
- Require a human/CODEOWNER review; the agent cannot approve or merge.
- Trigger deployment only from the protected branch after merge.

## Security and containment

### Inputs are adversarial data

GitHub warns that issue titles/bodies, PR content, branch names and other
`github` context values are attacker-controlled and must not be inserted into
shell scripts or interpreted as executable input. [^14] An agent additionally
reads repository code, documentation, test output and possibly tool results;
all can carry indirect instructions. The admission controller must never use
issue text as shell syntax, and the agent must receive untrusted content as
data, not privileged policy.

Never use `pull_request_target` to check out and execute fork code in a
privileged agent job. GitHub documents that this event has the base
repository's token and secrets; executing fork code after such a checkout is a
known "pwn request" shape. [^15] A pilot should have no fork/comment trigger
at all.

### Prompt injection is a design constraint

AgentDojo shows that tool-using systems can act on attacker-supplied text and
that utility and security must both be evaluated. [^10] The later ICML MELON
paper proposes a defense based on comparing trajectories with a masked user
prompt, but this is a detection/mitigation technique, not proof that an agent
is safe to authorize broadly. [^11]

The practical response is capability design:

- Keep the worker repository-scoped, branch-scoped and PR-only.
- Exclude production secrets, organization administration and deployment from
  its token and environment.
- Use a disposable hosted runner/container; do not reuse a privileged local or
  self-hosted runner for untrusted coding tasks.
- Default network access to the minimum; do not give arbitrary external MCP
  tools to an implementation agent.
- Make a second model reviewer read-only and advisory. It may find defects but
  cannot constitute a security gate.

### Kill switch

The runbook needs four separate actions because one is insufficient:

1. Cancel the current GitHub run; use force-cancel only if normal cancellation
   does not stop it. GitHub exposes both endpoints. [^16]
2. Disable the workflow and remove the admission label/policy to prevent the
   next run or retry.
3. Revoke/rotate the engine API key or worker cloud role, and block the worker
   network route if one exists.
4. Close the PR, preserve run ID/logs/task contract and create an incident
   record before changing policy.

Test this runbook on a harmless task before admitting useful code changes.

## Pilot design and decision gates

### Phase 0 — install controls

Protect the default branch; require CI and CODEOWNER/human review; disable
bypass for agents; establish a merge queue if the repository needs it. Create
a short issue/task template, low-risk labels and an operator cancel runbook.
Create a no-secret draft-PR workflow with manual dispatch.

### Phase 1 — compare two engines

Run the same four tasks serially with `engine: copilot` and `engine: codex`:

1. Documentation correction limited to one directory.
2. Isolated test addition with no production-code edit.
3. Lint/type remediation in an allowed path.
4. Small local refactor with explicit acceptance tests.

Record task-contract SHA, profile SHA, engine/model, run ID, elapsed time,
AIC/API usage, changed files/lines, CI result, review changes, policy blocks,
and time-to-cancel. Evaluate 8–12 completed runs before automating admission;
four per engine is enough to expose setup gaps but not to rank models.

### Phase 2 — conditional admission

Permit `agent:ready` only when a deterministic checker validates the contract.
Keep concurrency at one active implementation run per repository. Add an
optional read-only reviewer with a structured finding (`approve`,
`needs-human-review`, `reject`) and evidence paths. It never changes labels,
approvals, code or dispatch state.

### Phase 3 — decide whether to build

Build the Actions + Codex wrapper only if one or more facts are observed:

| Observed need | Next system |
| --- | --- |
| Engine routing, custom task schema or additional deterministic checks cannot be expressed | Small Actions policy wrapper + Codex SDK/API |
| Queue fairness, days-long pauses, cross-repo state or private VPC tests | Durable orchestrator with isolated workers |
| Product requires a custom human-in-the-loop agent service | LangGraph/LangSmith evaluation |
| No such measured gap | Keep Agentic Workflows; avoid building a platform |

## Open questions and limits

1. Exact Agentic Workflow availability, billing policy and permitted engines
   depend on the target GitHub organization/repository configuration; verify
   them in a disposable private repository before relying on them.
2. The correct initial path/command policy is repository-specific. A brittle
   test suite is evidence to narrow scope, not a reason to grant broad access.
3. Per-run inference caps control billed work, not side effects of an already
   over-privileged subprocess. They complement—not replace—credentials,
   containment and cancellation.
4. The academic results establish the class of prompt-injection risk; they do
   not quantify the risk for a particular repository. Include adversarial task
   text in the pilot evaluation before broadening triggers or tools.

## Sources

[^1]: GitHub. "[About GitHub Agentic Workflows](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/about-github-agentic-workflows)." Undated, accessed September 13, 2026.
[^2]: GitHub. "[Creating GitHub Agentic Workflows](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows)." Undated, accessed September 13, 2026.
[^3]: OpenAI. "[Codex TypeScript SDK](https://github.com/openai/codex/blob/main/sdk/typescript/README.md)." Undated, accessed September 13, 2026.
[^4]: OpenAI. "[Responses API reference](https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses)." Undated, accessed September 13, 2026.
[^5]: OpenAI. "[Model guidance: GPT-5.2](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2)." Undated, accessed September 13, 2026.
[^6]: Microsoft. "[Durable Functions overview](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview)." Undated, accessed September 13, 2026.
[^7]: Microsoft. "[Manage orchestration instances](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-instance-management)." Undated, accessed September 13, 2026.
[^8]: LangChain. "[LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)." Undated, accessed September 13, 2026.
[^9]: GitHub. "[About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)." Undated, accessed September 13, 2026.
[^10]: Edoardo Debenedetti et al. "[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)." NeurIPS Datasets and Benchmarks Track, 2024.
[^11]: Kaijie Zhu et al. "[MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents](https://proceedings.mlr.press/v267/zhu25z.html)." ICML, 2025.
[^12]: GitHub. "[OpenID Connect reference](https://docs.github.com/en/actions/reference/security/oidc)." Undated, accessed September 13, 2026.
[^13]: GitHub. "[Custom agents configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)." Undated, accessed September 13, 2026.
[^14]: GitHub. "[Script injections](https://docs.github.com/en/actions/concepts/security/script-injections)." Undated, accessed September 13, 2026.
[^15]: GitHub. "[Securely using pull_request_target](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)." Undated, accessed September 13, 2026.
[^16]: GitHub. "[REST API endpoints for workflow runs](https://docs.github.com/en/rest/actions/workflow-runs)." Undated, accessed September 13, 2026.
