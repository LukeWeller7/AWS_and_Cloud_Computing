HA-SC (High Ability - SCalability)
AZ - Availability zone (usually 3 sometimes 4 in regions)
scaling policy - threshold condition 
```
sudo apt-get install stress

stress --cpu 1 --timeout 20
```
- cpu 1 - how many cpus to target
- Timeout the duration of the stress test
load-balancer - main entry point for users, it distributes the users to different vm

subnet will determine the availability zone, we don't want this as we want to slipt accross all three
