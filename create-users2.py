#!/usr/bin/python3

# INET4031
# Trent
# Date Last Modified: 3/22/2026

# os: used to execute system commands
# re: searches for patterns in text
# sys: reads input from the terminal
import os
import re
import sys

def main():
    # Ask the user if they want to run in dry-run mode or for real
    dry_run = input("Run in dry-run mode? (Y/N): ")

    for line in sys.stdin:

        # Checks if the line starts with "#", if so, it is a comment and not user data.
        match = re.match("^#", line)

        # Removes extra whitespace and splits the line using ":" as the divider.
        fields = line.strip().split(':')

        # Skip this line if it is a comment or does not have exactly 5 fields.
        # You need exactly 5 fields to create a user account properly.
        if match or len(fields) != 5:
            # In dry-run mode, print out why the line was skipped
            if dry_run == 'Y':
                if match:
                    print("==> Skipping commented line: %s")
                else:
                    print("==> Skipping line, not enough fields: %s")
            continue

        # Pull out each piece of user info from the fields.
        # gecos is the full name format Linux uses when creating accounts.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # A user can be in multiple groups, so split them by comma into a list.
        groups = fields[4].split(',')

        # Lets the admin know we are creating an account for this user.
        print("==> Creating account for %s..." % (username))

        # Builds the command to create the user account with their full name and no password prompt.
        # cmd will contain the full adduser command string and is ready to run.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # In dry-run mode, print the command but do not run it.
        # In real mode, run the command to actually create the account.
        print(cmd)
        if dry_run == 'N':
            os.system(cmd)

        # Lets the admin know we are setting the password for this user.
        print("==> Setting the password for %s..." % (username))

        # Builds the command to set the user's password.
        # It sends the password twice for confirmation and sets it without any user interaction.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # In dry-run mode, print the command but do not run it.
        # In real mode, run the command to actually set the password.
        print(cmd)
        if dry_run == 'N':
            os.system(cmd)

        for group in groups:
            # If group is '-' it means no group was assigned, so skip it.
            # If group is anything else, the user belongs to that group and we add them to it.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # In dry-run mode, print the command but do not run it.
                # In real mode, run the command to actually add the user to the group.
                print(cmd)
                if dry_run == 'n':
                    os.system(cmd)

if __name__ == '__main__':
    main()