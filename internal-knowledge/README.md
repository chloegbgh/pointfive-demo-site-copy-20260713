---
description: "Internal docs operating model for PMs, CSMs, and engineers."
icon: users-gear
cover: "https://raw.githubusercontent.com/gitbook-demo-sites/pointfive-demo-site-20260713/main/assets/pointfive-docs-automation.svg"
coverY: 0
layout:
  width: wide
  cover:
    visible: true
    size: hero
---

# Internal Knowledge

This internal view demonstrates how PointFive's PMs, CSMs, and engineers can collaborate on docs without exposing draft or internal-only content to customers.

{% if visitor.claims.unsigned.persona === "internal" %}
{% hint style="success" icon="user-check" %}
You are viewing the internal contributor path. This view highlights docs automation, human review, segmented access, and internal knowledge management.
{% endhint %}
{% endif %}

## Contributor roles

| Team | Role in docs |
| --- | --- |
| Product managers | Own product narrative, release notes, and customer-facing workflows. |
| CSMs | Flag unclear customer journeys and contribute troubleshooting patterns. |
| Engineers | Tag the docs agent in pull requests and review technical accuracy. |

{% hint style="info" %}
This space is intentionally separate from the external developer docs. In a production setup, visitor authentication can make this visible only to internal teammates.
{% endhint %}
