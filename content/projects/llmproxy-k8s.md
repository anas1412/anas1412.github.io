---
title: "llmproxy-k8s"
date: 2026-07-17
draft: false
tags: ["kubernetes", "llm", "typescript"]
summary: "A Kubernetes-native LLM proxy that issues per-tenant API keys using CRDs and Secrets — no database, no Redis."
repo: "https://github.com/anas1412/llmproxy-k8s"
tech: ["TypeScript", "NestJS", "Kubernetes", "Prometheus"]
showDate: false
---
Give your tenants API keys that forward to your real LLM providers, without
running any state of your own.

## How it works

1. You create `Channel` CRDs holding the real provider keys
2. You create a `Group` CRD per tenant, listing the channels they may use
3. Tenants create `ProxyKey` CRDs in their own namespaces, referencing their Group

## Why

Every LLM gateway I looked at wanted Postgres and Redis to store what Kubernetes
already stores. CRDs and Secrets are the database.

## Get it

```bash
kubectl create namespace llmproxy-system
kubectl apply -f deploy/crds.yaml
kubectl apply -f deploy/operator.yaml
```

---

{{< github repo="anas1412/llmproxy-k8s" showThumbnail=false >}}
