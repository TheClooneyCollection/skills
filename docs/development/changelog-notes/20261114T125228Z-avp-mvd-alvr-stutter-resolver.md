---
subject: "feat(avp-mvd-alvr-stutter-resolver): add a Vision Pro MVD and ALVR stutter skill"
title: "Vision Pro MVD and ALVR stutter resolver"
---

- New `avp-mvd-alvr-stutter-resolver` skill: audits the Mac, router, wired path, subnets and the ALVR PC, and fixes AWDL channel hopping by locking the router to the AWDL social channel.
- The fix is verified at the radio level (a single-channel AWDL schedule); an ALVR retest is still pending.
