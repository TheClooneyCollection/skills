---
subject: "fix(design-lab): refuse dotfiles and directory listings in serve-lab"
title: "Keep hidden files and directory listings out of the design lab"
---

- Return 404 for dot-prefixed request path segments and directories without index.html, while keeping visual files available without caching on loopback.
- Add offline HTTP tests and include them in release checks.
