# Using scp 

```
 scp -i "C:/Users/lukew/.ssh/tech254.pem" -r app ubuntu@ec2-3-252-144-157.eu-west-1.compute.amazonaws.com:~
```
- scp - Secure copy 
- -i indentify
- "C:/Users/lukew/.ssh/tech254.pem" - file path for .pem used for instance
- -r 
- app - file you want to copy
- ubuntu@ec2-3-252-144-157.eu-west-1.compute.amazonaws.com:~ - copies to the instance



# Using git clone

```
sudo apt install git-all
```

```
git clone [repo-url]
```


# Install nodejs
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```
This command finds the pacific version of nodejs, otherwise when you still it, it will try and install the lastest version
```
sudo apt install nodejs -y
```
This command installs nodejs
```
node -v
```
This command shows the version of node being used.
```
sudo npm install pm2 -g
```
npm - node packet manager  
nodes version of pip  
pm2 - process manager, manager for node processes, easier to manage the processors used by nodejs  
https://www.vultr.com/docs/how-to-manage-node-applications-with-pm2/

# Running the app

```
npm install 
```

```
node app.js
```

In AWS you need to add port range 3000 to inbound security group
