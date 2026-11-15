---
subject: "feat(design-lab): make Tailscale optional, review locally without it"
title: "Review design labs locally without Tailscale"
---

- Use the loopback URL on the same machine, or optionally share over a tailnet for phone review.
- Keep the server on 127.0.0.1; public tunnels and binding to 0.0.0.0 are excluded from the workflow.
