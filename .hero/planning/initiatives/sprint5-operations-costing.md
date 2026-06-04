---
type: initiative
status: planning
horizon: next
title: "Sprint 5: Operations, Costing & Approvals"
tags: [9.0.0, operations, costing, approvals, sprint-5]
priority: 5
---

# Sprint 5: Operations, Costing & Approvals

## Priority: MEDIUM — Valuable for Enterprise Admins

## Scope

### Reports & Analytics (Expand)
- **Time Series Cost report** — Document advanced filters (Service, Region, Plan, Usage Type, Cost Project, Cost Team, Cost Environment, etc.)
- **Amazon Convertible RI Analytics** — Dedicated analytics dashboard
- **Capacity Planning Analytics** — Configuration options, projection charts
- **Cost dimensions** — Document Cost Project, Cost Team, Cost Environment allocation model
- **Invoice Details report** — Document Group By and tag grouping options

### Approvals (New Integration)
- **BMC Remedy/Helix** — Full approval integration (Change Requests, polling) with no documentation
- **ServiceNow Flows** — Document Flow type as alternative to Workflows

### Policies (Expand)
- **Label-based scoping** — `allowOnLabel` scoping for approval policies
- **Plan-based scoping** — `allowOnPlan` capacity policy scoping

### Identity & Auth (New Pages)
- **JumpCloud** — Identity source configuration
- **Custom External** — Custom identity source setup
- **Custom IAM API** — Programmable/API-based identity integration
- Link Azure AD/Entra ID guide from identity sources section

### Health & Scheduling
- **Alarms Management** — Full alarms interface (filtering, viewing, resolving)
- **Operations Scheduling** — Scheduling feature
- **Workload Analytics** — Workload-level analysis

## Source Code

- Reports: Time Series Cost report seeds, `AmazonConvertibleRiAnalyticsService`, `CapacityPlanningAnalyticsService`
- Approvals: `RemedyApprovalService`
- Identity: `jumpCloudConfig.jsx`, `customExternalConfig.jsx`, `customIamApiConfig.jsx`
- Health: `AlarmsController`, `SchedulingController`
