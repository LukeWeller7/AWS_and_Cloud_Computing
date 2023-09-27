# Basics on Linux

### Key Information
- bash 
  - born again shell 
  - determined with prefix $
  - a shell is an interface that allows you to run commands 
  - bash is known as the default shell
- Everything in Linux is either a file or folder
- In Linux, it is case-sensitive 
## Key Commands
### Basic Information
```
uname
```
This command is used to show the operating system that is in use.
```
uname -a
```
This command is used to show all information on the Operating system.
```
uname -p
```
This command is used to show information on the processor that is in use.
```
whoami
```
This command shows you the name of the user (Typically Ubuntu)
```
history
```
This command shows the history of the last 500 commands used on this system
```
history -c
```
Use this command to clear the history of commands use, main use of this is to remove any commands that contain passwords or sensitive information
### File commands
```
curl
```
This command is used to copy and transfer data from a given source. An example of this is shown below:
```
curl https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg --output cat.jpg
```
This example command consists with the first argument being the url/source of the data you want to copy, followed by the action which will be output, meaning you want to output what was just copied into the final argument being the location of the data tansfer.
```
mv
```
This command moves files. An example is given:
```
mv cat.jpg cat
```
What this command has done is move the file noted as the first argument and moved it into a file called after the second argument
```
file
```
This command outputs the type of file that is contained within the contents, even if the file is named differently.
```
cp
```
This command copies, taking the first argument, coping the contents and outputting a new file named after the second argument
```
rm 
```
This command removes the file named in the first argument (be careful as it doesn't ask for confirmation)
```
touch
```
This command creates a blank file named after first argument
```
nano
```
This command allows you to change the contents of a file
```
head -2 chicken-joke.txt
```
This command takes the top number of lines stated in argument one out of the file stated in argument two
```
tail -2 chicken-joke.txt
```
This command takes the bottom number of lines stated in argument one out of the file stated in argument two. This is useful for extracting the most recent data in a file as well as extracting last few lines of error codes instead of the while file.
```
nl
```
This command shows the contents of the file stated in argument one, as well as the number of lines (excluding blank space)
```
cat chickem-joke.txt | grep chicken
```
This command prints out any lines in txt file that contain the argument after grep and highlights. The pipe `|` allows you to chain commands together.
### Directory Commands
```
rm -r
```
This commands removes the directory named in each following argument
```
mkdir
```
This command makes directories names after the following arguments (spaces separate directories)
```
tree
```
This command needs to be installed via `sudo apt install tree` but it gives a working file order of current directory
```
cd /
```
This commands changes you to the root directory
### Terminal commands
```
clear
```
This command clears out the directory
```
sudo
```
This command stands for Super user do, meaning you can have extra permissions (be careful)
```
sudo su
```
This command turns on sudo for foreseeable future until you use `exit`
```
exit
```
This command allows you to exit sudo, but also will exit you out of instance connection if not in sudo.

