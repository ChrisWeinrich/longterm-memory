---
title: "OpenHands Coding-Agent Platform"
type: raw-research-report
tags: [research, coding-agents, openhands, orchestration, local-first, security]
origin: research-workflow
created: 2026-09-13
---

# OpenHands Coding-Agent Platform

## Conclusion

OpenHands is a credible **local coding-agent execution platform and SDK**, but
it is not by itself a deterministic delivery pipeline. Its strongest fit is as
the replaceable worker behind an existing deterministic task controller. For a
macOS environment that already has a Go task system, that system should retain
admission, state transitions, budgets, cancellation policy and acceptance
gates. OpenHands should receive one bounded task in one disposable worktree,
operate inside a Docker-backed workspace, and return a patch, branch or draft
pull request.

OpenHands now spans several layers: a Python SDK, typed tools and events,
workspace abstractions, an agent server, CLI/browser applications, local and
remote sandboxes, GitHub/event automation, multi-agent delegation, model
routing, ACP-backed agents and OpenTelemetry tracing. The SDK is the shared
foundation used by the OpenHands interfaces and cloud service.[^1] This makes
it substantially more capable than a single coding CLI, while also making
careful layer selection important.

For the stated setup, trial only the **SDK/agent-server plus Docker workspace**
path. Do not initially adopt OpenHands Cloud automations, Agent Canvas as a new
fleet control plane, multi-agent delegation or local models. Those are separate
capabilities with separate operational and security costs. Compare OpenHands
against the existing direct Codex worker using the same Go task contract.

## Product and architecture map

| Layer | Role | Relevant capability | Initial use |
| --- | --- | --- | --- |
| `openhands.sdk` | Agent kernel | Reason/action loop, conversations, typed events, LLM abstraction, skills, security analysis | Yes |
| `openhands.tools` | Capability library | Bash, file editing, browser and MCP tools | Minimal allowlist only |
| `openhands.workspace` | Execution boundary | Local, Docker and remote workspace implementations | Docker workspace |
| `openhands.agent_server` | Remote/API boundary | REST/WebSocket access and multi-user execution | Optional adapter for Go |
| CLI / local GUI / Agent Canvas | Human interface | Interactive local agent work and backend selection | Trial convenience only |
| Cloud / automations | Hosted control surface | GitHub events, webhooks, schedules and managed sandboxes | Defer |

The V1 SDK separates agent, tools, workspace and agent server. The same agent
code can switch from `LocalWorkspace` to Docker or remote workspaces, while the
server exposes conversations and workspaces through REST and WebSocket APIs.[^1]
That boundary is useful for a Go controller: Go does not need to embed Python;
it can invoke a narrow worker process or call an agent server.

The core agent is stateless relative to the event history. Each `step()` reads
conversation events, asks the LLM for an action, validates it, executes a tool
or waits for confirmation, and writes the resulting event. Individual steps
are interruptible and conversation state supplies continuation.[^2] This is a
controllable agent loop, not a deterministic workflow graph.

## Capability inventory

### Coding and tool execution

OpenHands provides typed action/observation tools with Pydantic schemas,
validation, automatic model-facing schemas and a tool registry. Its standard
tooling covers shell commands, file operations, browser access and MCP.[^3]
The platform can therefore inspect repositories, edit files, run builds/tests,
browse supporting material and call explicitly configured external services.

The tool layer is an authority surface. MCP tools are discovered during agent
initialization, so an unrestricted MCP configuration silently enlarges what a
task may do. A local pilot should supply a small task-specific tool set instead
of inheriting every available tool.

### Workspaces and sandboxes

The workspace interface normalizes command execution, file operations and
resource lifecycle across local processes, containers and remote servers.[^4]
OpenHands recommends Docker for local sandboxing because it improves isolation
and reproducibility. A host path mounted read-write into `/workspace` can be
modified by the agent.[^5]

Process mode is explicitly not isolated: the agent can read and write anything
available to the current macOS user and execute host commands. The official
documentation advises Docker when uncertain.[^6] Process mode is unsuitable
for unattended work on this Mac.

Docker lowers risk but does not automatically create a hard host boundary.
Installation patterns that expose the Docker socket give the coordinating
container substantial control over Docker. Host mounts, socket exposure,
network access and injected credentials must therefore be considered part of
the trusted computing base, not assumed safe because a container exists.[^7]

### Models and Codex integration

The normal LLM layer uses LiteLLM and supports OpenAI, Anthropic, Google,
Azure/Bedrock and local providers. OpenHands warns that coding agents issue
many model requests and that most local/open models are less reliable or may
produce malformed output.[^8] For this environment, API-backed Codex is the
useful baseline; a local LLM is a separate hardware and quality experiment.

OpenHands also supports ACP agents. `ACPAgent` starts an ACP-compatible server
as a subprocess, sends messages over JSON-RPC and lets that server own its LLM,
tools and execution. It captures token/cost metrics and supports cleanup.[^9]
Current documentation describes ChatGPT subscription login or provider API-key
fallbacks. It also states that ACP permission requests may be auto-approved;
the sandbox and outer policy must therefore carry the safety boundary.[^9]

### Task delegation and multiple agents

`TaskToolSet` lets a parent invoke registered subagents synchronously. Tasks
have IDs, completion/error state, persisted conversation context and optional
resumption.[^10] This can isolate specialist context, but it does not make the
result more deterministic. It increases token cost, state and correlated
failure modes. It should remain outside the first trial.

### Automation and GitHub

OpenHands supports issue/PR resolution through GitHub actions and hosted GitHub
integration. A `fix-me` label or agent mention can trigger work, followed by a
pull request and iterative feedback. The resolver exposes a maximum iteration
setting and configurable model/container image.[^11]

Hosted event automations can react to GitHub PR, issue and push events or custom
webhooks.[^12] These triggers are convenient but are not adequate admission
control by themselves. Issue/comment text is untrusted model input, and an
automatic label/mention path should only be enabled after the deterministic Go
controller can validate actor, risk class, scope and concurrency.

### Observability

The SDK has OpenTelemetry tracing for agent steps, tool execution, LLM calls,
conversation lifecycle and optional browser sessions. It can export to an OTLP
backend such as Jaeger, MLflow or Honeycomb.[^13] This is good diagnostic
evidence, but trace capture can contain code, prompts, tool output or secrets.
For a local-first pilot, write minimal local traces and redact before any remote
export.

### Security analysis and human confirmation

The core agent can classify actions by risk and pause high-risk actions for
confirmation.[^2] This is useful defense in depth. It remains model/framework
policy, not an authorization boundary: the Go controller and container must
make forbidden effects impossible even if classification fails.

The academic AgentDojo benchmark demonstrates the structural problem. Agents
that consume untrusted data can confuse instructions with data; its 97 tasks
and 629 security cases found both ordinary task failures and indirect prompt-
injection failures.[^14] Therefore repository text, issues, test logs, web pages
and MCP output must all be treated as potentially adversarial.

## Deterministic-pipeline fit

OpenHands can execute inside a deterministic pipeline. It does not supply the
complete pipeline contract. The recommended authority split is:

```text
Go task controller
  -> validate signed/typed task contract
  -> create disposable Git worktree
  -> start bounded OpenHands Docker worker
  -> collect events, usage, result and diff
  -> terminate worker and revoke its lease
  -> deterministic tests + diff/path policy
  -> branch or draft PR only
  -> human / protected merge
```

The Go controller should own the state machine:

```text
proposed -> admitted -> running -> verifying -> review-ready
                  \-> cancelled / timed-out / policy-blocked / failed
```

Every transition should be idempotent and keyed by one immutable task ID.
OpenHands conversation IDs, model/provider, image digest, worktree commit,
policy version, limits and produced diff should be recorded as evidence.

### Minimum task contract

| Field | Initial rule |
| --- | --- |
| Goal and acceptance checks | Explicit, machine-verifiable where possible |
| Base commit | Immutable SHA |
| Allowed/forbidden paths | Deny workflow, secrets, auth, IaC and dotfile ownership paths initially |
| Allowed commands/tools | Narrow build/test/edit list; MCP off by default |
| Resource limits | Wall time, iterations, tokens/cost, processes, CPU/RAM and network |
| Output | Patch/branch/draft PR plus evidence; no merge/deploy |
| Stop semantics | Cancel conversation, kill container/process, revoke credentials |

### What OpenHands should own

- Agent reasoning and code-oriented tool loop.
- Workspace-level command and file operations.
- Conversation events and resumable execution context.
- Provider/ACP adapter and usage telemetry.
- Optional action confirmation as defense in depth.

### What it should not own initially

- Determining whether arbitrary task text is authorized.
- Access to the primary checkout or user home.
- Production/cloud credentials, deployment or merge authority.
- Retry policy after a policy or security failure.
- The final statement that tests, scope and delivery policy passed.

## Alternatives

| Alternative | Stronger than OpenHands at | Weaker / different | Fit |
| --- | --- | --- | --- |
| Direct Codex SDK/API behind Go | Smaller stack; native Codex events/config; less translation | Provider-specific; Go still builds workspace/tool lifecycle | Best baseline comparison |
| GitHub Agentic Workflows | Git-native triggers, declared permissions, safe outputs, hardened lock workflow, AIC limit | Cloud/GitHub-centric and public preview | Best cloud pipeline companion |
| LangGraph + Deep Agents | Explicit state graph, persistence, interrupts and custom deterministic/agentic composition | General agent framework; more application/platform work | Only if building a custom agent service |
| Temporal / Azure Durable Functions | Durable queues, retries, timers, long waits and workflow recovery | Not coding-specific; requires a separate coding worker | Later for multi-host/long-running control |
| Herdr | Persistent terminal sessions, visibility and attachment to installed CLIs | Terminal runtime, not sandboxed policy engine or delivery pipeline | Human-supervised local sessions |
| Raw coding CLIs | Lowest setup and familiar interaction | No common lifecycle, sandbox or provider-neutral API | Interactive work, not unattended pipeline |

GitHub Agentic Workflows is the closest ready-made cloud control plane. It
supports Copilot and Codex engines, compiles Markdown to a hardened Actions
workflow, defaults repository access to read-only and restricts writes through
declared safe outputs. It also exposes usage/audit data and a per-run AIC
ceiling.[^15] OpenHands is stronger as a local/provider-neutral execution
platform; GitHub is stronger as the authority and delivery boundary.

LangGraph explicitly mixes deterministic nodes with agentic nodes and provides
persistence and human interrupts. It is a better fit when the workflow itself
is the product.[^16] For the existing Go controller, replacing its state machine
with LangGraph would add a second orchestration system without first proving a
gap.

Herdr, already documented in this Wiki, addresses durable terminal sessions and
operator visibility. It remains complementary: use Herdr for attended CLI work,
OpenHands for isolated programmatic workers, and Go/GitHub policy for authority.

## Recommended trial

### Phase 0 — boundary proof

1. Use a disposable repository and fresh worktree at a fixed commit.
2. Run one OpenHands worker in Docker with no home mount, SSH agent, MCP or
   production credentials.
3. Allow only repository editing and one test command.
4. Verify that cancellation kills the worker and that no filesystem changes
   appear outside the worktree.
5. Inspect event/trace output for secret and source leakage.

### Phase 1 — comparative tasks

Run the same four tasks through direct Codex and OpenHands+Codex: documentation
fix, isolated test, lint/type correction and small refactor. Record completion,
wall time, tokens/cost, changed paths, test results, review rework, policy
violations, cleanup and cancellation latency.

The goal is not to rank model intelligence; the model remains the same. The
trial asks whether OpenHands contributes enough sandboxing, lifecycle,
provider portability and observability to justify its additional Python/server
stack.

### Acceptance gates

- No host write outside the task worktree.
- Reproducible container image pinned by digest.
- Reliable timeout and cleanup, including ACP subprocess cleanup.
- Secrets injected only for one task and absent from logs/traces.
- Structured evidence can be consumed by the Go controller.
- No material increase in review rework versus direct Codex.
- A documented upgrade/rollback path exists.

Reject or defer OpenHands if direct Codex already satisfies the workflow with
less operational surface, or if Docker/socket/mount boundaries cannot be made
acceptable on the Mac.

## Trade-offs and risks

- OpenHands is undergoing a V1 architectural transition; documentation includes
  both new SDK paths and deprecated V0/local-GUI material. Pin versions and
  validate the exact interfaces used.
- Provider neutrality is valuable, but LiteLLM/ACP add translation and version
  compatibility layers.
- Docker isolation is only as strong as mounts, socket exposure, network and
  host configuration.
- Event automations can turn untrusted issue/comment content into agent input.
- OTEL and conversation persistence can retain sensitive source or prompts.
- Subagents and automatic retries increase cost and make failure analysis harder.
- Subscription authentication may be convenient but needs explicit review
  before unattended automation; an API key with task-scoped budget/accounting
  may be operationally clearer.

## Open questions

1. What API or process contract does the existing Go task system expose?
2. Can the agent server run without broad Docker-socket exposure in the chosen
   local deployment shape?
3. Does ACP-backed Codex preserve the required sandbox and approval semantics,
   especially where ACP permissions are auto-approved?
4. Which event and usage fields are stable enough for the Go evidence schema?
5. Where are conversations and traces persisted, and what is the deletion/
   retention policy for the pinned version?
6. Does OpenHands add enough value over direct Codex to justify a second runtime?

## Sources

[^1]: OpenHands. "[Software Agent SDK architecture](https://docs.openhands.dev/sdk/arch/overview)." Accessed September 13, 2026.
[^2]: OpenHands. "[Agent architecture](https://docs.openhands.dev/sdk/arch/agent)." Accessed September 13, 2026.
[^3]: OpenHands. "[Tool System & MCP](https://docs.openhands.dev/sdk/arch/tool-system)." Accessed September 13, 2026.
[^4]: OpenHands. "[Workspace architecture](https://docs.openhands.dev/sdk/arch/workspace)." Accessed September 13, 2026.
[^5]: OpenHands. "[Docker Sandbox](https://docs.openhands.dev/openhands/usage/sandboxes/docker)." Accessed September 13, 2026.
[^6]: OpenHands. "[Process Sandbox](https://docs.openhands.dev/openhands/usage/sandboxes/process)." Accessed September 13, 2026.
[^7]: OpenHands. "[Local setup](https://docs.openhands.dev/openhands/usage/run-openhands/local-setup)." Accessed September 13, 2026.
[^8]: OpenHands. "[LLM overview](https://docs.openhands.dev/openhands/usage/llms/llms)." Accessed September 13, 2026.
[^9]: OpenHands. "[ACP Agent](https://docs.openhands.dev/sdk/guides/agent-acp)." Accessed September 13, 2026.
[^10]: OpenHands. "[Task Tool Set](https://docs.openhands.dev/sdk/guides/task-tool-set)." Accessed September 13, 2026.
[^11]: OpenHands. "[OpenHands GitHub Action](https://docs.openhands.dev/openhands/usage/run-openhands/github-action)." Accessed September 13, 2026; the direct page returned inconsistently during retrieval.
[^12]: OpenHands. "[Event-Based Automations](https://docs.openhands.dev/openhands/usage/automations/event-automations)." Accessed September 13, 2026.
[^13]: OpenHands. "[Observability & Tracing](https://docs.openhands.dev/sdk/guides/observability)." Accessed September 13, 2026.
[^14]: Edoardo Debenedetti et al. "[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)." NeurIPS Datasets and Benchmarks Track, 2024.
[^15]: GitHub. "[About GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows)." Accessed September 13, 2026.
[^16]: LangChain. "[LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)." Accessed September 13, 2026.
