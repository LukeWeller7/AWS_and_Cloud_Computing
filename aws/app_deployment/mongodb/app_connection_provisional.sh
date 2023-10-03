#!/bin/bash

export DB_HOST=mongodb://79.125.51.74:27017/posts

cd testing_scp_gitclone

cd app

npm install

node app.js
