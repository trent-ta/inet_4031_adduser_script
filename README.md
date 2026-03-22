# INET4031 - Add User Script

## Description
Managing user accounts on a Linux server manually can be time consuming and error prone, 
especially when you need to add dozens or even hundreds of users at once. This Python script 
solves that problem by automating the entire process. It reads from a structured input file 
and automatically handles account creation, password setup, and group assignments for every 
user in the file. This makes it easy to set up multiple servers consistently and efficiently 
without having to touch each account individually.

## Files
- `create-users.py` - The main Python script that reads the input file and creates user accounts
- `create-users.input` - The input file containing the list of users and groups to add to the system
- `README.md` - Documentation for the project

## Input File Format
Each line in the input file represents one user and must have exactly 5 fields separated by 
a colon. The fields in order are username, password, lastname, firstname, and groups.

Rules for the input file:
- If a user belongs to multiple groups, separate the group names with a comma
- If a user has no group assignment, use a dash as a placeholder
- If you want to skip a user without deleting them from the file, add a # at the start of their line
- Any line that does not have exactly 5 fields will automatically be skipped by the script

## How to Run

### Step 1 - Make the script executable
Before running the script for the first time, you need to give it permission to execute:
```
chmod +x create-users.py
```

### Step 2 - Dry Run
Always do a dry run before running the script for real. A dry run runs all of the logic 
and prints out what commands would be executed without actually making any changes to the 
system. This lets you catch and fix any errors before they cause problems on the server. 
Make sure print(cmd) is uncommented and os.system(cmd) is commented out in all 3 places, then run:
```
./create-users.py < create-users.input
```

### Step 3 - Real Run
Once the dry run looks correct, uncomment all 3 os.system(cmd) lines in the script. 
Then run it with sudo so the script has the proper admin permissions to create accounts:
```
sudo ./create-users.py < create-users.input
```

## Verifying Users Were Created
After running the script you can confirm that the user accounts and group memberships were 
created correctly by using the grep command to search through the system files:
```
grep user0 /etc/passwd
grep user0 /etc/group
```
The /etc/passwd file stores all user account information on the system. The /etc/group file 
stores all group memberships. If the script ran correctly, you should see all of your users 
and their group assignments in the output.

## Troubleshooting
- If you get a Permission Denied error, make sure you ran chmod +x on the script
- If a user is missing from the output, check that their line in the input file has exactly 5 fields
- If the script added something incorrectly, you will need to manually remove the user with 
  the deluser command before running the script again

## Author
Trent - INET4031
