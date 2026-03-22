#!/usr/bin/python3

# INET4031
# Trent
# Date Last Modified: 3/19/2026

# os: used to execute system commands
# re: searches for patterns in text
# sys: reads inout from the terminal
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Checks if the line starts with "#", if so, it is a comment and not user data.
        match = re.match("^#",line)
        
        # Removes extra whitespace and splits the line using ":" as the divider.
        fields = line.strip().split(':')

        # Skip this line if it is a commnet or does not have aexactly 5 fields.
        # You need exactly 5 fileds to create a user account properly.
        if match or len(fields) != 5:
            continue

        # Pull out each piece of users info from the fields.
        # gecos is the full name format when creating accounts.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # A user can be in multiple groups, then splits them wiht a comma into a list.
        groups = fields[4].split(',')

        # Lets the admin know we are creating an account for this user.
        print("==> Creating account for %s..." % (username))
        
        # Builds the command to create the user account that uses their full name with no need of a password.
        # cmd will contain the full adduser command string and is ready to run.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # Use print(cmd) first to verify the command before running it.
        # Once it is verified, you should uncomment os.system(cmd) to actually create the account on the system.
        print(cmd)
        # os.system(cmd)

        # Lets the admin know we are setting the password for this user.
        print("==> Setting the password for %s..." % (username))
        
        # This builds the command to set the users password.
        # This sends the password twice to confirm it, and then sets it without any user interaction.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Same as previous one, Use print(cmd) first to verify the command before running it.
        # Once it is verified, you should uncomment os.system(cmd) to actually create the account on the system.
        print(cmd)
        # os.system(cmd)

        for group in groups:
            # The if group '-'  it means no group was assigned, so it skips it.
            # If group is anything else, the user belongs to that group and you add them to it.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                # os.system(cmd)

if __name__ == '__main__':
    main()
