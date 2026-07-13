---
description: "A tailored GitBook demo for PointFive's developer and internal documentation workflows."
icon: house
cover: "https://raw.githubusercontent.com/gitbook-demo-sites/pointfive-demo-site-20260713/main/assets/pointfive-cover.svg"
coverY: 0
layout:
  width: wide
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: false
---

# PointFive Docs Hub

A clean product-style docs experience for external developers, with an internal contributor view for product, CSM, and engineering teams.

The demo centers on the developer path Chloe requested: authenticate, make API requests, subscribe to webhooks, and troubleshoot errors. It also shows how PointFive could separate public customer-facing docs from internal knowledge and review workflows while keeping both surfaces in one GitBook site.

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><h3><i class="fa-code" style="color:$primary;"></i></h3></td><td><strong>External developer view</strong></td><td>API setup, requests, webhooks, troubleshooting, and integration patterns for customers.</td><td><a href="https://app.gitbook.com/s/M1iVnZAxYcYAd8w4aIU9/">External developer view</a></td></tr>
<tr><td><h3><i class="fa-users-gear" style="color:$primary;"></i></h3></td><td><strong>Internal contributor view</strong></td><td>Content workflow, human review, segmented access, and API docs unification notes.</td><td><a href="https://app.gitbook.com/s/eMdr8Lu5wEKImb812laB/">Internal contributor view</a></td></tr>
<tr><td><h3><i class="fa-key" style="color:$primary;"></i></h3></td><td><strong>Authentication</strong></td><td>Show developers exactly how to create tokens, scope them, and make the first secure request.</td><td><a href="https://app.gitbook.com/s/M1iVnZAxYcYAd8w4aIU9/api-authentication">Authentication</a></td></tr>
<tr><td><h3><i class="fa-webhook" style="color:$primary;"></i></h3></td><td><strong>Webhooks</strong></td><td>Event delivery, signature verification, retries, and operational troubleshooting.</td><td><a href="https://app.gitbook.com/s/M1iVnZAxYcYAd8w4aIU9/webhooks">Webhooks</a></td></tr>
</tbody></table>

{% columns %}
{% column width="58%" %}
## What this demonstrates

- GitHub-first docs automation with content reviewed before publishing.
- Separate internal and external views without duplicating content.
- Product, onboarding, how-to, and API content in a unified docs experience.
- A developer-facing structure that can sit beside PointFive's current knowledge base and FAQ.
{% endcolumn %}

{% column width="42%" %}
{% hint style="success" icon="sparkles" %}
This is a first draft. The API examples are demo-safe placeholders that should be replaced with PointFive's real GraphQL/OpenAPI schema before a customer-facing handoff.
{% endhint %}
{% endcolumn %}
{% endcolumns %}
