---
title: "Agent and Configuration Dashboard"
type: raw-research-report
tags: [research, agents, configuration, mcp, skills, chezmoi, dashboard]
origin: research-workflow
created: 2026-09-12
---

# Agent and Configuration Dashboard

## Conclusion

**Combine existing inspection tools with a small, read-only inventory and
comparison layer if a unified overview remains necessary.** The strongest
reason for custom work is connecting ChezMoi ownership, rendered targets,
installed files, and agent-specific configuration scope. A new MCP gateway or
configuration manager would introduce a different operating model.

The reviewed products cover substantial parts of the problem. CC Switch
combines cross-agent configuration management; VS Code and Cursor provide
native customization views; MCP Inspector examines individual servers;
ToolHive and MCPHub manage MCP infrastructure. None of the reviewed official
documentation establishes the complete combination of ChezMoi-aware drift,
cross-agent effective configuration, provenance, and strict secret exclusion.
This is a bounded finding about documented capabilities, not proof that no
other tool exists. [1–7](#sources)

For Christian's personal Mac, retain ChezMoi as the configuration owner.
Use native views for questions about what an agent recognizes, and ChezMoi
for target-versus-destination comparison within explicitly approved,
secret-free inputs. An optional collector should emit a sanitized snapshot
that an ordinary local viewer can display. Keep MCP Inspector as an on-demand
diagnostic, since connecting to a server is an active operation.

These are recommendations, not an accepted implementation decision. No
dashboard installation, live-configuration collection, credential resolution,
configuration change, or runtime connection is part of this report.

## Evidence

### Scope and confidence

The assessment concerns a personal macOS environment with ChezMoi-owned
configuration and multiple coding agents. Chip architecture, macOS version,
installed product versions, and actual runtime compatibility were not
validated. All external sources were retrieved on **2026-09-12**. Product
claims below describe retrieved upstream documentation; release observations
are identified separately.

The accepted [[_research/agent-config-dashboard/outline|research outline]] and
[[_research/agent-config-dashboard/query|research query]] define the scope.
The existing [[chezmoi-ai-configuration-architecture]] page supplies related
**unreviewed draft context**, especially the distinction between shared
templates, adapters, and runtime-preserving merges. Its architectural details
were not independently verified against private configuration.

The comparison separates documented facts from analysis. “Not established”
means that the reviewed sources do not demonstrate the capability; it must
not be interpreted as a tested absence. Privacy statements are documentation
assessments, not a source-code audit, penetration test, or offline test.

### Product comparison

| Tool or component | Documented coverage | Effective configuration and permissions | ChezMoi comparison | Assessment |
| --- | --- | --- | --- | --- |
| CC Switch | Claude Code/Desktop, Codex, Gemini, OpenCode, OpenClaw, Grok Build, Hermes; MCP, prompts, skills | Configuration management; comprehensive runtime policy resolution not established | No documented adapter | Closest broad manager; conflicting ownership model for this use. [1](https://github.com/farion1231/cc-switch) |
| VS Code Agent Customizations | Harness-scoped customizations, agents, instructions, skills, MCP and plugins | Native discovery and diagnostics; not a universal resolver | No documented adapter | Strong existing view for supported VS Code harnesses. [2](https://code.visualstudio.com/docs/agent-customization/overview) |
| Cursor Customize | Rules, skills, subagents, commands, hooks, plugins and MCP; user/team/workspace scope | Native Cursor view; full policy provenance not established | No documented adapter | Useful for Cursor's own configuration. [3](https://cursor.com/docs/customize-cursor) |
| Claude Code native views | Settings sources through `/status`; selected settings through `/config` | `/status` identifies loaded sources, not the origin of every key | No documented adapter | Useful runtime corroboration with an explicit provenance gap. [4](https://code.claude.com/docs/en/settings) |
| Codex app-server interface | Resolved on-disk config, skills, hooks, MCP status | Native APIs exist; on-disk resolution is not an arbitrary session snapshot | No documented adapter | Promising optional collector adapter. [5](https://learn.chatgpt.com/docs/app-server) |
| MCP Inspector | MCP server inspection through web, CLI and TUI | Server protocol view, not host-agent instruction or permission resolution | None documented | Focused diagnostic component. [6](https://github.com/modelcontextprotocol/inspector) |
| ToolHive | MCP runtime/UI, client discovery, skills, authorization and telemetry capabilities | Policies for its managed runtime; host-wide effective settings not established | None documented | Consider if runtime management becomes a requirement. [7](https://docs.stacklok.com/toolhive/) |
| MCPHub, samanhappy project | Self-hosted MCP routing, credentials, access controls, logs and health | Gateway view; host instruction and skill resolution not established | None documented | Useful gateway, substantial extra responsibility here. [8](https://github.com/samanhappy/mcphub) |
| Agent Studio extension | Workspace agents, skills and MCP editing; configuration packs | File-based management; comprehensive runtime resolution not established | None documented | Narrower candidate with coverage questions. [9](https://marketplace.visualstudio.com/items?itemName=AgentStudio.agent-studio) |
| MintMCP | Commercial gateways, audit logs and agent monitoring | Enterprise governance; local host-file inventory not established | None documented | Enterprise option, weak fit for a personal inventory. [10](https://www.mintmcp.com/pricing) |
| ChezMoi plus `jd` | Target/destination differences plus structural JSON/YAML comparison | Neither understands every agent's runtime semantics | Native ChezMoi commands supply the comparison basis | Best reusable components for a narrow collector. [11](https://www.chezmoi.io/reference/commands/diff/), [12](https://github.com/josephburnett/jd) |

### Local operation, privacy, licensing and maintenance

| Candidate | Local operation and data boundary | License or cost evidence | Maintenance implication |
| --- | --- | --- | --- |
| CC Switch | Native desktop; local database/backups; optional cloud sync and proxy functions. Strict sanitized export not established | MIT | Release `v3.20.3`, 2026-09-11; active changes do not establish compatibility. [1](https://github.com/farion1231/cc-switch), [23](https://github.com/farion1231/cc-switch/releases/tag/v3.20.3) |
| Native agent views | Local UI does not establish offline operation of all agent, marketplace or analysis features | Existing product/account terms; no separate dashboard price verified | Low added software burden, but support depends on installed agent and editor versions. [2](https://code.visualstudio.com/docs/agent-customization/overview), [3](https://cursor.com/docs/customize-cursor) |
| MCP Inspector | Local process; web backend uses authentication and loopback by default. Connecting can launch processes or contact remote servers | MIT | Release `2.6.0`, 2026-09-09; v2 differs from legacy v1. [6](https://github.com/modelcontextprotocol/inspector), [13](https://github.com/modelcontextprotocol/inspector/blob/main/clients/web/README.md), [24](https://github.com/modelcontextprotocol/inspector/releases/tag/2.6.0) |
| ToolHive | Local desktop/runtime; container and remote-service dependencies remain. Built-in secret storage uses encryption and OS keyring support | Core repository Apache-2.0; enterprise offering separate | Core `v0.49.0`, 2026-09-11; UI and core versions are distinct. [14](https://github.com/stacklok/toolhive), [15](https://docs.stacklok.com/toolhive/guides-ui/secrets-management), [25](https://github.com/stacklok/toolhive/releases/tag/v0.49.0) |
| MCPHub | Self-hosted service handling MCP connections, credentials and logs; no complete offline/redaction guarantee established | Apache-2.0 | Operator owns service updates, authentication, persistence and exposure. [8](https://github.com/samanhappy/mcphub) |
| Agent Studio | Workspace extension; registry downloads and whole-configuration export documented. Safe redaction not established | Listing says MIT | Release freshness not independently established; validate claimed paths and skill format. [9](https://marketplace.visualstudio.com/items?itemName=AgentStudio.agent-studio) |
| MintMCP | Hosted service with self-hosted options advertised; air-gapped operation and field-level redaction not established | Custom quote; no public numerical price on retrieved page | Procurement and deployment review needed; excessive overhead for this scope. [10](https://www.mintmcp.com/pricing) |
| ChezMoi and `jd` | Local CLI comparison; `jd` also documents a WebAssembly UI without network calls. Neither supplies automatic secret exclusion | Both MIT | `jd` release `v2.5.0`, 2026-02-23. Small components, but sanitization remains custom work. [12](https://github.com/josephburnett/jd), [22](https://www.chezmoi.io/license/), [26](https://github.com/josephburnett/jd/releases/tag/v2.5.0) |

Release dates were checked against the maintainers' GitHub release metadata.
They establish recent publication, not support quality, vulnerability status,
or an end-to-end test of the current main-branch documentation. No rankings
depend on stars, download counts, or unsupported numerical maturity scores.

### Findings that affect the choice

**CC Switch introduces another owner.** Its documented architecture uses
SQLite as its source of truth and synchronizes changes to live files. This
creates a second reconciliation path beside ChezMoi. Its reviewed support
list does not include Cursor or Copilot. The upstream repository identifies
`ccswitch.io` as its only official website; similarly named search results
should not be treated as authoritative. [1](https://github.com/farion1231/cc-switch)

**Native views already cover much of the visible inventory.** VS Code's
customization editor is scoped to the chosen harness. Its optional AI
evaluation feature uses Copilot, so invoking analysis is a separate data-flow
decision from browsing local files. Cursor's Customize page similarly groups
extensions by scope. Neither source establishes ChezMoi ownership or drift
tracking. [2](https://code.visualstudio.com/docs/agent-customization/overview),
[3](https://cursor.com/docs/customize-cursor)

**Copilot needs a surface identifier.** Copilot in VS Code and Copilot's cloud
agent do not share one undifferentiated configuration universe. GitHub's
custom-agent reference documents environment-specific behavior and processing
of repository MCP settings. A collector should identify `copilot-vscode`,
`copilot-cli`, and cloud configuration separately, marking uninspected cloud
state unknown. [16](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

**Codex offers useful native read APIs.** The app-server documentation defines
`config/read`, `skills/list`, `hooks/list`, and `mcpServerStatus/list`. The
configuration method resolves on-disk layers, while skill discovery can be
scoped by working directory. These can reduce duplicated parser logic in a
future adapter. They do not justify claiming that a newly launched server
represents an existing session's transient state. Nor does their availability
prove startup is side-effect-free. [5](https://learn.chatgpt.com/docs/app-server)

**Configuration resolution is agent-specific.** Codex documents command-line,
project, selected-profile, user, cloud-managed, system and default layers, with
project trust affecting loading and enforced requirements handled separately.
Claude documents its own scopes, list-merging behavior, managed settings and
session overrides. A generic JSON merge cannot reproduce both. Native
resolution should be preferred when it can be obtained safely; otherwise the
result must be labeled an estimate. [17](https://learn.chatgpt.com/docs/config-file/config-basic),
[4](https://code.claude.com/docs/en/settings)

**ToolHive solves a larger operational problem.** It discovers clients and
can automatically update their configuration as servers start, stop or are
removed. That behavior competes with ChezMoi ownership unless an explicit
boundary is designed. Encryption of ToolHive's own secrets does not establish
that a dashboard export omits all sensitive information. [18](https://docs.stacklok.com/toolhive/guides-ui/client-configuration),
[15](https://docs.stacklok.com/toolhive/guides-ui/secrets-management)

**MCP Inspector is an active diagnostic.** Its current web backend documents
token authentication, loopback binding and origin validation. It also
documents displaying raw OAuth tokens. A server inspector is therefore not a
sanitized configuration report. Keep authentication enabled and use it only
for deliberately selected servers; listing capabilities may still require
process startup or network access. [13](https://github.com/modelcontextprotocol/inspector/blob/main/clients/web/README.md)

**Agent Studio needs validation before reliance.** Its listing describes
workspace editing and exports that include complete agent and skill bodies
plus MCP configuration. It lists several MCP file locations, but does not
establish full coverage of Claude's native configuration locations. Those
claims warrant fixture testing rather than assuming the extension's active
indicator proves agent availability. [9](https://marketplace.visualstudio.com/items?itemName=AgentStudio.agent-studio)

### ChezMoi: which states must be compared?

ChezMoi documents three useful operations: `diff` compares intended target
state with destination state; `cat` emits target contents; `status` reports
both last-written-versus-actual and actual-versus-target differences. A Git
diff of the source repository answers a different question: what changed in
the source representation. [11](https://www.chezmoi.io/reference/commands/diff/),
[19](https://www.chezmoi.io/reference/commands/cat/),
[20](https://www.chezmoi.io/reference/commands/status/)

The following is a proposed analytical model, not a capability demonstrated
by any one dashboard:

| State | Meaning | Useful comparison |
| --- | --- | --- |
| Source | Tracked templates, shared data and adapter definitions | Git history: changed intent |
| Rendered target | What ChezMoi would produce for the selected environment | Target versus installed files: application drift |
| Installed destination | Current filesystem entries and sanitized settings | Destination versus observed agent state: loading differences |
| Agent observation | What a specified agent reports for a specified context | Observation versus expectation: visibility or policy discrepancy |

Source files and rendered files must not be compared as though they were the
same format. A template placeholder and its installed value are expected to
differ. Equally, an installed file can match the target while a project
override changes effective behavior. The dashboard should report both facts
without collapsing them into one green “in sync” badge.

The unreviewed local architecture note describes merges that preserve
runtime-added entries. **Conditional inference:** where rendering reads an
existing destination and retains its extra keys, a clean target/destination
diff cannot establish that every retained entry came from reviewed source.
Ownership classification must be separate from drift: source-owned,
runtime-preserved, explicitly external, or unknown.

ChezMoi's `pass` template function retrieves passwords through the `pass`
CLI. Its `output` function executes a command each time the template runs.
Consequently, a non-applying preview is not automatically a non-executing or
secret-free operation. Even status calculation may need target evaluation;
output containing only filenames does not by itself prove safe collection.
[21](https://www.chezmoi.io/reference/templates/pass-functions/pass/),
[27](https://www.chezmoi.io/reference/templates/functions/output/)

**Recommendation:** do not run a whole-home render and then try to redact its
output. Initially inspect only approved metadata and secret-free fixture
inputs. Treat any target whose dependency chain can resolve credentials,
execute arbitrary helpers, or include unaudited templates as
`not evaluated: unsafe render dependency`. A later sanitized projection must
have an explicit contract; replacing secret values can affect template
branches, so it cannot automatically claim exact rendered-state equivalence.

## Trade-offs and risks

### Build, adopt, or combine

| Approach | Benefit | Cost or limitation | Recommendation |
| --- | --- | --- | --- |
| Native views plus targeted ChezMoi inspection | Lowest extra maintenance; native semantics | Fragmented view; safe render boundaries still needed | Start here |
| Adopt CC Switch | Broad configuration UI | Additional writer/database; incomplete requested agent coverage | Only if configuration ownership changes deliberately |
| Adopt ToolHive or MCPHub | MCP runtime visibility and control | Runtime/service ownership, credentials, updates and client rewiring | Revisit for runtime requirements |
| Commission MintMCP | Enterprise governance and monitoring | Commercial terms and deployment overhead; local drift gap | Not justified by this personal scope |
| Small read-only collector plus existing viewer | Fits provenance, redaction and source/live question | Versioned adapters and careful secret handling | Best candidate if fragmented inspection remains costly |

This ranking is analysis against the accepted constraints. It does not rank
general product quality. A gateway can be the right choice for centralized
authorization and still be unnecessary for observing configuration files.

### Minimum useful collector

The following defines a possible future scope, not authorization to build it.
Begin with an on-demand command producing sanitized JSON and a short Markdown
summary. Use the same snapshot in a local viewer if needed. No persistent
database, background daemon, MCP proxy, configuration editor or model call is
necessary to demonstrate the core value.

Each record should carry:

- Agent and surface, scope, selected workspace alias and adapter version.
- Item type and reviewed identifier: skill, MCP registration, instruction
  source, hook, plugin or permission setting.
- Source reference, destination reference and ownership classification.
- Sanitized comparison result and the fields actually compared.
- Evidence level: declared, discovered, resolved on disk, or observed in a
  specified runtime; timestamp and freshness.
- Explicit unknowns, exclusions and parse failures.

For MCP entries, separate **registered**, **enabled**, **connected** and
**tools observed**. File parsing can establish registration; it cannot
establish connectivity. For skills, distinguish “folder exists,” “agent
discovers it,” and “loaded for this task.” Instruction files can influence
behavior without being enforceable permissions. A policy record should
identify both its source and the component that enforces it.

A valuable first screen would answer three questions: which agents share
each item, where to edit its source, and why its current status is known or
unknown. A field-level diff is useful only after those identities are clear.
Use stable identifiers scoped by agent and workspace; matching display names
alone can conflate unrelated skills or MCP registrations.

For comparisons, normalize object ordering but preserve list order unless
the adapter knows the field has set semantics. Keep disabled, absent, empty,
false, inaccessible and unknown distinct. `jd` provides structural comparison
and configurable array semantics, but selecting those semantics is the
collector's responsibility. Its local CLI is the smallest reusable viewer;
its web UI is optional. [12](https://github.com/josephburnett/jd)

### Explicit secret boundary

The acceptance criterion should be **allowlisted output**, not successful
masking of strings that resemble API keys. A recommended default boundary is:

| Input category | Allowed output | Excluded output or action |
| --- | --- | --- |
| Credentials, auth files, keychains, password stores | At most an explicitly reviewed opaque dependency label | Opening credential stores, retrieving values, hashes or lengths |
| Environment and HTTP headers | Reviewed variable/header names and configuration-presence flags | Values, resolution, credential validation |
| MCP commands and arguments | Reviewed executable/package identity and argument count | Raw command lines, inline scripts and arbitrary argument values |
| URLs | Reviewed service alias and transport class | User info, query, fragment and unapproved host/path details |
| Instructions, skills and hooks | Approved metadata, scope and location aliases | Full bodies, scripts or automatic execution |
| Errors and logs | Error codes and sanitized logical locations | Parser excerpts, raw stderr, request payloads and session transcripts |

Even names and paths can be sensitive; sanitize them against the report's
intended audience. A local-only report may allow more reviewed metadata than
a shareable export. Do not silently reuse the local view as the export view.

Files that mix configuration and secrets present a real trade-off. A parser
may read sensitive bytes into memory even when it emits only approved fields.
If the requirement is that secrets must never be read at all, exclude those
files until a separately produced, reviewed projection exists. If local
in-memory parsing is later accepted, it needs a separate design for bounded
reads, sanitized errors, no raw persistence, and fail-closed output.

Do not claim secret equality after replacing every value with one redaction
marker. Report `secret value not compared`. Hashing secrets is also outside
this design: it still requires reading them and exposes a persistent
fingerprint. Drift metrics must disclose their comparison coverage.

Avoid shell evaluation, template execution, arbitrary symlink traversal and
implicit MCP startup during collection. Bound allowed roots and file sizes;
do not recurse through the whole home directory. Version-specific native
introspection should be an optional adapter only after its startup and
network effects have been assessed.

A static local report avoids a listening service. If a live web viewer later
becomes necessary, its backend should expose only sanitized snapshots, bind
to loopback and enforce request-origin/authentication boundaries. Keep
telemetry, cloud sync, external assets and remote analysis out of the initial
design. These are proposed controls, not properties already verified in an
implementation.

### Maintenance and validation

The expensive part is preserving correct meaning as agents change their
configuration rules. Keep small adapters with a declared supported version
range and fixture examples. When a schema or precedence rule is unsupported,
show that limitation rather than silently approximating it. A broad
multi-agent “effective policy” engine should not be the first deliverable.

A future feasibility check can stay entirely within synthetic fixtures:

1. Represent one shared skill, one MCP entry and one permission in source and
   installed forms; include an intentional difference and a runtime-owned key.
2. Confirm source ownership and drift are reported independently.
3. Add fake secrets in headers, arguments, URLs, multiline strings and parser
   errors. Require zero appearances in output, logs, temporary files or UI.
4. Make secret/helper templates deliberately unevaluable. Require an explicit
   unknown result and no helper execution.
5. Exercise a project override, a missing file, an unsupported setting and a
   stale runtime observation. Require distinct states.
6. Confirm the collector changes neither source nor destination and initiates
   no network connection. Only then assess approved real metadata.

The initial manual comparison should take roughly 5–15 minutes once suitable
fixtures exist; building and hardening the collector is a separate estimate.
No delivery estimate is justified before the actual adapter and secret
boundaries are reviewed.

## Open questions

- Is the desired result a periodic inventory, drift check, or view of a
  particular running session? Each needs different evidence.
- Which Copilot surfaces and which project scopes must be covered initially?
- Does “exclude secrets” prohibit reading mixed files, or permit strictly
  local parsing with allowlisted output? The conservative starting point is
  to skip mixed files.
- Which ChezMoi targets can be evaluated without credential helpers or
  arbitrary commands, including their nested template dependencies?
- Which runtime-preserved configuration keys are intentionally outside
  ChezMoi's ownership?
- Can approved native read APIs operate without starting MCP servers,
  refreshing authentication, or making network requests in installed versions?
- Would native views plus a source map already answer most daily questions?
  If so, a custom dashboard is unnecessary.

No adoption or implementation decision is recorded as confirmed. Durable
acceptance belongs to subsequent human review and Wiki curation.

## Sources

All sources below were retrieved on **2026-09-12**. “Undated” means the
retrieved page did not establish a publication date; it does not imply that
the content is old. Repository main branches and live documentation can move
independently of the release versions listed here.

1. Farion1231 / CC Switch maintainers. [CC Switch README](https://github.com/farion1231/cc-switch). Undated, moving main branch. Coverage, architecture, storage, sync and MIT license.
2. Microsoft. [Create and manage agent customizations](https://code.visualstudio.com/docs/agent-customization/overview). Live documentation; search metadata dated 2026-09-09. Harness scope, native UI and optional AI evaluation.
3. Cursor. [Customize Cursor](https://cursor.com/docs/customize-cursor). Undated live documentation. Customization categories and scopes.
4. Anthropic. [Settings files and precedence](https://code.claude.com/docs/en/settings). Undated live documentation. Sources, `/status`, merging, overrides and limitations.
5. OpenAI. [Codex App Server](https://learn.chatgpt.com/docs/app-server). Undated live documentation; retrieved through the official developers.openai.com redirect. Native read methods and on-disk resolution.
6. Model Context Protocol maintainers. [MCP Inspector README](https://github.com/modelcontextprotocol/inspector). Undated, moving main branch. Clients, v2/v1 distinction and MIT license.
7. Stacklok. [ToolHive introduction](https://docs.stacklok.com/toolhive/), [Using ToolHive UI](https://docs.stacklok.com/toolhive/guides-ui/). UI page updated 2026-09-08. Runtime, UI, skills and enterprise distinction.
8. Samanhappy / MCPHub maintainers. [MCPHub README](https://github.com/samanhappy/mcphub). Undated, moving main branch. Gateway, credentials, logs, self-hosting and Apache-2.0 license.
9. AgentStudio publisher. [Agent Studio marketplace listing](https://marketplace.visualstudio.com/items?itemName=AgentStudio.agent-studio). Undated. Publisher-stated functionality, file locations, exports and MIT license; not independent validation.
10. MintMCP. [Pricing](https://www.mintmcp.com/pricing). Undated current commercial page. Quote-based pricing, monitoring and advertised self-hosted options.
11. ChezMoi maintainers. [`diff` command](https://www.chezmoi.io/reference/commands/diff/). Undated. Target/destination comparison and configurable external diff handling.
12. Joseph Burnett / jd maintainers. [JSON diff and patch](https://github.com/josephburnett/jd). Undated, moving main branch. CLI, structural comparison, local UI, array semantics and MIT license.
13. Model Context Protocol maintainers. [Inspector web-client README](https://github.com/modelcontextprotocol/inspector/blob/main/clients/web/README.md). Undated, moving main branch. Authentication, binding, origins and OAuth token display.
14. Stacklok. [ToolHive repository](https://github.com/stacklok/toolhive). Undated, moving main branch. Container runtime and Apache-2.0 license.
15. Stacklok. [Secrets management](https://docs.stacklok.com/toolhive/guides-ui/secrets-management). Undated live documentation. Built-in encrypted secrets and OS keyring.
16. GitHub. [Custom agents configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration). Undated live documentation. Environment differences and configuration processing.
17. OpenAI. [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic). Undated live documentation; retrieved through the official developers.openai.com redirect. Precedence, project trust and enforced requirements.
18. Stacklok. [Client configuration](https://docs.stacklok.com/toolhive/guides-ui/client-configuration). Undated live documentation. Discovery and automatic client-file updates.
19. ChezMoi maintainers. [`cat` command](https://www.chezmoi.io/reference/commands/cat/). Undated. Emission of target contents.
20. ChezMoi maintainers. [`status` command](https://www.chezmoi.io/reference/commands/status/). Undated. Last-written, actual and target comparisons.
21. ChezMoi maintainers. [`pass` template function](https://www.chezmoi.io/reference/templates/pass-functions/pass/). Undated. Credential retrieval during template evaluation.
22. Tom Payne / ChezMoi maintainers. [License](https://www.chezmoi.io/license/). MIT; copyright starts 2018.
23. CC Switch maintainers. [Release v3.20.3](https://github.com/farion1231/cc-switch/releases/tag/v3.20.3). Published 2026-09-11, verified through GitHub release metadata.
24. Model Context Protocol maintainers. [Inspector release 2.6.0](https://github.com/modelcontextprotocol/inspector/releases/tag/2.6.0). Published 2026-09-09, verified through GitHub release metadata.
25. Stacklok. [ToolHive release v0.49.0](https://github.com/stacklok/toolhive/releases/tag/v0.49.0). Published 2026-09-11, verified through GitHub release metadata; core release, not UI release.
26. Joseph Burnett. [jd release v2.5.0](https://github.com/josephburnett/jd/releases/tag/v2.5.0). Published 2026-02-23, verified through GitHub release metadata.
27. ChezMoi maintainers. [`output` template function](https://www.chezmoi.io/reference/templates/functions/output/). Undated. Command execution during template evaluation.
