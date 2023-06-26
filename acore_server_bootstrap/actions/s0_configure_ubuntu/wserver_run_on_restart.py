#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# --- run check server status cron job
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_check_server_status_cron_job",
]
subprocess.run(args)

# --- run wow server
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_server",
]
subprocess.run(args)
