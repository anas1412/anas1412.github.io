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
A reference stack where **one gateway does everything** — L7 path routing, L4 raw
TCP proxying for Postgres, per-route basic auth, and native Prometheus metrics
into Grafana.

The React + NestJS + Postgres app exists only to generate real traffic worth
routing and watching.

## Stack

Deployed to Kubernetes with Kustomize on k3d.

---

[Source](https://github.com/anas1412/envoy-fullstack-k8s)
*Envoy, Kubernetes, k3d, Kustomize, React, NestJS, Postgres*
