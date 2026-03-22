# INET4031 - Add User Script

## Description
A Python script that automates creating user accounts and adding them to groups on a Linux system using an input file.

## Files
- `create-users.py` - The main script
- `create-users.input` - The list of users to create

## Input File Format
Each line needs exactly 5 fields separated by `:`
```
username:password:lastname:firstname:group(s)
```
- Use a comma to put a user in multiple groups
- Use `-` if the user has no group
- Add `#` at the start of a line to skip it

## How to Run

Dry run (no changes made):
```bash
./create-users.py < create-users.input
```

Real run (actually creates accounts):
```bash
sudo ./create-users.py < create-users.input
```

## Author
Trent - INET4031
