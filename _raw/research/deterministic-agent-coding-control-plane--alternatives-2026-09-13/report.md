---
title: "Deterministic Agent Coding Control Plane — execution alternatives"
type: raw-research-report
tags: [research, coding-agents, github-actions, github-copilot, codex, cloud, orchestration]
origin: research-workflow
created: 2026-09-13
---

# Deterministic Agent Coding Control Plane — execution alternatives

## Conclusion

For the available estate, **GitHub Agentic Workflows is the best first control
plane to trial**. It is not merely "Copilot in the cloud": the same GitHub
workflow contract can select `copilot` or `codex` as its engine. Its frontmatter
declares trigger, permissions, network, tool access, safe write outputs, and a
per-run AI-credit ceiling; GitHub compiles that declaration to a locked Actions
workflow. This gives one auditable, Git-native shell for a fair Copilot-versus-
Codex comparison. [1][2]

Start with a manual workflow dispatch that can only create a draft PR (or, even
safer, an issue/comment). Run the same task contract against both engines,
serially. The deterministic authority remains GitHub branch protection, CI,
CODEOWNERS, merge queue, environment gates, and explicit cancellation—not the
model profile or prompt.

There are three real alternatives, ordered by when they become justified:

1. **GitHub Actions + Codex SDK/API.** Best when GitHub Agentic Workflows cannot
   express an admission rule, provider routing, or result format. The wrapper
   owns the state machine and starts an isolated worker. The Codex SDK exposes
   structured streaming events, JSON-schema output, an explicit working
   directory, and a restricted child-process environment; the API offers
   allowed-tools and structured-output controls. This is flexible, but every
   security boundary, retry, cancellation and audit record is now your code.
   [3][4]
2. **Temporal or a cloud-native durable workflow service.** Best only after
   cross-repository queues, multi-hour approval waits, private-network tests,
   or a provider-independent worker pool are concrete requirements. These make
   lifecycle deterministic and observable, but do not make a coding agent
   deterministic. Worker isolation, expiring credentials, egress policy, and
   an output-only-to-PR contract remain mandatory.
3. **LangGraph/LangSmith.** Best if the product being built is itself an agent
   service with stateful human approvals, not just an internal coding queue.
   It can mix hand-coded graph nodes with model nodes, persist state and pause
   for human input. It introduces a separate framework, storage and operational
   surface; do not add it merely to launch coding-agent tasks from GitHub. [5]

**Not a control-plane alternative:** a coding harness/CLI (Codex SDK, Copilot
CLI, OpenHands, SWE-agent, Claude Code, Aider) is an *executor*. It can be put
inside any shell above, but by itself does not reliably provide admission,
leases, hard budgets, credential revocation, protected delivery, or durable
operator controls. A multi-agent framework is also not an overseer; it can
increase variance and cost while leaving authority questions unresolved.

## Recommended selection matrix

| Option | Deterministic controls supplied | What remains yours | Fit now |
| --- | --- | --- | --- |
| GitHub Agentic Workflows, `engine: copilot` | Trigger, declared permissions, safe outputs, isolated Actions environment, locked workflow, AIC cap/audit | Issue admission schema, path policy, CI, protected merge/deploy gates | **Trial first** |
| GitHub Agentic Workflows, `engine: codex` | Same shell; changes only the executor | Same as Copilot; third-party engine authentication and invoice reconciliation | **Trial second, same tasks** |
| Actions + Codex SDK/API | Ordinary Actions controls and anything encoded in your policy action | Entire agent lifecycle, worker sandbox, costs, cancellation, prompts, evidence schema | Later; only for a demonstrated GitHub-native gap |
| Temporal / Azure Durable Functions + an executor | Durable state, retries, schedules, status and explicit lifecycle APIs | Worker cancellation/credential revocation, sandbox, PR gates, all coding semantics | Later; only for queues, waits or private runners |
| LangGraph/LangSmith + an executor | Graph state, checkpoints, resumable human interrupts and traces | GitHub admission/delivery controls, isolation, operational/data surface | No, unless building an agent product |

## Concrete pilot: one shell, two engines

Keep the first pilot deliberately narrow:

```text
workflow_dispatch
  -> validate typed task contract + risk/path allowlist
  -> one active run per repository
  -> Agentic Workflow (engine = copilot OR codex)
  -> safe-output: create draft PR only
  -> normal CI + deterministic diff policy
  -> CODEOWNER/human review -> protected merge queue
```

Use four mundane tasks: documentation correction, isolated test addition,
lint/type remediation, and a small local refactor. For each, record engine,
workflow revision/lockfile SHA, task-contract SHA, run ID, token/AIC estimate,
wall time, changed paths, CI result, review rework, and cancel latency. Do not
give either engine a production secret, deployment permission, write access to
workflow policy, or permission to merge.

### Initial GitHub policy shape

- The workflow is manually dispatched by a maintainer; no issue-comment,
  schedule, fork or PR-body trigger in the first phase.
- Repository branch protection only accepts required checks from expected Apps.
- Agentic-workflow `safe-outputs` permits only `create-pull-request`; separate
  read-only workflows may create comments/issues.
- Use a dedicated `agent-low-risk` profile. Explicit `tools:` is an allowlist;
  omitting it enables all available tools. In GitHub custom agents,
  `disable-model-invocation: true` prevents automatic selection, and profiles
  are versioned by Git commit SHA. [6]
- A stop runbook disables the workflow, cancels the run, removes the admission
  label, revokes the engine/API credential if applicable, and closes the PR.
- A deployment workflow is distinct and receives OIDC credentials only after
  protected post-merge gates.

## Evidence

GitHub Agentic Workflows supports Copilot, Claude, Codex and Gemini engines.
The workflow frontmatter declares permissions and `safe-outputs`; agents run
read-only by default in firewalled environments, while secrets remain in
downstream jobs. GitHub documents a `max-ai-credits` cap and run/audit commands
for usage evidence. [1][2]

GitHub custom-agent profiles can pin the available tool list and model-driven
selection behaviour. Their configuration is revisioned by Git SHA, which makes
the executor profile reviewable alongside code. This is useful control, but it
does not replace external authorization. [6]

The Codex TypeScript SDK starts and resumes threads, streams structured events,
supports JSON-schema output, and permits an explicit child environment and
working directory. OpenAI's official API guidance also describes coding models,
allowed tools, structured tool constraints and a configurable reasoning budget.
[3][4]

Temporal/Azure-style durable orchestration supplies persistent lifecycle state,
but a coordinator cancel request is not necessarily a worker kill. Azure
explicitly warns that terminating an orchestration does not propagate to
activities/sub-orchestrations. Therefore a worker must also have its own
deadline, short-lived identity and revocation path. [7][8]

LangGraph explicitly supports mixing deterministic and LLM-driven steps,
persistence and human-in-the-loop. Those are strong primitives for a custom
stateful agent product, but represent a larger control-plane build. [5]

## Trade-offs and risks

- Agentic Workflows is the lowest-operations choice, but its feature set and
  engine integration must be validated against the exact GitHub plan and
  repository ownership. Do not assume a preview or plan-limited feature is an
  enforceable production control until the pilot proves it.
- `max-ai-credits` bounds inference billed through the workflow, not all damage
  an over-privileged worker could cause. Retain OS/container limits, GitHub
  permissions and credential expiry.
- A custom Actions wrapper can be more exact than an Agentic Workflow, but it
  creates an application to maintain. It is not a cheaper first experiment.
- Durable orchestration is valuable for pause/resume and operations, not for
  judging model output. Never use the coordinator's status as proof that a
  subprocess lost access.

## Open questions

1. Are the target repositories organization-owned and on a Copilot plan that
   enables organization billing for Agentic Workflows? Personal and third-party
   engine use needs a managed secret/API key. [2]
2. Which four low-risk tasks and command/path allowlists should form the fair
   Copilot/Codex baseline?
3. Which signal justifies adding a custom wrapper: provider routing, a private
   VPC test, long human approval waits, cross-repo scheduling, or something
   else measurable?

## Sources

1. GitHub. "[About GitHub Agentic Workflows](https://docs.github.com/en/enterprise-cloud%40latest/copilot/concepts/agents/about-github-agentic-workflows)." Accessed September 13, 2026.
2. GitHub. "[Creating GitHub Agentic Workflows](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows)." Accessed September 13, 2026.
3. OpenAI. "[Model guidance: GPT-5.2](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2)." Accessed September 13, 2026.
4. OpenAI. "[Codex TypeScript SDK](https://github.com/openai/codex/blob/main/sdk/typescript/README.md)." Accessed September 13, 2026.
5. LangChain. "[LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)." Accessed September 13, 2026.
6. GitHub. "[Custom agents configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)." Accessed September 13, 2026.
7. Microsoft. "[Durable Functions overview](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview)." Accessed September 13, 2026.
8. Microsoft. "[Manage orchestration instances](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-instance-management)." Accessed September 13, 2026.
