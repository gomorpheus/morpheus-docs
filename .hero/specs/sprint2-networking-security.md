---
type: initiative
status: planning
horizon: now
title: "Sprint 2: Networking & Security Deep Dive"
tags: [9.0.0, networking, security, sprint-2]
priority: 2
---

# Sprint 2: Networking & Security Deep Dive

## Priority: HIGH — Large Undocumented Surface Area

The networking subsystem has extensive capabilities (DHCP servers, security servers, BGP, edge clusters, switches, scopes) that are entirely undocumented. These are critical for VMware-to-HVM migrations where operators need to replicate complex network topologies.

## Scope

### Network Services (New Pages)
- DHCP Servers — Full CRUD management
- DHCP Relays — Standalone relay management
- Network Switches — Switch management under network servers
- Edge Clusters — Network server edge cluster management
- Network Scopes — Server scope management

### Network Security (New Section)
- Security Servers — Commit workflows, security profiles
- Security Endpoints — Endpoint management
- Security Roles — Role-based network security
- Security Zones — Zone configuration

### Router Advanced Features (Expand Existing)
- BGP Neighbors — Full CRUD for BGP configuration
- Route Redistributions — Redistribution management
- DHCP Bindings — Static bindings on routers
- Application Ports — Port management
- Router Certificates — Certificate management

### Network Integrations (New Guides)
- NSX-T — Full integration guide (module exists, no guide)
- Cisco ACI — Configuration guide
- Palo Alto — Integration guide

## Source Code

- `NetworkDhcpServersController`, `NetworkDhcpRelaysController`
- `NetworkSecurityServersController`, `SecurityEndpointsController`, `SecurityRolesController`, `SecurityZonesController`
- `NetworkRouterBgpNeighborsController`, `NetworkRouterRouteRedistributionsController`
- `AciNetworkService`, `PaloAltoNetworkService`
- `clouds/nsxt/` module
