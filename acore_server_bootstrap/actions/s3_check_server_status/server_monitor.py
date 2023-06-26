#!/home/ubuntu/git_repos/acore_soap_app-project/.venv/bin/python

import time
import subprocess
from acore_paths.api import path_acore_soap_app_cli

while 1:
    time.sleep(30)
    args = [
        f"{path_acore_soap_app_cli}",
        "canned",
        "measure-server-status",
    ]
    res = subprocess.run(args, capture_output=True, check=False)
