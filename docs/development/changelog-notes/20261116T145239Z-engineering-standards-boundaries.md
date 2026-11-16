---
subject: "feat(engineering-standards): clarify boundary payloads and semantic grouping"
title: "Give boundary values and code groups clear meaning"
---

- Choose request encoding without mechanically duplicating domain types; a format-shaped wire value is an optional, deliberate choice.
- Name cohesive boundary payloads and group properties, methods and function stages by responsibility, with Swift ordering guidance.
- Verify final wire output, including explicit null, rather than internal conversion steps.
