# r28 — Copilot-in-Outlook workflow verification (retrieved 2026-09-16)

For exercise 4 (Summarize an email conversation). [REFRESH QUARTERLY.]

Verified against Microsoft's official support pages (support.microsoft.com):
- "Summarize an email thread with Copilot in Outlook" — a **Summary by Copilot /
  Summarize** control at the top of an open thread; the summary can include
  numbered citations that jump to the supporting message. (This is the native
  path the exercise's "cite the supporting message" requirement maps to.)
- "Draft an email message with Copilot in Outlook" — drafts are created in the
  compose box or via Chat; nothing is sent automatically (drafts stay drafts —
  matches the exercise's authority boundary).
- "Get email coaching with Copilot in Outlook" — a separate feedback feature on
  drafts (≥100 characters).
- Licensing dependency: the full Copilot-in-Outlook experience requires a paid
  Microsoft Copilot subscription on a work/school account; Microsoft documents a
  limited no-add-on Copilot Chat for eligible accounts. Feature names and
  entitlements churn — state as "depends on your organization's Copilot license
  and current Outlook version".

Teaching consequences (baked into the deck slide 42 notes + workbook tab 4):
1. Native path: open thread → Summary by Copilot → then run the reusable prompt
   in Copilot Chat scoped to the selected conversation, when chat over mail is
   available.
2. Fallback that always works: the supplied Packaging_Change_Thread.txt pasted
   into any approved assistant — the exercise is designed around this, so no
   participant needs private mail or a specific license.
3. Citation availability varies by surface; the prompt therefore says "cite the
   supporting message, or identify its sender and date if links are unavailable."

Sources (retrieved 2026-09-16):
- https://support.microsoft.com/en-us/office/summarize-an-email-thread-with-copilot-in-outlook-a79873f2-396b-46dc-b852-7fe5947ab640
- https://support.microsoft.com/en-us/outlook/copilot-pages/draft-an-email-message-with-copilot-in-outlook
- https://support.microsoft.com/en-us/office/get-email-coaching-with-copilot-in-outlook-91a3cd56-1586-4a31-85c7-2eb8cdb02405
- https://support.microsoft.com/en-us/outlook/frequently-asked-questions-about-copilot-in-outlook
