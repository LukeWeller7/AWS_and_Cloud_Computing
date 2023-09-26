# Starting a new instance
- Starting in AWS Console
- In services, search and select EC2
  - This is what is used to create virtual desktops
- Clicking on instances to view instances
- Click on launch instances (Orange button)
- Going down to Name and tags, this is where you name your instances (Ensure they are named properly)
  - tech254_lukew_testvm
  - every resource should start with tech254_lukew
  - then an instance/ref after
- Application and OS Images (Amazon Machine Image)
  - When creating a virtual machine, need to create what the base template will be, what do you need already installed (operating system)
  - Quick start
  - Ubuntu
  - Ubuntu Server 20.04 LTS (HVM), SSD Volume Type (Free tier eligible) (**Always use unless told otherwise**)
- Instance Type
  - t2.micro (Free tier eligible) (**Always use unless told otherwise**)
- Key Pair (login)
  - tech254
- Network Settings
  - Edit
  - Security group name
    - tech254_lukew_testsg
- Configure Storage
  - Leave as default
- Advance Details
  - Leave as default
- Summary
  - Suma
- Launch Instance
  - Success

# To View running
- Go to Instances
- Type running to filter instance state

# To stop instances
- In instances
- click on the instance to stop
- Instance State
  - Terminate Instance
  - Terminate

