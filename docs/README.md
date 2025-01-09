## Project: Automated Network Testbed with Performance Monitoring

### 1. Project Architecture Design

**Objective:**
Design a scalable virtual network environment to simulate enterprise-level networking scenarios. This network will include DNS, DHCP, firewall configurations, and automated deployment scripts. The system will also integrate performance monitoring and debugging tools to ensure real-time observation of network traffic and performance bottlenecks.

### 2. Network Architecture Overview

**Topology:**
- Core Network (Simulated Data Center)
- Firewall (pfSense or UFW)
- DHCP Server
- DNS Server
- Monitoring Node (Prometheus + Grafana)
- Client Nodes (Virtual Machines or Containers)

**Virtualization Tools:**
- VirtualBox / VMware Workstation for virtual environments
- GNS3 for network emulation (optional)

**Automation Tools:**
- Python for scripting network automation and deployments
- Ansible for configuration management (firewall rules, DHCP, DNS)

**Monitoring Tools:**
- Prometheus (data scraping and monitoring)
- Grafana (visualization and dashboards)
- Wireshark (network packet capture and analysis)

### 3. Network Diagram (Description)
The testbed consists of a core data center with a pfSense firewall protecting internal virtual machines. DNS and DHCP services run on separate virtual machines to provide essential network services. The monitoring node collects metrics from client machines, and dashboards visualize real-time traffic.

**Components:**
- **Firewall:** Controls inbound/outbound traffic with custom rules.
- **DNS Server:** Resolves hostnames to IP addresses.
- **DHCP Server:** Dynamically assigns IP addresses to clients.
- **Monitoring Node:** Collects network metrics and system performance data.
- **Clients:** Test machines running various network simulations.

### 4. Network Diagram

![Network Architecture Diagram](diagrams/network_architecture.png)

### 5. Diagram Legend
- **Blue Lines:** Internal traffic within the testbed
- **Red Lines:** Firewall boundaries
- **Dashed Lines:** Monitoring and logging traffic

### 6. Repository Structure

network-testbed-automation/
├── scripts/
│   ├── deploy_network.py  # Automates VM deployment
│   ├── configure_firewall.yml  # Ansible playbook for firewall config
│   └── monitor_setup.sh  # Bash script for monitoring tool setup
├── configs/
│   ├── dns_config.conf  # DNS server configuration
│   ├── dhcp_config.conf  # DHCP server configuration
│   └── firewall_rules.conf  # Firewall rule definitions
├── diagrams/
├── docs/
│   ├── PROJECT_REPORT.md
│   ├── README.md
│   └── DEPLOYMENT_GUIDE.md
└── performance_reports/


### Deployment Guide

#### Prerequisites
- VirtualBox or VMware Workstation installed.
- Python 3.x and Ansible installed on the control node.
- SSH access configured for target machines.




