# Kubernetes the Hard Way – Automated with Ansible

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Ansible](https://img.shields.io/badge/Ansible-Automation-green.svg)](https://www.ansible.com/)  
[![Kubernetes](https://img.shields.io/badge/Kubernetes-The%20Hard%20Way-orange.svg)](https://github.com/kelseyhightower/kubernetes-the-hard-way)

Automated deployment of **Kubernetes The Hard Way** using **Ansible** + **Vagrant** + **VirtualBox**.  
This project simplifies the original manual steps while preserving the educational experience.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Python Virtual Environment & Ansible](#python-virtual-environment--ansible)
- [Running the Cluster](#running-the-cluster)
- [Certificates](#certificates)
- [Cluster Access](#cluster-access)
- [License](#license)

---

## Overview
This repository is based on the original [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) guide.  
Changes and improvements:
- All Bash commands converted to **Ansible**.
- Added separate certificates for **etcd nodes**.
- Increased **etcd cluster size** from 1 to 3 nodes.

---
## Prerequisites
Tested on: **MacBook Pro 2020 (M1, 16 GB RAM)**  

Install:
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://developer.hashicorp.com/vagrant/install)  

Or via Homebrew:  
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/hashicorp-vagrant
```
---
## Setup
### Python Virtual Environment & Ansible

Create and activate a Python virtual environment, then install Ansible and required dependencies:
```
mkdir -p ~/work/venv_ansible
python3 -m venv ~/work/venv_ansible
source ~/work/venv_ansible/bin/activate
pip install ansible netaddr kubernetes
```

---

## Running the Cluster

### 1. Start Virtual Machines

Vagrant will create **6 virtual machines**:
- **3 Kubernetes control plane + etcd server nodes** (1 GB RAM each)
- **3 worker nodes** (2 GB RAM each)
```
vagrant up
```

### 2. Run the Ansible Playbook

Once the VMs are up and running, deploy everything with Ansible:
```
ansible-playbook -i inventory/kubernetes-local.yml kubernetes.yml
```

### 3. Run Specific Tags

If a section of the playbook fails or you want to run only a part of it, use tags:
```
ansible-playbook -i inventory/kubernetes-local.yml kubernetes.yml -t certificates
ansible-playbook -i inventory/kubernetes-local.yml kubernetes.yml -t server
ansible-playbook -i inventory/kubernetes-local.yml kubernetes.yml -t etcd
ansible-playbook -i inventory/kubernetes-local.yml kubernetes.yml -t kubernetes
```

---

### Certificates

All certificates and the `admin.kubeconfig` file are stored in the `files/` folder.  

---

### Cluster Access
You can access the cluster with:
```
kubectl --kubeconfig files/admin.kubeconfig get pods
```

- **Kubernetes API:** https://127.0.0.1:16443
- **First Vagrant node ports:** 8080 and 8443
- **Nginx pod available at:** http://localhost:8080

---
