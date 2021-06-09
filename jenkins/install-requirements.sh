#!/bin/bash

sudo apt update
sudo apt install -y curl jq

# Install docker
curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins

# Install docker-compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install ansible
# mkdir -p ~/.local/bin
# echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
# source ~/.bashrc
# sudo apt install python3-pip -y
# pip3 install --user ansible
# ansible --version
sudo apt-get update 
sudo apt-get install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install ansible -y

# Docker login
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD