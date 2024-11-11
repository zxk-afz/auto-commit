# This is a python bot to auto push commits on github

import os
import subprocess
import random
import datetime
import time

# Informations
REPO_PATH = ''
GIT_USERNAME = ''
GIT_USER_EMAIL = ''
BRANCH_NAME = ''

# Exec git commands
def execGitCommand(command):
    try:
        subprocess.check_call(command, shell=True, cwd=REPO_PATH)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    return True

# Set git user details
def setGitUser():
    execGitCommand(f"git config user.name '{GIT_USERNAME}'")
    execGitCommand(f"git config user.email '{GIT_USER_EMAIL}'")

# Create random commit
def createCommit(date):
    commitMessage = f'Random commit :)'

    # Random number lines
    numLines = random.randint(1, 7)
    commitFile = os.path.join(REPO_PATH, "Random commit.txt")

    with open(commitFile, "w") as f:
        for _ in range(numLines):
            f.write(f"Random commit on {date.strftime('%Y-%m-%d')}\n")

    # Add changes staging area & commit
    execGitCommand(f"git add {commitFile}")
    execGitCommand(f"git commit --date='{date.strftime('%Y-%m-%d %H:%M:%S')}' -m '{commitMessage}'")

# Push to repo

