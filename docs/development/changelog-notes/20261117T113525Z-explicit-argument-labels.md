---
subject: "feat(engineering-standards): require explicit argument labels"
title: "Explicit argument labels with clear call-site meaning"
---

- Engineering standards now require explicit external labels for every function and initializer parameter, including the first, with names that reveal domain meaning at calls.
- Required external signatures remain intact; Swift closure inputs use named boundary payloads when positional arguments hide their roles.
