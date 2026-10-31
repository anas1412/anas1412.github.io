---
title: "Valetkey - minimal LLM proxy for Kubernetes"
date: 2026-07-17
draft: false
weight: 3
tags: ["kubernetes", "llm", "go"]
summary: "Per-tenant API keys for OpenAI, Anthropic and any OpenAI-compatible model, configured as CRDs. One small image, no database, no passwords."
repo: "https://github.com/anas1412/valetkey"
demo: "https://anas.cyberia.tn/valetkey/"
tech: ["Go", "Kubernetes", "CRDs", "Helm", "Prometheus"]
showDate: false
---

Give each team or app its own API key for OpenAI, Anthropic or any OpenAI-compatible model. Your real provider keys never leave the cluster.

![Valetkey dashboard](https://raw.githubusercontent.com/anas1412/valetkey/main/docs/public/screenshots/overview-dark.png)

<div class="mt-8">{{< button href="https://anas.cyberia.tn/valetkey/" target="_blank" >}}Read the docs{{< /button >}}</div>

## What it does

- **Provider keys stay secret:** each tenant gets its own `sk-proxy-…` key. Disable, rotate or revoke it without touching the provider.
- **Configured as CRDs:** providers, tenants and keys are Kubernetes objects. Keep them in Git and deploy them with Argo CD or Flux.
- **No passwords:** Kubernetes RBAC decides who can change what, and the Kubernetes audit log records it.
- **Any provider:** OpenAI, Anthropic, and anything OpenAI-compatible (vLLM, Ollama, OpenRouter, Groq, DeepSeek, Azure).
- **Rules per key:** allowed models, IP ranges, requests and tokens per minute. Automatic failover between providers.
- **Dollar budgets:** per key, tenant and model, per day, week or month, with alerts before a budget runs out.
- **No prompts stored:** it only counts requests and tokens.

## How it works

| You create | Kind | What it is |
|---|---|---|
| Provider | `Channel` | An upstream API and its real key |
| Tenant | `Group` | A namespace allowed to use some providers |
| API key | `ProxyKey` | A virtual key, written into a Secret in the tenant's namespace |

Apps call Valetkey like any OpenAI endpoint. The `valetkeyctl` CLI and an optional dashboard cover status, provider checks and key rotation.

## Why

Every LLM gateway I looked at wanted Postgres and Redis to store what Kubernetes
already stores. CRDs and Secrets are the database.

## Get it

```bash
helm install valetkey oci://ghcr.io/anas1412/charts/valetkey \
  -n valetkey-system --create-namespace
```

The [quick start](https://anas.cyberia.tn/valetkey/guide/quick-start) walks through your first provider, tenant and key.

---

{{< github repo="anas1412/valetkey" showThumbnail=false >}}
