
# Auto-commit Github program

This Python script automates the creation of a fake commit history in a Git repository. ***EDUCATIONAL PURPOSE ONLY***.

## Features

- **Daily Random Commit Generation**: The script creates a random number of commits for each of the last 365 days, creating a consistent (kinda) contribution history.
- **Interactive User Setup**: The program prompts users for their Git username, email, repository location, and branch name.
- **Automatic Push to GitHub**: Each generated commit is pushed to the specified GitHub repository branch, *updating the contribution graph!!!!*. AND IT LOOKS ORGANIC!


## Requirements

- **Python 3.6+**
- **Git installed** on the system.
- **Python modules**: `os` `subprocess` `random` `datetime`
## Usage

1. **Clone or Download** this script to your local machine.
2. **Have a Github repo** ready to be auto-commited.
3. **Navigate** to the directory containing the script.
4. **Run the program** using the command below:

```bash
python auto_commit_bot.py
```
### Interaction

```bash
Enter the path to your Git repo. (e.g., /home/username/path/to/repo): /home/user/my-repo

Enter the branch name to push to (default: main): 

Enter a percentage of days to skip. e.g., 50 for 50% (default: 20%): 30

The percentage of days with 0 commits is set: 0.3

Enter your Git username: your-username

Enter your Git email: your-email@example.com
```