---
description: "Authenticate and query your first cloud efficiency findings."
icon: bolt
---

# Quickstart

Follow this path to authenticate, query findings, and connect remediation updates back into your workflow.

{% stepper %}
{% step %}
## Create a service token

In the PointFive console, create a service token with the minimum scopes required for your workflow.

For a read-only integration, start with `findings:read` and `accounts:read`.
{% endstep %}

{% step %}
## Store the token in your secret manager

Store the token as `POINTFIVE_API_TOKEN`. Do not commit it to the repository.
{% endstep %}

{% step %}
## Query high-impact findings

Use the API to find waste candidates that are safe to route into review.

```bash
curl "https://api.pointfive.example/v1/findings/query" \
  -H "Authorization: Bearer $POINTFIVE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "cloud": "aws",
    "severity": "high",
    "category": "deepwaste"
  }'
```
{% endstep %}

{% step %}
## Subscribe to webhooks

Add a webhook endpoint so PointFive can notify your systems when a finding changes state.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
These examples use demo-safe endpoint names. Replace them with the canonical PointFive API or GraphQL schema when available.
{% endhint %}
