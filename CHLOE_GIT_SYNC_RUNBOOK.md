# Chloe demo runbook: PointFive Git Sync workflow

Use this as the internal presenter script for the PointFive demo/training. The customer-facing content lives in `home/`, `developer-docs/`, and `internal-knowledge/`.

## Demo assets

- Live PointFive site: https://pointfive-1.gitbook.io/pointfive-developer-docs/RoSOtyNjzLotv623mrt7/
- GitBook app site: https://app.gitbook.com/o/iSAR3PTIuTm6A8q8Tfc3/sites/site_ieHLH
- Source repo: https://github.com/gitbook-demo-sites/pointfive-demo-site-20260713
- Demo branch: `main`
- Primary Git Sync project directory for the live workflow: `developer-docs`
- Optional supporting project directories: `home`, `internal-knowledge`
- Correct initial direction for the training demo: GitHub -> GitBook

## Goal

Show PointFive how GitBook can support external product documentation and developer documentation while still fitting an engineering-owned Git workflow. Keep the story practical: a public-facing docs hub, an external developer handbook, and an internal operating model for how product/API docs stay reviewed and accurate.

## Pre-demo checklist

1. Make sure you can open the source repo while sharing screen.
2. Make sure you can open the GitBook app site and the published PointFive site.
3. Open `developer-docs/SUMMARY.md` in one tab so you can show navigation as code.
4. Open `developer-docs/getting-started/quickstart.md` in one tab for the live edit.
5. Open `developer-docs/api-reference-model.md` in one tab for the API reference story.
6. Keep `internal-knowledge/docs-automation-pipeline.md` ready as the internal process bridge.
7. Start with the published site, then reveal the GitHub workflow.

## Suggested agenda

1. Start on the published PointFive docs site.
2. Show how the site separates public overview, external developer docs, and internal knowledge.
3. Open the GitHub repo and explain the folder-to-space model.
4. Make a small edit in `developer-docs/getting-started/quickstart.md`.
5. Explain the one-time Git Sync setup for the Developer Docs space.
6. Show how `SUMMARY.md` controls the developer handbook navigation.
7. Close on governance: engineering review in GitHub, product clarity in GitBook, and adaptive access for different audiences.

## Live demo steps

### 1. Published site

Open the live PointFive site and start on the homepage.

Point out:

- the external product/documentation entry point
- the Developer Docs section for technical evaluators and integration teams
- the Internal Knowledge section as the operating model for review and docs automation
- the `View as...` links for public, developer, and internal personas

Suggested framing:

> This demo is about keeping external product docs and developer docs in one polished GitBook experience while letting technical teams maintain the source through GitHub.

### 2. Repository structure

Open the GitHub repo.

Show:

- `home/README.md` as the public docs hub
- `developer-docs/README.md` as the external developer handbook
- `developer-docs/SUMMARY.md` as the sidebar/navigation source
- `openapi/pointfive-ai-efficiency-api.yaml` as the demo API spec placeholder
- `internal-knowledge/README.md` as the internal operating model

Say:

> Each top-level folder can be connected as a separate GitBook project directory. For the live Git Sync workflow, I would demo `developer-docs` first because it maps directly to the external developer documentation handbook.

### 3. Small GitHub edit

Edit one safe sentence in `developer-docs/getting-started/quickstart.md`.

Suggested edit:

```markdown
This quickstart is maintained by the developer experience team and reviewed whenever integration workflows change.
```

Recommended live edit flow:

1. In GitHub, open `developer-docs/getting-started/quickstart.md`.
2. Click edit.
3. Add the suggested sentence near the opening guidance or review note.
4. Commit directly to `main` with the message `Update developer docs review note`.
5. Switch back to GitBook and explain that Git Sync pulls the change into the connected Developer Docs space.
6. Refresh the relevant GitBook page after sync completes.

For a real customer workflow, recommend pull requests instead of direct commits to `main`.

### 4. One-time Git Sync setup

Use this setup for the Developer Docs space:

- repo: `gitbook-demo-sites/pointfive-demo-site-20260713`
- branch: `main`
- project directory: `developer-docs`
- initial direction: GitHub -> GitBook

Click path:

1. Open the GitBook Developer Docs space dashboard.
2. Click **Set up Git Sync**.
3. Choose **GitHub**.
4. Select repository `gitbook-demo-sites/pointfive-demo-site-20260713`.
5. Select branch `main`.
6. Open advanced options.
7. Set project directory to `developer-docs`.
8. Choose initial direction **GitHub -> GitBook**.
9. Click **Initialize**.

Say clearly: Git Sync setup itself is a GitBook UI step. The API can verify sync state, but it cannot connect a repo to a space.

### 5. Navigation as code

Open `developer-docs/SUMMARY.md`.

Show that the developer handbook navigation is versioned with the rest of the docs. This is useful when product, API, and engineering teams want the docs structure reviewed alongside content changes.

### 6. API reference story

Open `openapi/pointfive-ai-efficiency-api.yaml` and `developer-docs/api-reference-model.md`.

Position this carefully:

- the current API spec is demo-safe placeholder content
- PointFive should replace it with their canonical OpenAPI or GraphQL schema
- once connected, API reference docs can become part of the same Git-based review process

### 7. Internal operating model

Open `internal-knowledge/docs-automation-pipeline.md`.

Use it to bridge from the external developer experience to the internal handbook:

1. Product and engineering define the canonical docs source.
2. Technical changes are reviewed in GitHub.
3. Git Sync publishes approved docs into GitBook.
4. GitBook gives a polished, searchable product/developer docs experience.
5. Adaptive content can show different views for public users, developers, and internal contributors.

## Anticipated questions

### Is this only for developer docs?

No. The demo uses Developer Docs as the clearest Git Sync workflow because it maps well to API and integration content, but the same repo pattern can support product docs, internal handbooks, and partner enablement docs.

### Can PointFive use pull requests?

Yes. For the live demo, commit directly to `main` to keep the flow short. For production, recommend pull requests with reviewers from engineering, product, and developer experience.

### What about GraphQL?

The demo OpenAPI file is a placeholder. If PointFive's canonical API is GraphQL, use their GraphQL schema/source workflow as the source of truth and reflect the reference content in GitBook accordingly.

### Can internal and external docs live together?

Yes. Use separate GitBook spaces, audience-aware site structure, and adaptive conditions where needed. The current demo already separates public, developer, and internal views.

## Optional extra Git Sync setup

If you want to show that the same repo can power multiple spaces, repeat the setup with:

- Home space: project directory `home`
- Internal Knowledge space: project directory `internal-knowledge`

Keep the first live walkthrough focused on `developer-docs` so the audience sees one clean end-to-end workflow.
