---
description: "Subscribe to PointFive events and verify webhook delivery."
icon: webhook
---

# Webhooks

Webhooks let your systems react when PointFive creates a finding, updates remediation status, or detects an AI usage policy event.

## Delivery flow

```mermaid
sequenceDiagram
    participant PF as PointFive
    participant App as Your endpoint
    participant Queue as Work queue
    participant Human as Reviewer

    PF->>App: POST finding.created
    App->>App: Verify signature
    App->>Queue: Enqueue remediation review
    Queue->>Human: Assign task
    Human-->>PF: Approve or reject remediation
```

## Verify signatures

Every webhook request includes a timestamp and signature.

```bash
X-PointFive-Timestamp: 2026-07-13T12:00:00Z
X-PointFive-Signature: sha256=...
```

{% tabs %}
{% tab title="Node.js" %}
```javascript
import crypto from "node:crypto";

function verifyWebhook(secret, timestamp, body, signature) {
  const payload = `${timestamp}.${body}`;
  const expected = crypto
    .createHmac("sha256", secret)
    .update(payload)
    .digest("hex");

  return crypto.timingSafeEqual(
    Buffer.from(`sha256=${expected}`),
    Buffer.from(signature)
  );
}
```
{% endtab %}

{% tab title="Python" %}
```python
import hmac
import hashlib

def verify_webhook(secret, timestamp, body, signature):
    payload = f"{timestamp}.{body}".encode()
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```
{% endtab %}
{% endtabs %}

## Retry behavior

| Response | PointFive behavior |
| --- | --- |
| `2xx` | Delivery is marked successful. |
| `4xx` | Delivery is not retried unless the event is manually replayed. |
| `5xx` or timeout | Delivery is retried with exponential backoff. |
