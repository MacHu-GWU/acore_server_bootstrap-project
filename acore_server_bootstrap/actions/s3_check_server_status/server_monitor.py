#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import subprocess

while 1:
    time.sleep(30)
    args = [
        # make sure this path matches the definition in
        # ``from acore_paths.api import path_acore_soap_app_cli``
        f"/home/ubuntu/git_repos/acore_soap_app-project/.venv/bin/acsoap",
        "canned",
        "measure-server-status",
    ]
    res = subprocess.run(args)
