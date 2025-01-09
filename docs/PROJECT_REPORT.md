#### Objectives
- Design a scalable, automated network testbed.
- Implement core network services (DNS, DHCP, Firewall).
- Integrate monitoring tools to visualize and debug performance.

#### Implementation
- Virtual machines deployed using a Python script.
- Network services configured with Ansible for consistency and scalability.
- Monitoring set up with Prometheus and Grafana for real-time insights.

#### Testing Results
- Verified DNS query resolution with `dig`.
- Confirmed DHCP leases assigned dynamically to clients.
- Ensured firewall rules restricted/allowed traffic as expected.
- Visualized metrics on Grafana dashboards (CPU usage, traffic flow).

#### Challenges and Solutions
- **Issue:** Initial firewall rules blocked SSH access.
  **Solution:** Added explicit rules to allow SSH traffic on port 22.

- **Issue:** DHCP server misconfiguration caused lease failures.
  **Solution:** Corrected `dhcpd.conf` to match the network range.

#### Conclusion
This project successfully demonstrates the automation of network deployment and configuration. The monitoring tools provide real-time insights, making it a robust solution for testing and debugging networking scenarios.

#### Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes.


#### License
This project is licensed under the MIT License. See the LICENSE file for details.



