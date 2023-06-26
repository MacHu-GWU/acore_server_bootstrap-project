#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import subprocess
from pathlib import Path

# --- test
p = Path("/home/ubuntu/wserver_run_on_restart_test.txt")
p.write_text(str(random.randint(1, 100)))

# --- run check server status cron job
p = Path("/home/ubuntu/wserver_run_on_restart_test.log.txt")
lines = list()
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_check_server_status_cron_job",
]
res = subprocess.run(args, capture_output=True)
lines.append(res.stderr.decode("utf-8"))
lines.append(res.stdout.decode("utf-8"))

# --- run wow server
args = [
    "/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs",
    "run_server",
]
res = subprocess.run(args, capture_output=True)
lines.append(res.stderr.decode("utf-8"))
lines.append(res.stdout.decode("utf-8"))
p.write_text("\n".join(lines))