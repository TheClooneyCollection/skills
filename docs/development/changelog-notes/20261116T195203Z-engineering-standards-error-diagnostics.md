---
subject: "feat(engineering-standards): retain diagnostics at error boundaries"
title: "Keep error diagnostics and cancellation intent"
---

- Typed error boundaries retain necessary diagnostics through optional boundary logging or error metadata.
- Intentional cancellation is lifecycle control rather than a request failure requiring user action; no universal cancellation case or logging implementation is prescribed.
