---
title: "Private Codex and Claude Agent Supervision Control Plane"
type: raw-research-report
tags: [research, coding-agents, orchestration, terminal, tmux, codex, claude-code, mcp, chezmoi]
origin: research-workflow
created: 2026-09-12
---

# Private Codex and Claude Agent Supervision Control Plane

## Conclusion

### Recommendation

**Trial Agent Orchestrator (AO) first, as a desktop-local supervisor rather
than a replacement terminal.** It is the strongest documented fit for the
whole lifecycle: one isolated worktree per worker, Codex/Claude Code/OpenCode
selection, durable state, calculated attention states, native-terminal or
structured-chat execution, PR/CI/review feedback routing, and a local daemon
that can reconnect to detached session hosts after its UI or daemon is
replaced. Its supported-agent list explicitly includes Codex, Claude Code, and
OpenCode, and it ships Apple-silicon and Intel macOS builds. [AO README]

AO does **not** meet the literal TUI-first preference: it is a desktop app with
a CLI and local HTTP/SSE/WebSocket daemon. It should therefore be trialled as
the fleet and lifecycle layer beside a normal terminal/Neovim setup, not as a
new universal terminal. Its anonymous telemetry declaration and the local
HTTP control plane are acceptance gates, not details to wave away. In
particular, AO says it records the GitHub owner/account for a project; for a
personal project that is a personal username. [AO README]

**Fallback: Agent Manager.** It is the best small, terminal-native option for
the stated 2–10 persistent-session range. It runs installed CLIs unchanged in
a private tmux server; has a project tree, quick prompt without attachment,
per-session worktrees, native Codex/Claude/OpenCode status rules, revive/fork,
and an in-TUI diff/comment round-trip. Crucially, it does not need to own or
rewrite the existing agent configuration. Its status is heuristic screen
matching (or optional Claude hooks), so it is a superior daily cockpit but a
weaker authoritative control plane than AO. [Agent Manager README; Agent
Manager configuration]

**Do not trial Herdr, Agent Deck, NTM, or Paseo first** for this narrow goal.
They are credible, but each has a larger unwanted ownership surface: Herdr
replaces the terminal runtime and installs agent hooks; Agent Deck can
materialize skills and attach MCP configuration; NTM is deliberately a large,
tmux-centric orchestration ecosystem; Paseo is excellent multi-provider
infrastructure but adds daemon, mobile/web/relay, plugin, and configuration
scope that this local supervision decision does not need. They remain useful
second-wave evaluations if AO and Agent Manager fail a concrete test.

### Target composition

| Responsibility | Recommended owner | Why |
| --- | --- | --- |
| Fleet supervision, task/worktree lifecycle, CI and PR feedback | AO (first trial) | The only evaluated candidate with an explicitly documented end-to-end worker/PR/CI/review model. |
| Persistent native agent terminal | AO native-terminal worker during AO trial; Agent Manager tmux server in fallback | Avoids a second generic multiplexer. AO already owns its terminal worker runtime; Agent Manager deliberately owns only a separate tmux socket. |
| Folder, file, and code navigation | Existing Neovim | No evidence requires replacing it. |
| Local diff review | Hunk in a separate terminal pane | Independent, review-first, works directly against the selected worktree and can expose JSON live-session state. |
| PR review and requested changes | AO when it is the supervisor; otherwise GitHub CLI/browser plus the owning agent | Hunk is a local-diff viewer, not a GitHub PR-review client. |
| Markdown reading | Existing Obsidian for vault reading; a normal terminal pager/TUI only if separately chosen | No researched candidate supplies an Obsidian-equivalent knowledge-reading workflow. |
| MCP health | MCP Inspector CLI, supplied a read-only config | Explicit `--config` is a read-only session; use `initialize`/`tools/list`, never an interactive config catalog for this probe. |

This map leaves ChezMoi as the sole owner of global Codex/Claude/Copilot,
shared skills, MCP registrations, launchers, and guidance. The supervisor may
receive paths and launch already-installed binaries; it must not become a
second configuration authority.

## Evidence

### Decision matrix

Ratings are decision-fit ratings for this personal Mac and stated constraints,
not generic product quality. “Documented” means the cited upstream source says
so; it is not a local verification.

| Candidate | Codex / Claude / OpenCode | Persistence and recovery | Status mechanism / limitation | Worktrees and review | Machine surface | Config and trust boundary | Fit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AO** | All three listed among 27 agents; terminal or structured Chat. | Detached per-session hosts let Codex and ACP Chat processes reconnect after desktop/daemon replacement; reboot/sleep/SSH semantics were not verified. | Durable activity facts; display state derived at read time. `waiting_input` and `blocked` are distinct, with automation prohibited from injecting into blocked sessions. | One isolated git worktree per worker; worker keeps task, terminal, diff, PR, CI, and review together. | Loopback HTTP daemon, REST, SSE, terminal WebSocket, CLI. | Desktop-local daemon; automatic update check; anonymous telemetry includes GitHub owner segment. Config mutation / hook ownership needs live inspection. | **First trial**, subject to telemetry and listener validation. |
| **Agent Manager** | All three explicitly supported, and launched as installed CLIs. | Private `tmux -L agentmgr`; sessions survive manager exit. Revive/fork uses the tool’s native resume semantics. Reboot/sleep behavior is tmux/agent dependent. | Polls visible pane text every 2 seconds by default; optional Claude hooks. Rules break when an upstream TUI changes. | Optional per-session worktree; full-file diff review sends a comment round back to the pane. | TUI/CLI and tmux socket; no documented HTTP service in sources reviewed. | Creates macOS config and SQLite state under `~/Library/Application Support/agent-manager`; runs a separate tmux server. It retains existing agent config/MCPs. | **Best fallback**; the least disruptive TUI-first architecture. |
| **Herdr** | Claude, Codex, and OpenCode integrations documented. | Own PTY runtime; native restore can resume supported agent sessions after server restart. Server restart otherwise stops processes; reboot/sleep/SSH behavior needs test. | Screen-manifest detection, with native identity reported through local hooks. | Workspaces/tabs are runtime concepts; no equivalent PR/review lifecycle evidence found. | CLI and newline-delimited JSON on Unix-domain sockets; event subscriptions. | `herdr integration install` writes Claude hooks/settings and Codex hook files, `hooks.json`, and enables Codex hooks in `config.toml`. | Strong technical runtime, but **too invasive** as first tmux-dev replacement. |
| **Agent Deck** | Claude, Codex, OpenCode supported; TUI/CLI/web surfaces. | tmux-backed sessions and optional watchdog; recovery claims need direct test. | TUI status filters include running/waiting/idle/error; detection authority not fully verified. | Worktree sessions and in-product manager. | CLI/TUI plus optional browser API/UI; HTTP MCP administration needs a token. | `mcp attach` may write a project `.mcp.json`; `skill attach` materializes content under project `.claude/skills/` and changes `.agent-deck/skills.toml`. | **Reject for first trial**: collides with ChezMoi ownership unless tightly disabled. |
| **NTM** | Claude, Codex and OpenCode listed. | tmux is its core; checkpoints, history, audit and event streams claimed. | Agent-aware panes, but detailed false-positive/failure behaviour was not verified. | Worktrees/file reservations/assignment workflows are ecosystem features. | Robot JSON flags; `ntm serve` offers OpenAPI REST/WebSocket. | User config plus project `.ntm/` assets; many optional companion tools and policies. | **Reject for first trial**: powerful but much more opinionated than needed. |
| **Paseo** | Claude, Codex, OpenCode all explicitly supported. | Daemon has file-based JSON persistence in `~/.paseo`; docs say running agents continue on daemon restart and clients reconnect. Reboot/sleep/SSH needs test. | Provider and agent lifecycle through daemon; exact status false-negative modes need trial. | CLI accepts `--worktree`; data model documents worktree recovery. | CLI, WebSocket SDK/API, desktop/web/mobile, optional encrypted relay/direct TCP/Tailscale. | `~/.paseo/config.json` can pin provider commands; runs login shell for desktop PATH; trusted plugins run on daemon/client. | **Defer**: technically broad and polished, but remote/mobile/relay scope is excess here. |

### AO: why it wins the first trial

AO’s architecture directly models this problem rather than merely grouping
terminals. Its documentation says each session owns an isolated worktree and a
single committed interface mode. A TUI worker runs the selected agent in a
tmux runtime; a Chat worker uses a native protocol controller. Detached hosts
keep Codex and ACP chat processes alive through desktop/daemon replacement.
[AO architecture]

That matters for the required failure sequence: closing a terminal/UI is not
assumed to equal ending a task, while a separate `blocked` activity fact is
protected from blind prompt injection. AO stores activity, termination,
session-interface transitions, and PR facts; display status such as working,
needs input, CI failed, and mergeable is recalculated from those facts rather
than saved as a stale label. [AO architecture]

The source also documents the security-relevant local boundary: an HTTP daemon
at `127.0.0.1`, REST controllers, SSE events, and a terminal WebSocket. It
polls PRs every 30 seconds through the GitHub API. This is a good structured
surface for a future read-only monitor, but it is still a control plane: test
the exact listener, authentication, filesystem data directory, and any
GitHub-token scope before using it against real projects. [AO architecture]

AO’s official README documents Apple Silicon and Intel macOS downloads and
explicitly names Codex, Claude Code, and OpenCode. It frames worker creation
as choosing the agent/model/interface per task, so the desired agent selection
is per worker rather than a global provider rewrite. The docs retrieved do not
prove the exact command line or prove no user-home mutation; that is a
pre-install acceptance check, not a positive claim. [AO README]

### Agent Manager: why it is the fallback

Agent Manager’s decisive property is modesty. It puts each agent into a
persistent tmux session on a private `agentmgr` socket and launches the
installed CLI “as-is,” retaining its login, config files, and MCP servers.
Thus it can preserve the ChezMoi-owned Codex and Claude configurations instead
of trying to administer them. It supports macOS through Homebrew and separates
its own tmux server from the user’s existing tmux server. [Agent Manager
README]

It is also unusually close to the requested operator experience: project-tree
grouping/folding, quick prompts to an unfocused pane, session fork/revive,
optional worktrees, a live TUI status list, and line comments that return to
the agent as a review prompt. [Agent Manager README]

Its weakness is honest and important. By default it polls pane text every two
seconds, matching configurable regular expressions; a changed Codex/Claude
terminal presentation can make status wrong. Claude hooks are an optional
alternative, but they become another configuration mutation. Treat state as
“operator attention hint,” never as a safety-grade authority, and validate
waiting/permission/error classifications after every substantial CLI upgrade.
[Agent Manager configuration]

### Rejected and deferred candidates

**Herdr** is the best evaluated replacement for a terminal runtime, not the
best low-risk supervisor beside an existing one. Its socket is local and
structured (newline-delimited JSON over a Unix socket), and its CLI can emit a
JSON schema; those are excellent properties. [Herdr socket API] But its
Codex integration writes under `~/.codex`, updates `hooks.json`, and ensures
the hooks feature in `config.toml`; Claude integration similarly adds a hook
and updates settings. That violates the requested “no unmanaged global
configuration change” condition unless ChezMoi deliberately owns every change.
[Herdr integrations]

**Agent Deck** has a capable TUI and a useful read-only browser-client option,
but it is explicitly a manager of MCPs and skills. Its documentation says a
skill attachment writes into the project’s `.claude/skills/` and updates
`.agent-deck/skills.toml`; its MCP attachment can write a project `.mcp.json`.
Those are unacceptable defaults for a trial intended to preserve declarative
ChezMoi authority. [Agent Deck skills; Agent Deck README]

**NTM** is an orchestration platform on top of tmux, not a tmux replacement.
It has a TUI, robot JSON API, `ntm serve` REST/WebSocket surface, checkpoints,
and a wide package of project/user configuration, policies, worktrees, file
reservations, and companion utilities. That makes it a credible later choice
if the actual need becomes coordinated swarms and policy/audit workflows.
For this task, its integration breadth is a cost and additional configuration
surface, not a benefit. [NTM README; NTM AGENTS]

**Paseo** most closely matches multi-provider breadth, including Codex,
Claude, and OpenCode, with CLI commands to list, attach, and send follow-ups,
and a WebSocket SDK. [Paseo README] It is not rejected because it is weak; it
is deferred because its daemon supports desktop/web/mobile, pairing, direct
TCP/Tailscale, an optional E2E relay, plugins that execute trusted TypeScript
on the daemon machine, and provider configuration under `~/.paseo`. A later
Paseo trial should start offline/local-only with relay and plugins disabled.
[Paseo README; Paseo troubleshooting]

### Companion workflow

Run **Hunk** in a dedicated terminal pane rooted in the selected worker’s
worktree, e.g. `hunk diff --watch`. Hunk is explicitly a review-first terminal
viewer and supports Git working-tree diffs, watch reload, inline agent notes,
and JSON commands that expose live review/session context. It should be the
human local-diff surface even when AO or Agent Manager has a built-in diff
view. [Hunk README; Hunk CLI reference]

Hunk does not replace GitHub PR review: it does not establish PR identity,
fetch review comments, or submit GitHub review actions. With AO, use AO’s
worker-attached PR/review loop; with Agent Manager, use `gh pr view` / `gh pr
checks` and GitHub’s review interface, then send the review result back through
the manager’s quick prompt or the attached terminal. This separation prevents
a local worktree diff from being mistaken for a remote PR review.

For MCP health, use **MCP Inspector CLI** with a supplied `--config` file, not
its writable catalog. The official CLI supports a read-only config session and
`initialize`, `tools/list`, `resources/list`, and `prompts/list`. It also
requires OAuth callback listeners to bind loopback only. Probe with
`initialize` and `tools/list`; do not call tools in the baseline health test.
[MCP Inspector CLI]

## Trade-offs and risks

| Risk | Impact | Guardrail |
| --- | --- | --- |
| Supervisor manages agent configuration | Can overwrite or bypass ChezMoi source of truth. | Trial only in a throwaway repo with temporary home/config paths if supported. Reject any automatic global MCP/skill/hook write. |
| Status inference is wrong | A waiting, approval-blocked, or failed agent can be missed or prompted unsafely. | Record ground truth for each test state; never automate `send` on inferred status until proven. |
| Persistent processes after UI close | Desired for recovery but can leave credentials and worktrees live. | Require an explicit list/stop workflow and verify owner PID, tmux/socket, and worktree cleanup. |
| Local control endpoints | A local process can steer agents or read output. | Confirm loopback/Unix socket only, file permissions, auth, and no unrequested relay, LAN bind, or SSH forwarding. |
| Desktop environment differs from shell | Agent binary may be absent or launch with different PATH/environment. | Start with terminal launch. If desktop mode is used, compare its environment and preserve a clean login-shell path via ChezMoi. |
| Telemetry or remote/mobile features | Violates local-first/privacy expectation. | Do not accept AO without reviewing/choosing telemetry behavior; decline Paseo pairing/relay; do not install plugins. |
| Worktree cleanup | Unreviewed changes may be deleted or abandoned checkout accumulates. | Use a disposable repo; check `git worktree list` before and after each teardown. |

## Open questions

These are deliberately unresolved until an isolated trial; upstream documents
retrieved did not prove them.

1. AO’s exact state/config/data locations, listener authentication model,
   telemetry opt-out controls, and all automatic filesystem mutations on first
   launch.
2. AO behaviour across macOS sleep, full reboot, and SSH disconnect; its docs
   support daemon/desktop replacement but do not establish survival across
   process-host loss.
3. AO’s exact per-worker Codex/Claude/OpenCode command/adaptor configuration,
   including whether it needs hooks, MCP edits, or provider credentials beyond
   the already-authenticated CLI.
4. Whether AO’s dashboard navigation remains usable for more than ten active
   sessions across multiple repositories; no numerical scale limit was found.
5. Whether Agent Manager’s pane rules correctly classify the current installed
   Codex and Claude Code versions, especially approval dialogs and rate limits.
6. Whether Hunk’s live JSON session commands are sufficient for the desired
   review-comment handoff without a custom integration.
7. A terminal Markdown reader that gives an acceptable Obsidian-like reading
   experience is a separate selection; no candidate here establishes one.

## No-install-yet validation plan

The plan is intentionally a gated, throwaway exercise. It authorizes no
ChezMoi edit, global agent/MCP/skill/hook mutation, remote listener, relay, or
real repository work.

1. Create a disposable local Git repository with a harmless test fixture and
   two branches/worktrees. Snapshot `git worktree list`, `git status`, relevant
   agent config checksums, active tmux servers, and listeners before the trial.
2. Install/run AO only by its documented method in an isolated trial account or
   temporary support/config location if AO offers one. Before starting workers,
   inspect the newly created files, `lsof`/socket/listener information, update
   setting, telemetry setting, and processes. Stop if it edits `~/.codex`,
   `~/.claude`, shared MCP files, or ChezMoi-managed files without an explicit
   reversible plan.
3. Create four independent workers: two Codex, two Claude Code; select
   OpenCode for one optional fifth check only after the four core workers work.
   Use two worktrees and two ordinary repository-root tasks. Confirm displayed
   agent, repo, branch, worktree path, and session identifier for every worker.
4. Induce and record four states: a normal active turn; an explicit “waiting
   for your answer” prompt; an approval/permission block; and a harmless
   command-not-found error. Compare the screen, process, AO state, and any
   structured API/CLI output. Verify that a blocked session cannot receive an
   automated follow-up and that a follow-up reaches exactly the intended
   waiting worker.
5. Close the attached terminal, close/reopen the AO desktop UI, then restart
   its daemon if the supported workflow permits it. Confirm which processes,
   native conversations, task state, worktrees, and pending prompts survive.
   Do not claim reboot/sleep recovery until those separate destructive-to-turn
   tests are run with disposable sessions.
6. In a separate terminal, run `hunk diff --watch` in each changed worktree.
   Add a review note and ensure it remains attributable to that checkout;
   then exercise AO’s diff/PR feedback only with a throwaway GitHub repository
   or skip the remote PR step. Do not equate Hunk output with PR review.
7. Prepare a minimal non-secret MCP configuration copy and run MCP Inspector
   with `--config ... --server <name> --method initialize`, then `tools/list`.
   Confirm no config/catalog write and no public listener. Do not invoke a tool.
8. Stop all workers through the supervisor. Verify no residual worktrees,
   tmux/session hosts, sockets/listeners, or unexpected global files. Compare
   the pre/post snapshots. Only if every gate passes, write a ChezMoi-managed
   integration proposal; do not apply it in this trial.

### AO acceptance gates

- Codex and Claude Code run as already-authenticated installed CLIs, selected
  per worker, without rewriting their global configuration.
- All exposed endpoints are loopback/Unix-socket only, with an understandable
  local authorization model; no relay, remote access, or public listener.
- Closing UI and replacing the daemon produces the documented recovery result
  for each tested session type.
- Worktree creation, ownership, and deletion are inspectable and reversible.
- Status accuracy is sufficient for attention triage, with blocking states
  protected against automatic injection.
- Telemetry has an acceptable, explicit setting; otherwise AO is rejected for
  this private workflow.

If a gate fails, stop the AO trial and run the same four-session experiment in
Agent Manager. Preserve tmux-dev unchanged until that fallback proves it can
coexist or deliberately replace the relevant sessions.

## Sources

- **AO README**, Agent Orchestrator repository, accessed 2026-09-12. https://github.com/Untrivial-ai/agent-orchestrator
- **AO architecture**, Agent Orchestrator repository, accessed 2026-09-12. https://github.com/Untrivial-ai/agent-orchestrator/blob/main/docs/architecture.md
- **Agent Manager README**, accessed 2026-09-12. https://github.com/YoanWai/agent-manager
- **Agent Manager configuration**, accessed 2026-09-12. https://github.com/YoanWai/agent-manager/blob/main/docs/configuration.md
- **Herdr socket API**, accessed 2026-09-12. https://herdr.dev/docs/socket-api/
- **Herdr integrations**, accessed 2026-09-12. https://herdr.dev/docs/integrations/
- **Agent Deck README**, accessed 2026-09-12. https://github.com/asheshgoplani/agent-deck
- **Agent Deck skills documentation**, accessed 2026-09-12. https://github.com/asheshgoplani/agent-deck/blob/main/documentation/SKILLS.md
- **Agent Deck orchestration skill**, accessed 2026-09-12. https://github.com/asheshgoplani/agent-deck/blob/main/skills/agent-deck/SKILL.md
- **NTM README**, accessed 2026-09-12. https://github.com/Dicklesworthstone/ntm
- **NTM AGENTS**, accessed 2026-09-12. https://github.com/Dicklesworthstone/ntm/blob/main/AGENTS.md
- **Paseo README**, accessed 2026-09-12. https://github.com/getpaseo/paseo
- **Paseo troubleshooting**, accessed 2026-09-12. https://github.com/getpaseo/paseo/blob/main/public-docs/troubleshooting.md
- **Hunk README**, accessed 2026-09-12. https://github.com/modem-dev/hunk
- **Hunk CLI reference**, accessed 2026-09-12. https://github.com/modem-dev/hunk/blob/main/website/src/content/docs/docs/reference/cli.md
- **MCP Inspector CLI Client**, accessed 2026-09-12. https://github.com/modelcontextprotocol/inspector/blob/main/clients/cli/README.md
