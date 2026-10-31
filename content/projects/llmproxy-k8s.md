---
title: "LLMP - your LLM keys, shared safely on Kubernetes"
date: 2026-07-17
draft: false
weight: 3
tags: ["kubernetes", "llm", "go"]
summary: "A Kubernetes-native LLM proxy. Each tenant gets its own API key for OpenAI, Anthropic or any OpenAI-compatible model, with limits, a dashboard and an audit trail. No database."
repo: "https://github.com/anas1412/llmp"
demo: "https://anas.cyberia.tn/llmp/"
tech: ["Go", "Kubernetes", "CRDs", "Prometheus"]
showDate: false
---

Give each app or team its own API key for OpenAI, Anthropic or any OpenAI-compatible model. Your real provider keys never leave the cluster.

![LLMP dashboard](https://raw.githubusercontent.com/anas1412/llmp/main/docs/public/screenshots/overview-dark.png)

<div class="mt-8">{{< button href="https://anas.cyberia.tn/llmp/" target="_blank" >}}Read the docs{{< /button >}}</div>

## What it does

- **Virtual keys per tenant:** each app gets its own `sk-proxy-…` key. Disable, rotate or delete it without touching the provider.
- **Any provider:** OpenAI, Anthropic, and anything OpenAI-compatible (vLLM, Ollama, OpenRouter, Groq, DeepSeek, Azure).
- **Limits per key:** allowed models, IP ranges, requests and tokens per minute. Automatic failover between providers.
- **Built-in dashboard:** add a provider by pasting its key, create keys with copy-paste examples, watch usage live.
- **Audited admin access:** sign-in lockout, revocable sessions, and every admin change in the activity log.
- **Small to run:** one 32 MB image, about 15 MB of memory, no database, no Redis.

## How it works

| You create | Kind | What it is |
|---|---|---|
| Provider | `Channel` | An upstream API and its real key |
| Tenant | `Group` | A namespace allowed to use some providers |
| API key | `ProxyKey` | A virtual key in the tenant's namespace |

All three can be managed from the dashboard or with `kubectl`.

## Why

Every LLM gateway I looked at wanted Postgres and Redis to store what Kubernetes
already stores. CRDs and Secrets are the database.

## Get it

```bash
kubectl create namespace llmproxy-system
kubectl apply -f https://raw.githubusercontent.com/anas1412/llmp/main/deploy/crds.yaml
kubectl apply -f https://raw.githubusercontent.com/anas1412/llmp/main/deploy/operator.yaml
```

The [quick start](https://anas.cyberia.tn/llmp/guide/quick-start) covers turning on the dashboard and creating your first key.

---

{{< github repo="anas1412/llmp" showThumbnail=false >}}
