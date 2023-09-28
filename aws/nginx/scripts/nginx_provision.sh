#!/bin/bash

# update
sudo apt update -y

# upgrade
sudo apt upgrade -y

# install nginx
sudo apt install nginx -y

# restart
sudo systemctl restart nginx

# enable nginx
sudo systemctl enable nginx
