#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a automation script that run the ``acsoap`` cli command
to check the server status and update EC2 tags every 30 seconds.

This script will be run as a cron job in ``screen``.
"""

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
