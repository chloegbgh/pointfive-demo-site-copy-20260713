---
description: "Resolve common API, webhook, and integration issues."
icon: triangle-exclamation
---

# Troubleshooting

Start with the symptom, then check the likely cause and fix.

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `401 Unauthorized` | Missing or revoked token | Rotate the token and confirm the header format. |
| `403 Forbidden` | Token scope does not match endpoint | Add the minimum required scope. |
| Empty findings list | Filters are too narrow or account sync is incomplete | Relax filters and confirm the cloud account is connected. |
| Duplicate webhook events | Endpoint retried after timeout | Deduplicate by `event.id`. |
| Signature verification fails | Body was parsed before verification | Verify against the raw request body. |

{% hint style="info" %}
Include `request_id`, endpoint, timestamp, token scope, and sanitized payload when escalating an API issue.
{% endhint %}

## Support bundle checklist

{% stepper %}
{% step %}
## Capture the request ID

Every API response includes a request identifier. Include it in support tickets.
{% endstep %}

{% step %}
## Confirm account and environment

Specify cloud provider, account, workspace, and environment.
{% endstep %}

{% step %}
## Remove secrets

Redact bearer tokens, webhook secrets, and customer identifiers before sharing logs.
{% endstep %}
{% endstepper %}
