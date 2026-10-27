# Bicycle Lab team workspace

Job: help five students see the next learning task, understand handoffs, open Colab, and share task status. This is a coordination website; model training and prediction remain in the existing Colab/Streamlit workflow.

Visual direction: a calm teaching workspace informed by a bicycle route map. The signature is a seven-stop route showing real workflow phases and completion, with A/B training called out in task details. Avoid decorative dashboard statistics or fabricated student names.

Tokens: canvas #F3F6FA, ink #1E3047, blue #2C5FC6, muted #617084, green #236D5D, line #DCE4ED. White working surfaces, 8px spacing rhythm, restrained 10–18px corners. IBM Plex Sans Thai for reading; Manrope for Latin identity and compact numeric labels.

Desktop: quiet left navigation, top role filter, next task plus actual completion, route overview, ready tasks and five roles. Mobile: horizontal navigation and single-column work areas. Use real text, native controls and an accessible modal; respect reduced motion and preserve form text on save errors.

Shared state: Apps Script ScriptProperties, one property per task, guarded with ScriptLock and per-task expected revision. Initial read does not write or fabricate progress. Each task has status, short note, optional HTTPS evidence link, last updated role/time and revision. A role is a self-selected attribution/filter, not verified identity or a permission boundary. Deployment access controls who can reach the board.

Safety: no dataset uploads, model training, credentials, student IDs, external URL fetching or broad Drive permissions. User text renders through textContent. Workflow order, roles and suggested checkpoints are guidance only. Members can update any task in any order; notes and evidence links are optional. Progress counts the statuses the team entered and does not verify uploaded files. The hub stores notes/links, not project files; members save notebooks through Colab/GitHub directly.

Verification: backend checks cover shared state, stale writes, out-of-order task updates, validation and corrupt storage. Browser checks cover desktop/mobile, role/task filtering, modal controls, saving, evidence and error states. Test progress stays in local mock storage, separate from the real team board.
