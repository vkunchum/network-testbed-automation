#!/bin/bash

# Update and install required packages
sudo apt update
sudo apt install -y prometheus grafana

# Enable and start Prometheus
  sudo systemctl enable prometheus
  sudo systemctl start prometheus

# Enable and start Grafana
  sudo systemctl enable grafana-server
  sudo systemctl start grafana-server

# Confirm installation
  systemctl status prometheus
  grafana-server -v
