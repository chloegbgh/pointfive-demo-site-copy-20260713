---
description: "How PointFive can unify prose docs and generated API reference."
icon: brackets-curly
---

# API reference model

This page shows where a generated reference could live next to hand-authored guides.

## Recommended source of truth

{% columns %}
{% column width="50%" %}
### GraphQL schema

Keep the current playground for exploration, but export schema documentation into GitBook so developers can search, ask AI questions, and review changes in pull requests.
{% endcolumn %}

{% column width="50%" %}
### OpenAPI wrapper

For REST-style automation and webhooks, generate OpenAPI from the gateway or maintain a slim OpenAPI spec in the docs repo.
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
The generated operation pages below are sample-only. They demonstrate the unified experience, not the final PointFive API contract.
{% endhint %}
