---
description: "Send your first API request and inspect the response."
icon: paper-plane
---

# Make your first API request

Use a service token to query findings that match a cloud, account, or severity filter.

{% tabs %}
{% tab title="cURL" %}
```bash
curl "https://api.pointfive.example/v1/findings/query" \
  -H "Authorization: Bearer $POINTFIVE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"cloud":"aws","severity":"high"}'
```
{% endtab %}

{% tab title="Node.js" %}
```javascript
const response = await fetch("https://api.pointfive.example/v1/findings/query", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.POINTFIVE_API_TOKEN}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ cloud: "aws", severity: "high" })
});

if (!response.ok) throw new Error(`PointFive API error: ${response.status}`);
console.log(await response.json());
```
{% endtab %}
{% endtabs %}

## Response

```json
{
  "findings": [
    {
      "id": "fnd_01HZE6",
      "category": "deepwaste",
      "resource": "eks/prod/token-router",
      "estimatedMonthlyWaste": 18400,
      "remediation": {
        "status": "review_required",
        "source": "ci"
      }
    }
  ]
}
```
