#### Deployment Steps
1. Clone the repository:
   
   git clone https://github.com/username/network-testbed-automation.git
   cd network-testbed-automation
   

2. Create an inventory file for Ansible:
   
   [network_lab]
   192.168.1.10 ansible_user=root ansible_ssh_pass=password
   192.168.1.11 ansible_user=root ansible_ssh_pass=password
   

3. Deploy virtual machines:
  
   python3 scripts/deploy_network.py


4. Configure DNS, DHCP, and firewall rules:
 
   ansible-playbook -i inventory.ini scripts/configure_firewall.yml


5. Install Prometheus and Grafana for monitoring:
  
   bash scripts/monitor_setup.sh
 

#### Verification
- **Firewall:**

  sudo ufw status

  Ensure necessary ports (22, 53, 67, 80, 443) are open.

- **DNS:**
 
  dig example.com

  Ensure DNS queries resolve correctly.

- **DHCP:**

  journalctl -u isc-dhcp-server

  Verify that clients are receiving IP addresses.

- **Monitoring Tools:**
  Access Grafana dashboards at `http://<monitoring_node_ip>:3000`.

#### Troubleshooting
- **Firewall Rules Not Applied:** Re-run the playbook and check the UFW status.
- **DNS Resolution Issues:**
    Inspect logs with `journalctl -u bind9`.
- **DHCP Service Issues:** Restart the DHCP server:
    sudo systemctl restart isc-dhcp-server

