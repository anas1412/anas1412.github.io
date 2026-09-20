---
title: "Envoy Full-Stack Reference"
date: 2026-08-15
draft: false
tags: ["kubernetes", "envoy", "observability"]
summary: "Envoy as the single ingress: L7 routing, L4 Postgres proxying, per-route auth and Prometheus metrics through one gateway."
repo: "https://github.com/anas1412/envoy-fullstack-k8s"
tech: ["Envoy", "Kubernetes", "k3d", "Kustomize", "React", "NestJS", "Postgres"]
showDate: false
---

A reference stack where **one gateway does everything** - L7 path routing, L4 raw
TCP proxying for Postgres, per-route basic auth, and native Prometheus metrics
into Grafana.

The React + NestJS + Postgres app exists only to generate real traffic worth
routing and watching.

![envoy-fullstack-k8s](https://raw.githubusercontent.com/anas1412/envoy-fullstack-k8s/main/preview.png)

## Stack

Deployed to Kubernetes with Kustomize on k3d.

## Get it

One command builds the images, creates the k3d cluster, applies the manifests
and waits for readiness:

```bash
./scripts/k3d-up.sh      # http://localhost:30080/
./scripts/k3d-down.sh    # tears everything back down
```

---

{{< github repo="anas1412/envoy-fullstack-k8s" showThumbnail=false >}}
