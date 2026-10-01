import subprocess
import os
import sys

from dotenv import load_dotenv
load_dotenv()

user = os.getenv ("GITHUB_USER")
repo = os.getenv ("GITHUB_REPO")
token = os.getenv ("GITHUB_TOKEN")

if not (user and repo and token):
    sys.exit("Set GITHUB_USER, GITHUB_REPO and GITHUB_TOKEN in .env")

url = f"https://{user}:{token}@github.com/{user}/{repo}.git"

for cmd in (
    ["git", "init"],
    ["git", "add", "."],
    ["git", "commit", "-m", "First commit"],
    ["git", "remote", "add", "origin", url],
    ["git", "branch", "-M", "main"],
    ["git", "push", "url", "main"],
):
    subprocess.run(cmd)
    
