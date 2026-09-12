# Build and operate the SCC System Grip Agent

This guide uses the owner-supplied configuration with the requested generic source naming in `agent/`. It carries forward the nine-stage build, source preparation, tests and operating runbooks from the supplied handbook and interactive companion. The older copy kit is superseded.

## 1. Confirm fit, access and ownership

- Use a work account with Agent Builder available in Microsoft 365 Copilot. If **New agent** is missing, ask your Microsoft 365 administrator to check entitlement and tenant policy.
- Name an agent owner, deputy, operational reviewer and data owner using [ownership-and-change-log.txt](templates/ownership-and-change-log.txt).
- Agree the permitted source content, intended users and operating process. Keep patient-identifiable material out of the knowledge set.
- Confirm that a person will prepare the data and initiate each conversation. This implementation is for briefings and reviewed drafts. Automation needs separate design.

## 2. Prepare the source area

Use your approved SCC SharePoint site. The recommended layout is:

```text
Daily Operational Snapshot library/   ← quantitative authority only
  Current/                      ← newest approved extracts
  History/                      ← dated comparisons, agreed retention
SCC Narrative Knowledge/
  Meeting Transcripts/
  Actions/
  Templates/
  Reference/                    ← dictionary + source guide
SCC Agent Management/           ← outside production knowledge
  Ownership and Change Log/
  Test Records and Answer Keys/
```

Existing controlled libraries can be used without renaming them. Record how each configured source maps to the instruction term **Daily Operational Snapshot library**. Do not rename files that feed other processes without checking the impact.

Populate the [source register](templates/source-register.txt) and [data dictionary](templates/data-dictionary.txt). Identify numerical authority, refresh time, timezone, null meaning, owner, access and known limitations. Select narrow evidence folders; avoid adding a parent site that also contains answer keys or obsolete instructions.

## 3. Prepare the daily operational evidence

The original SCC process runs three approved SQL scripts each morning. Your organisation must supply and approve its own queries and schemas; this repository does not invent them.

1. Confirm the correct server, database and reporting period, then run the approved scripts.
2. Check dates, extraction times, expected columns, row count, completeness and absence of patient-identifiable information.
3. Preserve dated source exports. Do not silently replace missing figures, overwrite comparison evidence or make incomplete files look complete.
4. Provide a readable, supported knowledge representation. Prefer a simple `.xlsx` workbook with one clear sheet or a controlled `.txt` snapshot that preserves the original values and provenance. CSV is an export/interchange format, but is not listed in Microsoft's current Agent Builder knowledge file-type table; verify support before relying on it as knowledge.
5. Use a name such as `Operational_Daily_Snapshot_20260912_0730.xlsx`. Include date, extraction time, timezone and individual metric times inside the file too. A filename alone does not prove freshness.
6. Upload to the approved library, reopen the SharePoint copy, and check file readiness and retrieval in Copilot before briefing. Record delayed or missing extracts.

Do not mix the fictional test files with operational snapshots. The `.txt` examples are a teaching schema, not a specification of the actual operational data database.

## 4. Create the agent using the exact configuration

1. Open Microsoft 365 Copilot on desktop or web and select **New agent**.
2. Select **Skip to configure**, or open **Configure** if you have already used Describe.
3. Set **Name** to [name.txt](agent/name.txt): `SCC System Grip Agent`.
4. Set **Description** to the full text in [description.txt](agent/description.txt).
5. Paste the whole of [instructions.txt](agent/instructions.txt) into **Instructions**. Copy the contents only, without Markdown fences or a filename. The root HTML companion has a copy button.
6. Confirm the final rule is still present at the end. Check that the UI has not truncated or rewritten the text.
7. Configure capabilities only where the workflow needs them. Image generation is unnecessary for this build. If you enable document/chart/code tools, include them in local testing.

Where the agent icon control is available, upload [jh-agent-icon.png](assets/branding/jh-agent-icon.png). Keep the exact name, description and instructions unchanged. The small JH mark identifies the creator of the build kit.

The supplied configuration fits the documented 30-character name, 1,000-character description and 8,000-character instruction fields. Re-check the limits if your interface differs. [Microsoft configuration reference](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents).

**There is no one-click GitHub import into Agent Builder in this kit.** The JSON starter file is a convenient list for copying, not a Microsoft deployment manifest.

## 5. Connect knowledge deliberately

In **Configure → Knowledge**, add the actual approved sources. Source names in an instruction cannot grant access or establish a connection.

| Source | Configure | Check |
| --- | --- | --- |
| Daily Operational Snapshot library | Select controlled current and comparison evidence in SharePoint | Only this source supplies operational figures and OPEL |
| Transcripts, notes, actions, templates | Add approved narrative folders/files | Dates, scope and action provenance are visible |
| Teams | Add approved specific chats/meetings, or the broader option only if justified | Scope and results vary by the user's access |
| Outlook | Select **My emails** if approved and available | Current documentation says email cannot be scoped; sharing does not expose the creator's mailbox to recipients |

A SharePoint-only pilot is an optional way to establish a repeatable baseline. It is a staged implementation choice, not a replacement of the actual agent's Outlook/Teams narrative design. If those sources are unavailable, document the limitation and use approved saved transcripts/notes where appropriate.

Turn off **Search all websites** for operational evidence. Where available, **Only use specified sources** gives priority to configured knowledge but cannot completely block general model knowledge. Keep source checks and human review. Do not assume prompt instructions are a security boundary.

Referenced SharePoint content uses existing permissions. **Embedded uploads have different sharing behaviour:** users with agent access may receive answers grounded in those files. Prefer referenced controlled sources for operational knowledge and test recipient access. Personal Teams and email knowledge require the relevant Microsoft 365 Copilot entitlement. Do not assume **My emails** includes an SCC shared mailbox; validate that route explicitly or use approved saved narrative evidence.

Microsoft's configuration page currently mentions 20 knowledge sources, while the detailed knowledge page lists source-specific allowances, including up to 100 SharePoint items. Do not design around a maximum: use a small scoped set and confirm the limit shown in your tenant. [Microsoft knowledge reference](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge).

## 6. Add starter prompts

Open [starter-prompts.json](agent/starter-prompts.json), or the companion's Prompt Kit, and copy each title and prompt into **Starter Prompts**. The core six cover morning, meeting preparation, meeting summary, actions, handover and claim checking. A follow-up email prompt is supplied as an optional seventh.

The morning prompt invokes the exact A–G format: correct Cornwall & Isles of Scilly header, separate position/preparation times, headline evidence, operational read, asks, gaps, message and final source note. The meeting prompt uses all eight action columns from the actual instructions.

## 7. Test with separate evidence

Create a separate test copy of the agent and a test source location. Use [examples/README.md](examples/README.md) and [ACCEPTANCE_TESTS.md](tests/ACCEPTANCE_TESTS.md). Keep the expected answers and test register outside the test agent's knowledge too.

Use **Try it** for initial checks, then run recipient tests with the published pilot. Start a fresh conversation for each case. Retain the prompt, output, cited source, reviewer and result in an approved internal record. No scenario is marked passed merely because it appears in this repository.

Test stale, missing, conflicting and inaccessible sources; unsupported trends, OPEL forecasts and invented owners; patient identifiers; layout fidelity and provider/SCC boundaries. Include individual metric times and the difference between snapshot time and preparation time.

## 8. Release and share

Complete the [release record](templates/release-record.txt). Record the exact configuration version, sources, enabled capabilities, reviewer and unresolved limitations. Create/share the agent with a small authorised group, then check each representative user's agent entitlement and source retrieval. Check both allowed and disallowed access cases.

Give users the operating rule: **prepare evidence → initiate → verify → approve → circulate**. The current Agent Builder overview lists restrictions on use in Teams Chat; validate the actual supported experience in your tenant rather than equating Teams knowledge with Teams deployment. [Microsoft overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder).

Publishing this GitHub kit is separate from releasing an operational agent inside Microsoft 365.

## 9. Run and improve

### Morning

1. Run and check the approved SQL outputs; save and reopen the SharePoint evidence.
2. Confirm current snapshot, narrative and action updates are accessible.
3. Open a new conversation and use the morning starter. Supply the first-touchpoint deadline where known.
4. Check the header, position/prepared times, headline figures and individual metric dates.
5. Verify discrepancies, overdue actions, missing ownership and the prioritised assurance questions.
6. Confirm the suggested message says the snapshot date/time and does not imply a live feed. Edit and approve before circulation.

### After a meeting

1. Confirm the transcript is complete, appropriate to retain, and saved with meeting name/date/time.
2. Ask for the summary; verify the correct transcript was used.
3. Check decisions and all action columns. Preserve missing owners/deadlines rather than guessing.
4. Transfer confirmed actions to the tracker through your normal human process. Review any follow-up email before sending.

### Close of play / on call

1. Confirm the newest quantitative evidence and today's action/narrative updates.
2. Generate the handover, retaining position time, risks, watch points, follow-up and executive awareness.
3. Verify figures, actions and role boundaries; approve the handover and short email summary for continuity.

### Review cycle

Log retrieval failures, false claims, poor wording and user-permission differences. Re-test after material source, instruction or capability changes. Review whether the manual process still meets the team's needs; design automation separately if required.

## Troubleshooting

| Symptom | Next check |
| --- | --- |
| Agent cannot find a newly uploaded snapshot | Reopen the SharePoint file, check knowledge readiness, exact source scope and user permissions; do not label an old file current |
| Users get different context | Compare their SharePoint access and personal Teams/Outlook sources; record expected variation |
| CSV cannot be added | Preserve the source export and create a validated supported representation with dates, units and nulls retained |
| Morning output is a generic summary | Re-paste the canonical instructions, check the A–G section, use the current morning starter and begin a fresh conversation |
| Conflicting figures | Retain both dated claims, with operational data as numerical authority, and seek clarification; do not invent a reconciliation |
| Too few real asks to fill the layout | Keep the output evidence-based; the exact instructions allow empty sections or explicit absence |
| Browser blocks saved progress/copying | Companion still displays the kit; copy manually and retain approved test records elsewhere |

## Companion privacy

The companion has no backend or telemetry. It stores checklist choices locally in your browser where storage is available. Avoid operational or personal information in shared-device exports. Its release signal is a record of manual selections and does not validate the agent's behaviour.

<!-- JH creator signature -->

---

[![A JH Agent — Designed & built by Josh Harvey](assets/branding/a-jh-agent-badge.svg)](assets/branding/README.md)
