Ansible Role: Docker Swarm
==========================

This role is used to install docker swarm on multi-hosts as follows:

1. create 3 virtual/physical machines

2. install the following packages

```
	# generate rsa public/private key pair for each machine
	ssh-keygen -t rsa	
	# update hosts list on virtual machine
	vi /etc/hosts
	# copy ssh keys to remote hosts
	ssh-copy-id host1
	ssh-copy-id host2
	ssh-copy-id host3
	
	# install the following packages
	sudo apt-get install jq

	# update the inventory file with new hosts
	vi inventory
	
	# install ansible on master node
	sudo apt-get update
	sudo apt-get install libffi-dev
	sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
	sudo pip install cryptography==1.5
	sudo pip install ansible
	
	# change directory to the parent directory
	cd ..

	# call ansible to execute the playbook	
	ansible-playbook -h ansible/inventory ansible-dockerswarm/playbook.yml -vvvv
``` 
Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
