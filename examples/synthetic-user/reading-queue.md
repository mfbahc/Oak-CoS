# Synthetic Reading Queue

This example is synthetic. It shows the shape of a private review queue without real user data.

## Today

| Item | Source | Why read now | Status |
| --- | --- | --- | --- |
| Example Company Board Pack - Current.pdf | `workspace/artifacts/example-company/board-pack-current.pdf` | Needed before tomorrow's board meeting. | unread |
| Example Customer Contract Summary.docx | `workspace/artifacts/example-customer/contract-summary.docx` | Decision needed on commercial terms. | unread |

## This Week Or Can Wait

| Item | Source | Why it can wait | Status |
| --- | --- | --- | --- |
| Vendor Security FAQ.pdf | `workspace/artifacts/vendors/security-faq.pdf` | Useful background, not blocking a vote or decision. | unread |

## Stale Or Superseded

| Item | Replaced by | Action |
| --- | --- | --- |
| Example Company Board Pack - 2026-01-01.pdf | Example Company Board Pack - Current.pdf | Move out of `_to-read`; keep source artifact. |

## Notes

- The review folder should contain only the current unread items.
- Living files should use stable names such as `board-pack-current.pdf` with source and refresh time recorded here.
- Never delete source artifacts when moving items out of the active queue.
