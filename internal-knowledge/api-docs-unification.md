---
description: "How to bring GraphQL playground docs and narrative guides into one experience."
icon: diagram-project
---

# API docs unification

PointFive currently handles API docs separately through a GraphQL playground. GitBook can sit above that surface as the unified developer experience.

## Recommended model

- Keep GraphQL playground for live exploration.
- Generate schema docs into GitBook on every tagged release.
- Write narrative guides for common workflows: authentication, querying findings, webhooks, and remediation review.
- Link every guide to the exact generated operation or schema field it depends on.

{% hint style="info" %}
This is not a blocker for the demo. The site can start with narrative developer docs and add generated schema reference once PointFive shares the source schema.
{% endhint %}
