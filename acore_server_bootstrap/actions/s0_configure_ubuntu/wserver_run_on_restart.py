#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# --- test
# uncomment the following lines to test this script
# import random
# p = Path("/home/ubuntu/wserver_run_on_restart_test.txt")
# p.write_text(str(random.randint(1, 100)))

# --- configure db
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "configure_db",
]
subprocess.run(args)

# --- apply server config
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "apply_server_config",
]
subprocess.run(args)

# todo: the run_check_server_status_cron_job is no longer needed, consider remove it in the next release
# --- run check server status cron job
# args = [
#     "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
#     "run_check_server_status_cron_job",
# ]
# subprocess.run(args)

# --- run log to ec2 tag cron job
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_log_to_ec2_tag_cron_job",
]
subprocess.run(args)

# --- run measure worldserver cron job
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_measure_worldserver_cron_job",
]
subprocess.run(args)

# --- run wow server
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_server",
]
subprocess.run(args)
