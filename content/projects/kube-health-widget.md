---
title: "kube-health-widget"
date: 2026-10-20
draft: false
weight: 2
tags: ["kubernetes", "monitoring", "devops"]
summary: "Kubernetes cluster health in your desktop panel, with Watchdog down detection and alerts to Telegram, Slack, Mattermost and Discord."
repo: "https://github.com/anas1412/kube-health-widget"
tech: ["QML", "Bash", "kubectl", "Alertmanager"]
showDate: false
---

A KDE Plasma 6 widget and GNOME Shell extension that shows whether your clusters are healthy, and tells you when they stop being.

## What it checks

- **Down detection:** API `/readyz` plus the Alertmanager Watchdog alert. If Watchdog stops firing, your alerting pipeline is dead, and the widget says so.
- **Pod health %:** healthy pods over total, per cluster.
- **Nodes, pods, alerts, warnings:** CPU and RAM per node, firing alerts, recent `Warning` events.
- **CI:** latest GitHub Actions or GitLab CI status for the repos you pick.

## Alerts

Desktop, Telegram, Slack, Mattermost or Discord. Sent once when a problem starts and once when it resolves, with per-rule thresholds and mute.

## Get it

```bash
curl -fsSL https://raw.githubusercontent.com/anas1412/kube-health-widget/main/install.sh | bash
```
