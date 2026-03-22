# INET4031 - Add User Script

## Description
Adding user accounts to a Linux server one by one can take a long time and it is easy to 
make mistakes, especially when you need to add a lot of users at once. This Python script 
makes that process much easier. It reads from a simple input file and automatically creates 
every user account, sets their password, and adds them to the right groups. This makes 
setting up a server faster and less stressful, without having to manually add each user 
one at a time.

## Files
- `create-users.py` - The main Python script that reads the input file and creates the user accounts
- `create-users.input` - The input file that holds the list of users and groups to add
- `README.md` - Documentation for the project

## Input File Format
Each line in the input file is one user. Each line must have exactly 5 pieces of information 
separated by a colon. The order is username, password, lastname, firstname, and groups.

Rules for the input file:
- If a user belongs to more than one group, separate the group names with a comma
- If a user does not belong to any group, put a dash as a placeholder
- If you want to skip a user without removing them from the file, put a # at the start of their line
- Any line that does not have exactly 5 fields will automatically be skipped

## How to Run

### Step 1 - Make the Script Executable
Before running the script for the first time, you need to give it permission to run:
```
chmod +x create-users.py
```

### Step 2 - Dry Run
Always do a dry run before running the script for real. A dry run goes through all the 
steps and prints out what it would do, without actually making any changes to the server. 
This is a good way to catch mistakes before they cause problems. Make sure print(cmd) is 
uncommented and os.system(cmd) is commented out in all 3 places in the code, then run:
```
./create-users.py < create-users.input
```

### Step 3 - Real Run
Once the dry run looks good, uncomment all 3 os.system(cmd) lines in the script. 
Then run it with sudo so the script has the right permissions to create accounts on the server:
```
sudo ./create-users.py < create-users.input
```

## Verifying Users Were Created
After running the script you can check that everything was created correctly by searching 
through the system files with these commands:
```
grep user0 /etc/passwd
grep user0 /etc/group
```
The /etc/passwd file is where Linux keeps track of all user accounts on the system. 
The /etc/group file is where Linux keeps track of all groups and who is in them. 
If the script ran correctly, you should see all your users and their groups in the output.

## Troubleshooting
- If you get a Permission Denied error, make sure you ran chmod +x on the script
- If a user is missing, check that their line in the input file has exactly 5 fields
- If something was added incorrectly, you will need to manually remove the user with 
  the deluser command before running the script again

## Author
Trent - INET4031
