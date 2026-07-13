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
