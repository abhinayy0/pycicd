# from asyncio import subprocess
import subprocess, os

def poll():
    while True:
        subprocess.check_output("./update_repo.sh")

        if os.path.isfile(".commit_id"):
            