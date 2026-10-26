# Resume research: April-October 2026

Prepared October 26, 2026. This note records the evidence behind the updated
resume and the broader work found during research.

## Scope and attribution

- Starting document: `archive/LukasJoseFerrer_Resume_April2026.pdf`, created April
  27. Earlier career facts and established impact metrics come from this
  user-supplied document; they were not independently remeasured.
- AutoIndex: reviewed history since April 1 and prioritized changes after April
  27. The checked-out branch was at September 23 (`fd78b2bd`); October research
  used local tracking refs `origin/main` (`0223ec75`, October 20) and `origin/dev`
  (`6ee4ba60`, October 22). A final `git ls-remote` check on October 26 confirmed
  these match the remote main/dev branch tips. Uncommitted work was left intact.
- Selected implementation commits are authored by `SQPferrer`. June foundation
  commits under `rust` and `chrome` share the user's company email identity.
  Author attribution was checked separately from team-owned infrastructure.
- WAR: reviewed public version 0.21.16 at
  [`dd8373325fafee2cc4626a83aa835c4870eb7b62`](https://github.com/Ljferrer/WorkAuditRefine/tree/dd8373325fafee2cc4626a83aa835c4870eb7b62)
  and local history for the project's origin.
- Current unit economics come from the user's dashboard screenshot. Only its
  aggregate figures are retained here.

## Activation below one cent per page

The supplied dashboard shows October 21-26, 2026 in its UTC view:

| Measure | Displayed value |
| --- | ---: |
| Page activations | 110.1K |
| Cases | 463 |
| AI pipeline cost per activation | $0.009628 |
| Chat cost per activation | $0.003115 |
| Combined cost per activation | $0.0127 |

The supported claim is **measured Activation AI pipeline cost below $0.01/page**,
excluding chat. This is a six-day observation, not a lifetime average or complete
infrastructure TCO study. The April resume's $0.0269/page uses broader wording;
its accounting scope has not been reconciled with the screenshot. No savings
percentage, annualized savings, or profit improvement is therefore asserted.

Source identifies Qwen 3.6 FP8 as `Qwen36` / `qwen-3.6-fp8`; **27B** is supplied
directly by Lukas. The August 18 plan calls the inference service
colleague-operated. Lukas's evidenced ownership is pipeline integration,
rollout, recovery, and fallback, rather than sole creation of the model server.

| Work | AutoIndex commit evidence |
| --- | --- |
| Detection/transcription and schema-constrained extraction integration | `0a77a928`, `7b295314` (Aug 18) |
| SQS completion consumer, DynamoDB results, alarms | `3229f773` (Aug 18) |
| Step Functions callback execution | `22b1b979` (Sep 3) |
| Production detect/transcribe, OmniExtraction, DescribeChunks, BulletSum rollout | `7e073a95`, `463e5f34`, `3fb59a05`, `e9e915ca` |
| RemapBullets, QuickPrev, Identifier, deduplication, CaseOverview expansion | `35f422f8`, `d34ba884`, `e80255f5`, `7b97caa9`, `67234e1c` |
| Durable pending-job recovery, quality retries, bounded paid fallback | `6f430de6` (Sep 8) |
| Outage/quality fallback metrics | `ef64536c` (Sep 8) |
| Corrected callback routing and verified actual serving route | `ec464269`, `fbbdfdf7` (Sep 14) |
| Durable result references and immutable snapshots | `748c1119`, `cd6701f8` (Sep 14) |
| One outcome per prompt per page | `0f0eca2a` (Oct 6) |

Source entry points:

- `auto_index/stacks/external_api/llm_queue/consumer.py`
- `auto_index/stacks/external_api/V2/prompt_runner/execute.py`
- `auto_index/stacks/case_prep/CasePrepV3/page/detect_transcribe_page.py`
- `auto_index/stacks/summary/AssistiveMetadataV2/page_extractions/run_all_page_extractions.py`
- `docs/audits/2026-09-14-assistive-qwen-routing.md`

Billing reconciliation includes estimated warm/cold Qwen token prices; local
inference is not simply counted as free. That pricing implementation belongs to
another contributor (`8a9906a`) and is not claimed as Lukas's work. Paid API
fallback remains. Final native Record Summary has its Qwen lane off in the
October production configuration; not every stage runs on Qwen.

## Other new AutoIndex accomplishments

| Accomplishment | Evidence and scope |
| --- | --- |
| Fargate and ARM64 modernization | Foundation `1fef2050`; summary steps `2a159165`, `fc6a5e9e`; page processing `d71acc46`, `2d3efde1`; production Spot gates `9d8b3aa7`; ARM64 gates `89655e42`, `53910edc`. Seven compute steps, with Spot/on-demand recovery for the two bulk page steps. No overall savings percentage asserted. |
| Hybrid GPU serving | `3c9f6959`, `84c01596`, `803ef897`, `99fce8f1`; production cutover `44dc6b6b` (Aug 25); backlog-driven cloud fallback `8c578af2` and worker-pool separation `89c55492` (Sep 28). This is RecSeg serving, distinct from the Qwen server. |
| Python-native record summaries | Native chain `b9a264aa`; pgvector readers `852f2f57`; routing `4fbc62cf`; transactional writers/parity artifacts `a27dd380`, `d4728f0b`; production switch `2a7b0e3c` (Oct 16); recovery/fencing `6b4df9d3`, `6a32366e`, `bf7f3d7b`. |
| Translation evaluation | New May pipeline: `f4d30f27`, `b796e0cc`, `a3382dd2`, `c52e46f1`, `41246aef`, `6129536a`, `64151163`, `505514e4`, `cbf603a0`. OpenWHO, WMT Biomedical, FLORES; COMET/COMETKiwi, classical metrics, GEMBA scoring, degraded scans, bootstrap intervals, clinical-error reporting. Clinical thresholds await calibration; no safety guarantee is claimed. |
| Extraction and deduplication evaluations | Extensions to the existing extraction suite: `f484dd5a`, `aedd48bc`, `93dc3fc7`, `dfd90e9d`. Paired/blinded dedup replay: `19272c99`, `1e194284`, `8b0c7285`. The extraction suite itself predates April. |
| Preserve human edits on reruns | Synchronous/bounded writers `9a2ab720`, `3b1ea708`; database-authoritative reconciliation `7fab3511`, `c3fa0beb`, `ddfe177d`; invalidation `e4aeffcd` (Sep 7-8). Synthetic fixture timings were not presented as production throughput. |

Source entry points, relative to AutoIndex (October content read at `origin/main`):

- `auto_index/configs/assistive_summary_config.json` and
  `auto_index/configs/case_prep_config.json`: production compute and rollout settings.
- `auto_index/stacks/summary/RecordSummaryV3/README.md`: native chain, retrieval,
  transactional writes, shadow comparison, fallback, and hierarchical reduction.
- `auto_index/stacks/record_segmentation/README.md`: local/cloud serving.
- `tools/PageTranslation/pagetranslation/`: evaluation implementation and reports.
- `tools/ExtractionTestSuite/evaluation/statistics.py` and
  `tools/DedupModelEval/README.md`: paired evaluation and statistics.
- `docs/reference/2026-09-08-db-authoritative-record-reruns.md`: persistence rules.

## Additional work found by month

- **Late April:** identifier tool calling and silent-cache repair (`d0439803`,
  `79f49005`).
- **May:** translation benchmark ingestion, test-document rendering, pipeline-output
  joins, scoring, and reporting.
- **June:** task-token ECS execution for long-running case summaries; parallel S3
  consolidation and checkpoint-compatible retries (`6b160f91`, `681a3c80`) for
  workloads hitting Lambda's duration limit.
- **July:** duplicate-record grouping (`1a3fd2ca`, `10c19b3b`), extraction
  normalization (`1fa35fb4`), citation shape handling (`c798fb6c`), strict content
  checks (`efedeadd`), bounded oversized-record processing (`18ac20b2`, `81dcbd39`).
  General citation validation was already in the April baseline.
- **August:** Qwen adoption, hybrid GPU serving, ECS page compute, handwritten-date
  detection (`bc69f945`, `8814567f`, `809421fb`, `0f658fb9`; production `547b928d`),
  bounded CaseOverview catch-back loops (`7eebf6f0`).
- **September:** record-split audit integration (`2eb09010`, `639bd956`), human-edit
  preservation, orientation/handwriting fixes (`72f148f8`, `7db363ec`), concurrent
  run/restart handling (`c829f640`, `65318c5d`, `234bdc9e`, `ae77de43`), weighted
  progress (`3b1aa149`), large-record summaries with page provenance and hierarchical
  reduction (`231a9bbd`, `08da3116`, `15cae812`).
- **October:** production large-record v2 (`86e40106`), native summaries, monitoring
  stack separation (`d52d3818`), removal of inert invocation settings (`7242aca4`),
  infrastructure resource budgets (`3274ce49`, `75e43983`), prompt-rejection alarms
  and delivery recovery (`71ae166e`, `bab94099`, `6bdadb2c`).

## WAR: Work Audit Refine

Creator-owned project begun June 18, 2026 (initial commits `3401ff7d`, `d187eaf9`).
The resume features its shipped Claude Code workflow.

- [README](https://github.com/Ljferrer/WorkAuditRefine#what-it-does) and
  [workflow engine](https://github.com/Ljferrer/WorkAuditRefine/blob/dd8373325fafee2cc4626a83aa835c4870eb7b62/skills/war/assets/workflow-template.js):
  task DAGs, parallel workers in isolated Git worktrees, 1-5 auditor seats,
  commit-pinned verdicts, severity blocking, serial integration and test/lint gates.
- [Auditor guard](https://github.com/Ljferrer/WorkAuditRefine/blob/dd8373325fafee2cc4626a83aa835c4870eb7b62/hooks/validate-auditor-git.sh):
  read-only command restrictions for auditor agents.
- [Memory implementation](https://github.com/Ljferrer/WorkAuditRefine/blob/dd8373325fafee2cc4626a83aa835c4870eb7b62/skills/_shared/war-memory.mjs):
  persistent engineering records searched through an in-memory SQLite FTS5 index,
  BM25 retrieval, and provenance ranking.
- [Recovery design](https://github.com/Ljferrer/WorkAuditRefine/blob/dd8373325fafee2cc4626a83aa835c4870eb7b62/docs/adr/0008-git-is-the-resume-source-of-truth.md):
  interrupted-run reconciliation against Git. Some checks are agent instructions,
  not formal guarantees.
- [Demo](https://youtu.be/6LXrfWtKSlg?si=guy4gEUdLSzJRNSj): YouTube metadata identifies
  Lukas Ferrer as creator and the title as "What If AI Agents Could Audit Their
  Own Code? - WAR on Claude." Metadata and README linkage were verified; video
  contents were not independently reviewed.
- [LinkedIn](https://www.linkedin.com/in/lukasferrer/) is the exact user-provided
  destination. Retrieval returned HTTP 999; no profile facts were inferred.

No unsupported productivity multiplier, adoption claim, or production Codex
execution parity is asserted. Public documentation describes the Codex port as
work in progress.

## Editorial choices

- Two pages: WAR and recent Sequoia work on page one; earlier impact, prior roles,
  skills, and education on page two.
- Established Sequoia metrics remain separate from newly researched results.
- Earlier roles and degrees are retained. Departure commentary and claims of a
  uniquely possible technical remedy were removed.
- All three requested QR codes also have clickable PDF links. Main text is
  selectable; QR graphics are vectors.
- The April document is preserved byte-for-byte. `src.tex` remains historical;
  `generate_resume.py` is the current editable source.

## Delivery validation

The final PDF has two US Letter pages and selectable text. Both pages were
rendered and visually inspected. All three QR codes were decoded from a 300-DPI
render to the exact requested destinations, and their PDF link annotations were
checked. The root and dated PDFs are identical; the archived April PDF matches
the supplied original byte-for-byte.
