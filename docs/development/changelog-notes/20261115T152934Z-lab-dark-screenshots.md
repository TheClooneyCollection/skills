---
subject: "fix(design-lab): take dark screenshots with preferredColorScheme=0"
title: "Dark design-lab screenshots no longer depend on the Mac's appearance"
---

- Use `--blink-settings=preferredColorScheme=0` for dark and `=1` for light screenshots; `--force-dark-mode` never switched `prefers-color-scheme` and only looked right on a Mac in Dark mode.
