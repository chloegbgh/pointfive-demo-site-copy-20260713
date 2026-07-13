---
description: "How internal reviewers approve AI-assisted documentation changes."
icon: user-check
---

# Human review process

AI can draft updates, but the publishing decision should stay with a human reviewer.

{% stepper %}
{% step %}
## Agent drafts the change

The docs agent reads the pull request, identifies affected docs, and opens a draft update.
{% endstep %}

{% step %}
## Reviewer checks accuracy

PMs review product language. Engineers review endpoint behavior, payloads, and operational caveats.
{% endstep %}

{% step %}
## GitBook publishes after approval

Approved changes merge through Git and sync into GitBook.
{% endstep %}
{% endstepper %}
