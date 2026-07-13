import json
import os
import subprocess
import sys
import textwrap
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = "https://api.gitbook.com/v1"
ORG_ID = "iSAR3PTIuTm6A8q8Tfc3"
ORG_TITLE = "PointFive"
REPO_OWNER = "gitbook-demo-sites"
REPO = "pointfive-demo-site-20260713"
REPO_URL = f"https://github.com/{REPO_OWNER}/{REPO}.git"
RAW = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO}/main"
OPENAPI_SLUG = "pointfive-ai-efficiency-api-demo"
OPENAPI_FILE = ROOT / "openapi/pointfive-ai-efficiency-api.yaml"

SPACES = [
    {
        "key": "HOME",
        "sentinel": "XSPACE_HOME",
        "folder": "home",
        "title": "Home",
        "emoji": "1f3e0",
        "icon": "house",
        "path": "home",
        "description": "Demo homepage with external and internal views for PointFive.",
    },
    {
        "key": "DEVELOPERS",
        "sentinel": "XSPACE_DEVELOPERS",
        "folder": "developer-docs",
        "title": "Developer Docs",
        "emoji": "1f4bb",
        "icon": "code",
        "path": "developers",
        "description": "External developer documentation for auth, API requests, webhooks, and errors.",
    },
    {
        "key": "INTERNAL",
        "sentinel": "XSPACE_INTERNAL",
        "folder": "internal-knowledge",
        "title": "Internal Knowledge",
        "emoji": "1f9ed",
        "icon": "users-gear",
        "path": "internal",
        "description": "Internal docs workflow, review process, and API documentation operating model.",
    },
]


def write(path: str, content: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def api(method: str, path: str, body=None, expected=(200, 201, 204)):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {os.environ['GITBOOK_TOKEN']}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            text = resp.read().decode()
            payload = json.loads(text) if text else None
            if resp.status not in expected:
                raise RuntimeError(f"{method} {path} returned {resp.status}: {text}")
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def run(cmd: list[str], cwd=ROOT, check=True):
    return subprocess.run(cmd, cwd=cwd, check=check, text=True)


def card(icon: str, title: str, description: str, href: str) -> str:
    return (
        f'<tr><td><h3><i class="fa-{icon}" style="color:$primary;"></i></h3></td>'
        f"<td><strong>{title}</strong></td><td>{description}</td>"
        f'<td><a href="{href}">{title}</a></td></tr>'
    )


def yaml_file(space: str) -> None:
    write(
        f"{space}/.gitbook.yaml",
        """
        root: ./
        structure:
          readme: README.md
          summary: SUMMARY.md
        """,
    )


def vars_file(space: str) -> None:
    write(
        f"{space}/.gitbook/vars.yaml",
        """
        company_name: PointFive
        product_name: AI Efficiency OS
        api_base_url: https://api.pointfive.example/v1
        webhook_event: finding.created
        support_email: docs-review@pointfive.example
        review_sla: "2 business days"
        """,
    )


def scaffold_assets() -> None:
    write(
        "assets/pointfive-wordmark.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="560" height="128" viewBox="0 0 560 128" role="img" aria-label="PointFive">
          <rect width="560" height="128" rx="20" fill="#08111F"/>
          <circle cx="72" cy="64" r="30" fill="#5DF2B6"/>
          <path d="M72 34 A30 30 0 0 1 72 94" fill="#2F7BFF"/>
          <text x="124" y="78" font-family="Inter, Arial, sans-serif" font-size="52" font-weight="760" fill="#FFFFFF">PointFive</text>
        </svg>
        """,
    )
    write(
        "assets/pointfive-cover.svg",
        """
        <svg xmlns="http://www.w3.org/2000/svg" width="1600" height="560" viewBox="0 0 1600 560" role="img" aria-label="PointFive developer docs">
          <defs>
            <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
              <stop offset="0" stop-color="#08111F"/>
              <stop offset="0.62" stop-color="#102D3B"/>
              <stop offset="1" stop-color="#113F36"/>
            </linearGradient>
            <pattern id="grid" width="72" height="72" patternUnits="userSpaceOnUse">
              <path d="M72 0H0V72" fill="none" stroke="#FFFFFF" stroke-opacity=".07" stroke-width="1"/>
            </pattern>
          </defs>
          <rect width="1600" height="560" fill="url(#bg)"/>
          <rect width="1600" height="560" fill="url(#grid)"/>
          <circle cx="1230" cy="178" r="190" fill="#5DF2B6" opacity=".14"/>
          <circle cx="1390" cy="385" r="142" fill="#2F7BFF" opacity=".16"/>
          <text x="104" y="166" font-family="Inter, Arial, sans-serif" font-size="76" font-weight="760" fill="#FFFFFF">PointFive Developer Docs</text>
          <text x="108" y="230" font-family="Inter, Arial, sans-serif" font-size="30" fill="#DDF7EF">Authenticate, stream findings, receive remediation webhooks, and troubleshoot integrations.</text>
          <rect x="108" y="295" width="285" height="54" rx="8" fill="#5DF2B6"/>
          <text x="136" y="330" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="720" fill="#08111F">Start in five minutes</text>
          <g transform="translate(980 112)">
            <rect width="470" height="328" rx="18" fill="#06101A" stroke="#FFFFFF" stroke-opacity=".16"/>
            <text x="34" y="58" font-family="IBMPlexMono, monospace" font-size="20" fill="#5DF2B6">POST /v1/findings/query</text>
            <text x="34" y="116" font-family="IBMPlexMono, monospace" font-size="18" fill="#FFFFFF">{</text>
            <text x="58" y="150" font-family="IBMPlexMono, monospace" font-size="18" fill="#FFFFFF">"cloud": "aws",</text>
            <text x="58" y="184" font-family="IBMPlexMono, monospace" font-size="18" fill="#FFFFFF">"severity": "high",</text>
            <text x="58" y="218" font-family="IBMPlexMono, monospace" font-size="18" fill="#FFFFFF">"category": "deepwaste"</text>
            <text x="34" y="252" font-family="IBMPlexMono, monospace" font-size="18" fill="#FFFFFF">}</text>
            <path d="M34 282H432" stroke="#5DF2B6" stroke-width="4"/>
          </g>
        </svg>
        """,
    )


def scaffold_home() -> None:
    yaml_file("home")
    vars_file("home")
    write(
        "home/SUMMARY.md",
        """
        # Table of contents

        * [Home](README.md)
        * [Demo assumptions](demo-assumptions.md)
        """,
    )
    write(
        "home/README.md",
        f"""
        ---
        description: "A tailored GitBook demo for PointFive's developer and internal documentation workflows."
        icon: house
        cover: "{RAW}/assets/pointfive-cover.svg"
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
        {card("code", "External developer view", "API setup, requests, webhooks, troubleshooting, and integration patterns for customers.", "https://app.gitbook.com/s/XSPACE_DEVELOPERS/")}
        {card("users-gear", "Internal contributor view", "Content workflow, human review, segmented access, and API docs unification notes.", "https://app.gitbook.com/s/XSPACE_INTERNAL/")}
        {card("key", "Authentication", "Show developers exactly how to create tokens, scope them, and make the first secure request.", "https://app.gitbook.com/s/XSPACE_DEVELOPERS/api-authentication")}
        {card("webhook", "Webhooks", "Event delivery, signature verification, retries, and operational troubleshooting.", "https://app.gitbook.com/s/XSPACE_DEVELOPERS/webhooks")}
        </tbody></table>

        {{% columns %}}
        {{% column width="58%" %}}
        ## What this demonstrates

        - GitHub-first docs automation with content reviewed before publishing.
        - Separate internal and external views without duplicating content.
        - Product, onboarding, how-to, and API content in a unified docs experience.
        - A developer-facing structure that can sit beside PointFive's current knowledge base and FAQ.
        {{% endcolumn %}}

        {{% column width="42%" %}}
        {{% hint style="success" icon="sparkles" %}}
        This is a first draft. The API examples are demo-safe placeholders that should be replaced with PointFive's real GraphQL/OpenAPI schema before a customer-facing handoff.
        {{% endhint %}}
        {{% endcolumn %}}
        {{% endcolumns %}}
        """,
    )
    write(
        "home/demo-assumptions.md",
        """
        ---
        description: "Scope and assumptions behind this first-draft demo."
        icon: clipboard-list
        ---

        # Demo assumptions

        This demo was created from the sales request, PointFive's public positioning, and the current direction of their knowledge base and FAQ.

        ## Assumptions

        - PointFive wants to show a developer-first docs experience, not a marketing site.
        - API examples should be representative and demo-safe until the real GraphQL/OpenAPI schema is available.
        - Internal docs should focus on how PMs, CSMs, and engineers collaborate on content.
        - Visitor authentication and segmented access are important enough to show as an information architecture pattern.

        ## Best feedback areas

        1. Replace placeholder endpoint names with real API or GraphQL operations.
        2. Confirm which content should be public, customer-only, or internal-only.
        3. Decide whether API reference should be generated from OpenAPI, GraphQL schema, or both.
        """,
    )


def scaffold_developer_docs() -> None:
    yaml_file("developer-docs")
    vars_file("developer-docs")
    write(
        "developer-docs/SUMMARY.md",
        """
        # Table of contents

        * [Developer Docs](README.md)

        ## Getting started

        * [Quickstart](getting-started/quickstart.md)
        * [Make your first API request](getting-started/first-api-request.md)

        ## Core integration

        * [API authentication](api-authentication.md)
        * [Webhooks](webhooks.md)
        * [Troubleshooting](troubleshooting.md)

        ## Reference

        * [API reference model](api-reference-model.md)
        * ```yaml
          type: builtin:openapi
          props:
            models: true
            downloadLink: true
          dependencies:
            spec:
              ref:
                kind: openapi
                spec: pointfive-ai-efficiency-api-demo
          ```
        """,
    )
    write(
        "developer-docs/README.md",
        """
        ---
        description: "Build cloud and AI efficiency workflows with PointFive."
        icon: code
        layout:
          width: default
          title:
            visible: true
          description:
            visible: true
          tableOfContents:
            visible: true
          outline:
            visible: true
          pagination:
            visible: true
        ---

        # Developer Docs

        Use PointFive APIs and webhooks to bring cost intelligence into the workflows developers already use: pull requests, CI/CD checks, IDEs, FinOps dashboards, and remediation queues.

        <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
        <tr><td><h3><i class="fa-bolt" style="color:$primary;"></i></h3></td><td><strong>Quickstart</strong></td><td>Create a token, query high-impact findings, and inspect remediation context.</td><td><a href="getting-started/quickstart.md">Quickstart</a></td></tr>
        <tr><td><h3><i class="fa-key" style="color:$primary;"></i></h3></td><td><strong>Authentication</strong></td><td>Use scoped service tokens safely across development, CI, and production.</td><td><a href="api-authentication.md">Authentication</a></td></tr>
        <tr><td><h3><i class="fa-webhook" style="color:$primary;"></i></h3></td><td><strong>Webhooks</strong></td><td>Receive findings, remediation status changes, and policy alerts.</td><td><a href="webhooks.md">Webhooks</a></td></tr>
        <tr><td><h3><i class="fa-triangle-exclamation" style="color:$primary;"></i></h3></td><td><strong>Troubleshooting</strong></td><td>Resolve auth failures, missing findings, duplicate events, and rate limits.</td><td><a href="troubleshooting.md">Troubleshooting</a></td></tr>
        </tbody></table>

        ## Typical flow

        ```mermaid
        sequenceDiagram
            participant Dev as Developer or CI
            participant API as PointFive API
            participant Review as Human review
            participant Prod as Production docs

            Dev->>API: Query waste findings
            API-->>Dev: Findings and remediation context
            Dev->>Review: Open PR with suggested doc or code change
            Review-->>Prod: Approve and publish
        ```
        """,
    )
    write(
        "developer-docs/getting-started/quickstart.md",
        """
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
        curl "https://api.pointfive.example/v1/findings/query" \\
          -H "Authorization: Bearer $POINTFIVE_API_TOKEN" \\
          -H "Content-Type: application/json" \\
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
        """,
    )
    write(
        "developer-docs/getting-started/first-api-request.md",
        """
        ---
        description: "Send your first API request and inspect the response."
        icon: paper-plane
        ---

        # Make your first API request

        Use a service token to query findings that match a cloud, account, or severity filter.

        {% tabs %}
        {% tab title="cURL" %}
        ```bash
        curl "https://api.pointfive.example/v1/findings/query" \\
          -H "Authorization: Bearer $POINTFIVE_API_TOKEN" \\
          -H "Content-Type: application/json" \\
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
        """,
    )
    write(
        "developer-docs/api-authentication.md",
        """
        ---
        description: "Authenticate requests with scoped service tokens."
        icon: key
        ---

        # API authentication

        PointFive API requests use bearer tokens. Create separate service tokens for local development, CI/CD, and production automation.

        ## Header

        ```http
        Authorization: Bearer <POINTFIVE_API_TOKEN>
        ```

        ## Recommended scopes

        | Scope | Use |
        | --- | --- |
        | `findings:read` | Query DeepWaste and AI usage findings. |
        | `remediations:write` | Create or update remediation tasks. |
        | `webhooks:write` | Register or rotate webhook endpoints. |
        | `accounts:read` | Resolve account and environment metadata. |

        {% hint style="warning" %}
        Use the narrowest token that can complete the job. CI jobs that only annotate pull requests should not receive write access to remediation records.
        {% endhint %}

        ## Token lifecycle

        ```mermaid
        stateDiagram-v2
            [*] --> Created
            Created --> Active
            Active --> Rotating
            Rotating --> Active
            Active --> Revoked
            Revoked --> [*]
        ```

        ## Common authentication failures

        <details>
        <summary>`401 Unauthorized`</summary>

        The token is missing, expired, malformed, or revoked. Check the `Authorization` header and rotate the token if needed.
        </details>

        <details>
        <summary>`403 Forbidden`</summary>

        The token is valid but does not have the required scope for this endpoint or account.
        </details>
        """,
    )
    write(
        "developer-docs/webhooks.md",
        """
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
        """,
    )
    write(
        "developer-docs/troubleshooting.md",
        """
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
        """,
    )
    write(
        "developer-docs/api-reference-model.md",
        """
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
        """,
    )


def scaffold_internal() -> None:
    yaml_file("internal-knowledge")
    vars_file("internal-knowledge")
    write(
        "internal-knowledge/SUMMARY.md",
        """
        # Table of contents

        * [Internal Knowledge](README.md)

        ## Documentation workflow

        * [Docs automation pipeline](docs-automation-pipeline.md)
        * [Human review process](human-review-process.md)
        * [Segmented access model](segmented-access-model.md)

        ## Knowledge management

        * [Internal knowledge base](internal-knowledge-base.md)
        * [API docs unification](api-docs-unification.md)
        """,
    )
    write(
        "internal-knowledge/README.md",
        """
        ---
        description: "Internal docs operating model for PMs, CSMs, and engineers."
        icon: users-gear
        ---

        # Internal Knowledge

        This internal view demonstrates how PointFive's PMs, CSMs, and engineers can collaborate on docs without exposing draft or internal-only content to customers.

        ## Contributor roles

        | Team | Role in docs |
        | --- | --- |
        | Product managers | Own product narrative, release notes, and customer-facing workflows. |
        | CSMs | Flag unclear customer journeys and contribute troubleshooting patterns. |
        | Engineers | Tag the docs agent in pull requests and review technical accuracy. |

        {% hint style="info" %}
        This space is intentionally separate from the external developer docs. In a production setup, visitor authentication can make this visible only to internal teammates.
        {% endhint %}
        """,
    )
    write(
        "internal-knowledge/docs-automation-pipeline.md",
        """
        ---
        description: "A GitHub and CI/CD driven documentation automation workflow."
        icon: code-branch
        ---

        # Docs automation pipeline

        PointFive's key requirement is docs automation tied to code changes with human review before publishing.

        ```mermaid
        flowchart LR
            Code[Product or API change] --> PR[GitHub pull request]
            PR --> Agent[Docs agent tagged]
            Agent --> Draft[Draft docs update]
            Draft --> Review[PM or engineer review]
            Review --> Publish[GitBook publish]
        ```

        ## Recommended checks

        - Detect changed API schema or GraphQL fields.
        - Suggest guide updates for new remediation workflows.
        - Block publishing until required reviewers approve.
        - Keep AI-generated drafts visible as suggestions, not silent changes.
        """,
    )
    write(
        "internal-knowledge/human-review-process.md",
        """
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
        """,
    )
    write(
        "internal-knowledge/segmented-access-model.md",
        """
        ---
        description: "Model public, customer-only, and internal docs access."
        icon: lock
        ---

        # Segmented access model

        Use visitor authentication to show the right docs to the right audience.

        | Audience | Content |
        | --- | --- |
        | Public visitors | Product overview, onboarding, common how-to guides, FAQ. |
        | Authenticated customers | API reference, environment-specific setup, account configuration. |
        | Internal team | Roadmap notes, support playbooks, draft release content, review queues. |

        {% hint style="success" %}
        The default public view should still feel complete. Gate sensitive or account-specific content, not the whole docs experience.
        {% endhint %}
        """,
    )
    write(
        "internal-knowledge/internal-knowledge-base.md",
        """
        ---
        description: "Internal knowledge management patterns for CSMs and product teams."
        icon: book-open
        ---

        # Internal knowledge base

        Internal KB content should capture the context that external docs should not: implementation caveats, customer patterns, escalation paths, and enablement notes.

        ## Suggested internal collections

        - CSM troubleshooting playbooks.
        - Product launch readiness notes.
        - Known limitations and recommended workarounds.
        - Competitive positioning for cloud and AI efficiency workflows.
        """,
    )
    write(
        "internal-knowledge/api-docs-unification.md",
        """
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
        """,
    )


def scaffold_openapi() -> None:
    write(
        "openapi/pointfive-ai-efficiency-api.yaml",
        """
        openapi: 3.1.0
        info:
          title: PointFive AI Efficiency API
          version: demo
          description: Demo-safe placeholder API used for the GitBook site preview.
        servers:
          - url: https://api.pointfive.example/v1
        security:
          - bearerAuth: []
        paths:
          /findings/query:
            post:
              summary: Query efficiency findings
              operationId: queryFindings
              tags: [Findings]
              requestBody:
                required: true
                content:
                  application/json:
                    schema:
                      $ref: '#/components/schemas/FindingQuery'
              responses:
                '200':
                  description: Matching findings
                  content:
                    application/json:
                      schema:
                        type: object
                        properties:
                          findings:
                            type: array
                            items:
                              $ref: '#/components/schemas/Finding'
          /remediations:
            post:
              summary: Create a remediation review task
              operationId: createRemediation
              tags: [Remediations]
              requestBody:
                required: true
                content:
                  application/json:
                    schema:
                      type: object
                      properties:
                        findingId:
                          type: string
                        reviewer:
                          type: string
              responses:
                '202':
                  description: Remediation task queued
          /webhooks/test:
            post:
              summary: Send a test webhook event
              operationId: sendTestWebhook
              tags: [Webhooks]
              responses:
                '202':
                  description: Test event accepted
        components:
          securitySchemes:
            bearerAuth:
              type: http
              scheme: bearer
          schemas:
            FindingQuery:
              type: object
              properties:
                cloud:
                  type: string
                  enum: [aws, azure, gcp, snowflake, databricks]
                severity:
                  type: string
                  enum: [low, medium, high, critical]
                category:
                  type: string
            Finding:
              type: object
              properties:
                id:
                  type: string
                category:
                  type: string
                resource:
                  type: string
                estimatedMonthlyWaste:
                  type: number
                remediation:
                  type: object
                  properties:
                    status:
                      type: string
                    source:
                      type: string
        """,
    )


def scaffold_content() -> None:
    write(
        "README.md",
        """
        # PointFive demo site

        First-draft GitBook demo content for PointFive. Each top-level folder is imported as a GitBook space in the PointFive org.

        The API examples are demo-safe placeholders and should be replaced with PointFive's canonical API or GraphQL schema.
        """,
    )
    write(
        ".gitignore",
        """
        .DS_Store
        Thumbs.db
        *.swp
        *.swo
        .idea/
        .vscode/
        __pycache__/
        """,
    )
    scaffold_assets()
    scaffold_home()
    scaffold_developer_docs()
    scaffold_internal()
    scaffold_openapi()


def ensure_repo() -> None:
    if not (ROOT / ".git").exists():
        run(["git", "init", "-b", "main"])
    run(["git", "add", "."])
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode != 0:
        run(["git", "commit", "-m", "Initial PointFive demo scaffold"])

    view = subprocess.run(["gh", "repo", "view", f"{REPO_OWNER}/{REPO}"], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    remotes = subprocess.run(["git", "remote"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    if "origin" not in remotes:
        if view.returncode == 0:
            run(["git", "remote", "add", "origin", REPO_URL])
        else:
            run(["gh", "repo", "create", f"{REPO_OWNER}/{REPO}", "--public", "--source", str(ROOT), "--remote", "origin", "--push"])
            return
    run(["git", "push", "-u", "origin", "main"])


def git_commit_push(message: str) -> None:
    run(["git", "add", "."])
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode != 0:
        run(["git", "commit", "-m", message])
    run(["git", "push"])


def ensure_openapi_spec(org_id: str) -> dict:
    payload = {"slug": OPENAPI_SLUG, "source": {"text": OPENAPI_FILE.read_text(encoding="utf-8")}}
    try:
        _, spec = api("POST", f"/orgs/{org_id}/openapi", payload)
        return {"created": True, "slug": OPENAPI_SLUG, "spec": spec}
    except RuntimeError as exc:
        if "400" not in str(exc) and "409" not in str(exc):
            raise
        _, specs = api("GET", f"/orgs/{org_id}/openapi")
        items = specs.get("items") or specs.get("results") or (specs if isinstance(specs, list) else [])
        for item in items:
            if item.get("slug") == OPENAPI_SLUG:
                return {"created": False, "slug": OPENAPI_SLUG, "spec": item, "note": "slug already existed"}
        return {"created": False, "slug": OPENAPI_SLUG, "error": str(exc)}


def create_site(org_id: str, openapi_result: dict) -> dict:
    _, site = api(
        "POST",
        f"/orgs/{org_id}/sites",
        {"type": "ultimate", "title": "PointFive Developer Docs", "visibility": "share-link"},
    )
    site_id = site["id"]
    api(
        "PATCH",
        f"/orgs/{org_id}/sites/{site_id}",
        {"title": "PointFive Developer Docs", "visibility": "share-link", "basename": "pointfive-developer-docs"},
    )
    created = {
        "org": org_id,
        "org_title": ORG_TITLE,
        "site": site_id,
        "spaces": {},
        "sections": {},
        "site_spaces": {},
        "site_object": site,
        "openapi": openapi_result,
    }
    for item in SPACES:
        _, space = api(
            "POST",
            f"/orgs/{org_id}/spaces",
            {"title": item["title"], "emoji": item["emoji"], "empty": True, "editMode": "live"},
        )
        space_id = space["id"]
        created["spaces"][item["key"]] = space_id
        _, section = api(
            "POST",
            f"/orgs/{org_id}/sites/{site_id}/sections",
            {"spaceId": space_id, "title": item["title"], "icon": item["icon"], "draft": False},
        )
        section_id = section["id"]
        site_space_id = section["siteSpaces"][0]["id"]
        created["sections"][item["key"]] = section_id
        created["site_spaces"][item["key"]] = site_space_id
        api(
            "PATCH",
            f"/orgs/{org_id}/sites/{site_id}/sections/{section_id}",
            {"path": item["path"], "description": item["description"], "draft": False, "defaultSiteSpace": site_space_id},
        )
    api(
        "PATCH",
        f"/orgs/{org_id}/sites/{site_id}",
        {"defaultSiteSection": created["sections"]["HOME"], "defaultSiteSpace": created["site_spaces"]["HOME"]},
    )
    return created


def replace_sentinels(space_ids: dict[str, str]) -> None:
    replacements = {item["sentinel"]: space_ids[item["key"]] for item in SPACES}
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")


def import_spaces(created: dict) -> None:
    imports = {}
    for item in SPACES:
        status, _ = api(
            "POST",
            f"/spaces/{created['spaces'][item['key']]}/git/import",
            {
                "url": REPO_URL,
                "ref": "refs/heads/main",
                "repoProjectDirectory": item["folder"],
                "repoTreeURL": f"https://github.com/{REPO_OWNER}/{REPO}/tree/main",
                "repoCommitURL": f"https://github.com/{REPO_OWNER}/{REPO}/commit",
                "force": True,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            expected=(204,),
        )
        imports[item["key"]] = {"status": status, "space": created["spaces"][item["key"]], "folder": item["folder"]}
    write("gitbook-import-results.json", json.dumps(imports, indent=2))


def customization_payload(created: dict) -> dict:
    logo = f"{RAW}/assets/pointfive-wordmark.svg"
    return {
        "title": "PointFive Developer Docs",
        "localizedTitle": {},
        "internationalization": {"locale": "en"},
        "styling": {
            "theme": "clean",
            "primaryColor": {"light": "#0F7B5F", "dark": "#5DF2B6"},
            "infoColor": {"light": "#2F7BFF", "dark": "#82B4FF"},
            "successColor": {"light": "#0F7B5F", "dark": "#5DF2B6"},
            "warningColor": {"light": "#C98216", "dark": "#F5C45B"},
            "dangerColor": {"light": "#C93C4A", "dark": "#FF8691"},
            "tint": {"color": {"light": "#F4FBF8", "dark": "#08111F"}},
            "corners": "rounded",
            "depth": "flat",
            "links": "accent",
            "font": "Inter",
            "monospaceFont": "IBMPlexMono",
            "icons": "regular",
            "background": "plain",
            "sidebar": {"background": "filled", "list": "line"},
            "codeTheme": {
                "default": {"light": "default-light", "dark": "default-dark"},
                "openapi": {"light": "default-light", "dark": "default-dark"},
            },
            "search": "prominent",
        },
        "favicon": {"icon": {"light": logo, "dark": logo}},
        "header": {
            "preset": "default",
            "logo": {"light": logo, "dark": logo},
            "links": [
                {"title": "Developers", "to": {"kind": "space", "space": created["spaces"]["DEVELOPERS"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Internal", "to": {"kind": "space", "space": created["spaces"]["INTERNAL"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "PointFive", "to": {"kind": "url", "url": "https://www.pointfive.co/"}, "style": "button-secondary", "links": [], "localizedTitle": {}},
            ],
        },
        "footer": {
            "logo": {"light": logo, "dark": logo},
            "groups": [
                {
                    "title": "Demo sections",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Home", "to": {"kind": "space", "space": created["spaces"]["HOME"]}, "localizedTitle": {}},
                        {"title": "Developer Docs", "to": {"kind": "space", "space": created["spaces"]["DEVELOPERS"]}, "localizedTitle": {}},
                        {"title": "Internal Knowledge", "to": {"kind": "space", "space": created["spaces"]["INTERNAL"]}, "localizedTitle": {}},
                    ],
                },
                {
                    "title": "Sources",
                    "localizedTitle": {},
                    "links": [
                        {"title": "PointFive", "to": {"kind": "url", "url": "https://www.pointfive.co/"}, "localizedTitle": {}},
                        {"title": "Knowledge base", "to": {"kind": "url", "url": "https://www.pointfive.co/knowledge-base"}, "localizedTitle": {}},
                        {"title": "Source repo", "to": {"kind": "url", "url": f"https://github.com/{REPO_OWNER}/{REPO}"}, "localizedTitle": {}},
                    ],
                },
            ],
            "copyright": "PointFive Developer Docs demo - sample content only.",
        },
        "themes": {"default": "light", "toggeable": True},
        "pdf": {"enabled": True},
        "feedback": {"enabled": True},
        "ai": {
            "mode": "assistant",
            "suggestions": [
                "How do I authenticate with the API?",
                "How do I subscribe to webhooks?",
                "What should I include in a troubleshooting ticket?",
                "How does the internal docs review workflow work?",
            ],
        },
        "advancedCustomization": {"enabled": True},
        "trademark": {"enabled": True},
        "externalLinks": {"target": "self"},
        "pagination": {"enabled": True},
        "pageActions": {"externalAI": True, "markdown": True, "mcp": True, "items": ["assistant", "markdown", "external-ai", "mcp", "pdf"]},
        "git": {"showEditLink": False},
        "privacyPolicy": {"url": "https://www.pointfive.co/privacy-policy"},
        "socialPreview": {"url": logo},
        "socialAccounts": [{"platform": "linkedin", "handle": "company/pointfive", "display": {"footer": True, "header": False}}],
        "insights": {"trackingCookie": True},
    }


def apply_customization(org_id: str, site_id: str, created: dict) -> None:
    _, customized = api("PUT", f"/orgs/{org_id}/sites/{site_id}/customization", customization_payload(created))
    write("gitbook-customization-result.json", json.dumps(customized, indent=2))


def main() -> None:
    scaffold_content()
    ensure_repo()
    openapi_result = ensure_openapi_spec(ORG_ID)

    created_path = ROOT / "gitbook-created.json"
    if created_path.exists():
        created = json.loads(created_path.read_text(encoding="utf-8"))
        replace_sentinels(created["spaces"])
        git_commit_push("Resolve PointFive GitBook space links")
    else:
        created = create_site(ORG_ID, openapi_result)
        replace_sentinels(created["spaces"])
        write("gitbook-created.json", json.dumps(created, indent=2))
        git_commit_push("Resolve PointFive GitBook space links")

    import_spaces(created)
    try:
        first_publish_status, first_publish = api("POST", f"/orgs/{ORG_ID}/sites/{created['site']}/publish")
    except RuntimeError as exc:
        if "Site is already published" not in str(exc):
            raise
        first_publish_status, first_publish = api("GET", f"/orgs/{ORG_ID}/sites/{created['site']}")

    share_status, share = api("POST", f"/orgs/{ORG_ID}/sites/{created['site']}/share-links", {"name": "PointFive demo review"})
    apply_customization(ORG_ID, created["site"], created)

    try:
        publish_status, publish = api("POST", f"/orgs/{ORG_ID}/sites/{created['site']}/publish")
    except RuntimeError as exc:
        if "Site is already published" not in str(exc):
            raise
        publish_status, publish = api("GET", f"/orgs/{ORG_ID}/sites/{created['site']}")

    _, structure = api("GET", f"/orgs/{ORG_ID}/sites/{created['site']}/structure")
    write("gitbook-structure.json", json.dumps(structure, indent=2))
    final = {
        "org": ORG_ID,
        "org_title": ORG_TITLE,
        "publish_status": publish_status,
        "publish": publish,
        "first_publish_status": first_publish_status,
        "share_status": share_status,
        "share": share,
        "published_url": share["urls"]["published"],
        "app_url": publish["urls"]["app"],
        "preview_url": publish["urls"]["preview"],
        "repo": f"https://github.com/{REPO_OWNER}/{REPO}",
        "openapi": openapi_result,
    }
    write("gitbook-publish-share.json", json.dumps(final, indent=2))
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    if "GITBOOK_TOKEN" not in os.environ:
        print("GITBOOK_TOKEN is required", file=sys.stderr)
        sys.exit(1)
    main()
