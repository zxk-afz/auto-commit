import os
import subprocess
import random
import datetime

REPO_PATH = ''
GIT_USERNAME = ''
GIT_USER_EMAIL = ''
BRANCH_NAME = ''
DAY_TO_SKIP = 0.2

# Execute Git command
def exec_git_command(command):
    try:
        print(f"Executing command: {command} in {REPO_PATH}")
        subprocess.check_call(command, shell=True, cwd=REPO_PATH)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    return True

# Set Git users
def set_git_user():
    global GIT_USERNAME, GIT_USER_EMAIL

    GIT_USERNAME = input("Enter your Git username: ")
    GIT_USER_EMAIL = input("Enter your Git email: ")

    print(f"Setting Git user for repo at: {REPO_PATH}")

    exec_git_command(f"git config user.name '{GIT_USERNAME}'")
    exec_git_command(f"git config user.email '{GIT_USER_EMAIL}'")

# Create commit
def create_commit(date):
    commit_message = "Random commit :)"
    # Random num of lines - for contribution :)
    num_lines = random.randint(1, 7)
    commit_file = os.path.join(REPO_PATH, "random_commit.txt")

    # Write the lines
    with open(commit_file, "w") as f:
        for _ in range(num_lines):
            f.write(f"Random commit on {date.strftime('%Y-%m-%d')}\n")

    exec_git_command(f"git add {commit_file}")
    exec_git_command(f"git commit --date='{date.strftime('%Y-%m-%d %H:%M:%S')}' -m '{commit_message}'")

# Main function (fake auto-commit bot)
def fake_commit_bot():
    global REPO_PATH, BRANCH_NAME, DAY_TO_SKIP

    REPO_PATH = input("Enter the path to your Git repo. (e.g: /home/username/path/to/repo): ")
    BRANCH_NAME = input("Enter the branch name to push to (default: main): ") or "main"

    print(f"Repository path: {REPO_PATH}")
    # Percentage of days to skip
    DAY_TO_SKIP = input("Enter a percentage of days to skip. e.g., 50 for 50% (default: 20): ") or 20
    
    try:
        # Convert to a float
        DAY_TO_SKIP = float(DAY_TO_SKIP) / 100  # Convert to value between 0 and 1
        print(f"The percentage of days with 0 commits is set: {DAY_TO_SKIP * 100}%")
    except ValueError:
        print("That's not a valid percentage.")

    # Set Git user info
    set_git_user()

    today = datetime.date.today()
    for day_offset in range(365):
        commit_date = today - datetime.timedelta(days=day_offset)
        
        # Skip days
        if random.random() < DAY_TO_SKIP:
            continue
        
        # Choose random number between 1 - 8 commits
        num_commits = random.randint(1, 8)
        for _ in range(num_commits):
            create_commit(commit_date)

    print("Pushing all commits...")
    exec_git_command(f"git push origin {BRANCH_NAME}")
    print("\nFinished pushing all the commits, thank me later ;)")

if __name__ == "__main__":
    try:
        fake_commit_bot()
    except KeyboardInterrupt:
        print("\n\nProgram was cancelled :(")
