import subprocess
import os
import sys
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("GITHUB_USER")
repo = os.getenv("GITHUB_REPO")
token = os.getenv("GITHUB_TOKEN")

if not (user and repo and token):
    sys.exit("Set GITHUB_USER, GITHUB_REPO and GITHUB_TOKEN in .env")

url = f"https://{user}:{token}@github.com/{user}/{repo}.git"

# subprocess.run(["git", "add", "."])
# subprocess.run(["git", "commit", "-m", "Update"])
# subprocess.run(["git", "branch", "-M", "main"])
# subprocess.run(["git", "push", url, "main"], check=True)
""" either we can use above commands or we can also use a 
loop to run the commands in sequence as it is written below i.e
 for cmd in) """


for cmd in (
    ["git", "init"],
    ["git", "add", "."],
    ["git", "commit", "-m", "Update"],
    ["git", "branch", "-M", "main"],
    ["git", "push", url, "main"],
):
    subprocess.run(cmd)