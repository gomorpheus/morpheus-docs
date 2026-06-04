---
type: initiative
slug: sprint6-certs-dns-provisioning
status: completed
horizon: next
title: "Sprint 6: Certificates, DNS, SCM & Provisioning Features"
tags: [9.0.0, certificates, dns, scm, provisioning, sprint-6]
priority: 6
---

# Sprint 6: Certificates, DNS, SCM & Provisioning Features

## Priority: MEDIUM — Operational Features Missing Documentation

## Scope

### Certificate/Trust Management (New Section)
- **Certificate Service** — Core certificate management capabilities
- **Certificate Authorities** — CA integration
- **Private Key Management** — Key management
- **NSX-T Certificates** — Certificate management for NSX-T
- **Amazon Certificate Manager (ACM)** — Integration
- **Certificate Export** — Export functionality

### DNS (Expand)
- **Plugin DNS Framework** — Plugin-based DNS provider extensibility
- **Built-in DNS Resolver** — Full record type support (MX, NS, PTR, DNAME, SOA, TSIG, etc.)

### SCM/Code (Expand)
- **Git Code Service** — Git repository integration as standalone feature
- **GitHub Code Service** — GitHub-specific integration details
- **Terraform Tools** — Terraform as a Tools-level feature (state management, drift)

### Provisioning Features (Expand)
- **Provisioning Licenses** — Windows license key management applied during provisioning
- **Provisioning Settings** — Admin-level ordering and defaults
- **Conditional Workflow tasks** — Detailed configuration (JavaScript syntax, branching, result propagation)
- **Write Attributes task** — JSON payload format documentation
- **Ansible Tower Job** — Job type integration docs
- **Library Services** — Automation service integration management

### Other Tools
- **Boot Scripts (iPXE)** — Script management
- **Preseed Scripts** — Kickstart/preseed management
- **Catalog Item Types** — Self-service catalog type management

## Source Code

- Certs: `CertificateService`, `NsxtCertificateService`, `AmazonCertificateService`, `CertificateIntegrationExportService`
- DNS: `PluginDnsService`, `MorpheusDnsResolver`
- SCM: `GitCodeService`, `GithubCodeService`, `TerraformController`
- Provisioning: `ProvisioningLicensesController`, `ProvisioningSettingsController`
