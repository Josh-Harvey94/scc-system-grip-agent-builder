# SCC System Grip Agent

Build a reusable operational grip assistant in **Microsoft 365 Copilot Agent Builder**. Copy the configuration, connect your organisation's approved sources, test it, then share it with authorised colleagues.

> An SCC-focused Copilot agent that turns emails, Teams chats, meetings, data and documents into clear operational grip by summarising risks, actions, owners, deadlines, unresolved issues, handovers and politically careful follow-up.

**[Start the build guide](BUILD_GUIDE.md)** · **[Get the interactive companion](SCC_System_Grip_Agent_Build_Companion.html)** · **[Copy the exact instructions](agent/instructions.txt)** · **[Run the acceptance tests](tests/ACCEPTANCE_TESTS.md)**

Download this repository using **Code → Download ZIP**, extract it and open `SCC_System_Grip_Agent_Build_Companion.html` in a browser. It works offline, has copy buttons, saved checklists, starter prompts, testing and daily runbooks. GitHub's file viewer displays HTML source; download it to use the interactive version.

## Start here

1. Open Microsoft 365 Copilot with your work account. Select **New agent → Skip to configure**.
2. Copy [name.txt](agent/name.txt), [description.txt](agent/description.txt) and [instructions.txt](agent/instructions.txt) into the corresponding fields.
3. Add your **Daily Operational Snapshot library** and approved narrative sources. Pasting instructions does not connect a library, mailbox or Teams chat.
4. Add the [starter prompts](agent/starter-prompts.json). Use a separate test agent and the [synthetic examples](examples/README.md) to work through the acceptance tests.
5. Record the [release decision](templates/release-record.txt), then share within your organisation and check each recipient's source access.

This is a manual configuration kit for Microsoft 365 Copilot Agent Builder. It does not require programming, a GitHub Copilot subscription, an OpenAI API key or a Copilot Studio project. Microsoft 365 entitlement, tenant settings and approved source access are still required. The repository is public; each organisation's agent and operational information remain in its own environment.

## What it produces

| Task | Result |
| --- | --- |
| Morning start of play | Dated headline position, operational read, first-touchpoint asks, grip gaps and a draft partner message |
| Meeting preparation | Source position, unresolved commitments, partner updates and assurance questions |
| Meeting summary | Decisions, full action table, discussion not converted into action and follow-up questions |
| Action review | Missing owners/times, overdue or repeated actions, dependencies and closure gaps |
| Close-of-play or on-call handover | Dated position, risks, partner updates, actions, watch points and short email summary |
| Follow-up communication | Calm, constructive requests for evidence, ownership and timescales |

The Daily Operational Snapshot library is the sole numerical authority. Narrative sources provide context. The agent distinguishes facts, interpretation and missing information, keeps discrepancies visible, and supports SCC/ICB assurance while providers retain operational delivery.

## Contents

| Location | Use |
| --- | --- |
| [BUILD_GUIDE.md](BUILD_GUIDE.md) | Nine build stages, source configuration, operating method and troubleshooting |
| [agent/](agent/) | Exact name, description and instructions, plus suggested starter prompts |
| [SCC_System_Grip_Agent_Build_Companion.html](SCC_System_Grip_Agent_Build_Companion.html) | Updated standalone interactive guide using the exact configuration |
| [templates/](templates/) | Source register, data dictionary, output structures, ownership and release records |
| [examples/](examples/) | Fictional dated snapshots and meeting evidence for a separate test agent |
| [tests/ACCEPTANCE_TESTS.md](tests/ACCEPTANCE_TESTS.md) | Human-run behavioural checks and expected results |
| [reference/](reference/) | Supplied historical PDF and HTML, explicitly superseded for configuration |
| [assets/branding/](assets/branding/README.md) | Josh Harvey logo, monograms, watermark, creator badge and agent icon |
| [validate.py](validate.py) | Optional local checks for canonical text, HTML parity, field limits and links |

## Exact configuration and adaptation

The three `agent/*.txt` configuration files preserve the owner's supplied wording, including the Cornwall & Isles of Scilly morning header, with the owner's requested generic source naming: **Daily Operational Snapshot library** and **operational snapshot**. The instructions are **7,199 characters**, excluding the final file newline, against Microsoft's documented **8,000-character** limit. The name is 21 characters and the description is 231.

For another system, fork the repository, explicitly change the geography and source names in your copy, and repeat the tests. Your data owner must nominate the local quantitative authority and map it to Daily Operational Snapshot library; do not connect unrelated datasets without documenting their meaning. Record local adaptations rather than describing them as the exact original.

The earlier PDF and HTML contain a different 5,478-character instruction set. They remain in `reference/` for provenance. **Use `agent/instructions.txt` and the root HTML companion for new builds.** See [CHANGELOG.md](CHANGELOG.md).

## Operating boundary

People run and validate the SQL extracts, save them into SharePoint, initiate the agent, review the outputs and circulate approved material. This kit does not run SQL, monitor continuously, update trackers, send messages or confirm the live operational feed. SQL scripts, tenant connections and live organisational records are not included.

Treat outputs as drafts for a responsible operational reviewer. The tests in this repository have not been run in your Microsoft 365 tenant and publication is not evidence of clinical, operational or information-governance approval. The companion records your checklist choices; its readiness indicator is not an automated safety assessment.

## Microsoft documentation

Setup references checked **12 September 2026**: [Build and configure](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents), [knowledge and permissions](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge), [overview and limitations](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder). Labels and availability can vary by tenant. The build guide notes an inconsistency between Microsoft's published knowledge-source limits, so follow the current controls in your tenant.

## Reuse

Created from Joshua Harvey's SCC System Grip Agent configuration and supplied build materials. Released under the [MIT licence](LICENSE) so others can use and adapt the kit. No NHS or Microsoft endorsement, trademark permission, operational data access or service entitlement is granted. See [CONTRIBUTING.md](CONTRIBUTING.md) for changes and [SECURITY.md](SECURITY.md) for handling sensitive reports.

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](assets/branding/a-jh-agent-badge.svg)](assets/branding/README.md)
