# INET4031 - Add User Script

## Description
A Python script that automates the creation of user accounts and group assignments on a Linux system. Instead of manually adding each user one by one, this script reads from an input file and creates all the accounts automatically.

## Files
- `create-users.py` - The main Python script that creates user accounts
- `create-users.input` - The input file containing the list of users to create

## Input File Format
Each line in the input file must have exactly 5 fields separated by a colon `:`
```
username:password:lastname:firstname:group(s)
```
Example:
```
user01:pass01:Last01:First01:group01
user02:pass02:Last02:First02:group01,group02
user03:pass03:Last03:First03:-
```
- A user can belong to multiple groups, separated by a comma
- A `-` in the groups field means no group assignment
- Lines starting with `#` are skipped

## How to Run

### Dry Run (test without making changes)
Make sure `print(cmd)` is uncommented and `os.system(cmd)` is commented out, then run:
```bash
./create-users.py < create-users.input
```

### Real Run (actually creates accounts)
Uncomment all `os.system(cmd)` lines, then run:
```bash
sudo ./create-users.py < create-users.input
```

## Verify Users Were Created
```bash
grep user0 /etc/passwd
grep user0 /etc/group
```

## Author
Trent  
INET4031
