import os
import subprocess
import random
import datetime
import time

REPO_PATH = ''
GIT_USERNAME = ''
GIT_USER_EMAIL = ''
BRANCH_NAME = ''

# Execute Git commands
def exec_git_command(command):
    try:
        subprocess.check_call(command, shell=True, cwd=REPO_PATH)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    return True

# Set user info
def set_git_user():
    global GIT_USERNAME, GIT_USER_EMAIL

    GIT_USERNAME = input("Enter your Git username: ")
    GIT_USER_EMAIL = input("Enter your Git email: ")

    exec_git_command(f"git config user.name '{GIT_USERNAME}'")
    exec_git_command(f"git config user.email '{GIT_USER_EMAIL}'")

# Create commit
def create_commit(date):
    commit_message = "Random commit :)"
    num_lines = random.randint(1, 7)
    commit_file = os.path.join(REPO_PATH, "random_commit.txt")

    with open(commit_file, "w") as f:
        for _ in range(num_lines):
            f.write(f"Random commit on {date.strftime('%Y-%m-%d')}\n")

    exec_git_command(f"git add {commit_file}")
    exec_git_command(f"git commit --date='{date.strftime('%Y-%m-%d %H:%M:%S')}' -m '{commit_message}'")

# Push commit
def push_commit():
    exec_git_command(f"git push origin {BRANCH_NAME}")

#  Main function
def fake_commit_bot():
    global REPO_PATH, BRANCH_NAME

    REPO_PATH = input("Enter the path to your Git repository: ")
    BRANCH_NAME = input("Enter the branch name to push to (default: main): ") or "main"
    set_git_user()

    today = datetime.date.today()
    for day_offset in range(365):
        commit_date = today - datetime.timedelta(days=day_offset)
        print(f"Creating commit for {commit_date}")

        create_commit(commit_date)
        push_commit()
        
        time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    fake_commit_bot()
