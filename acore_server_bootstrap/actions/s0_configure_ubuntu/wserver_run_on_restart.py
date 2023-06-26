#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from pathlib import Path

p = Path("/home/ubuntu/wserver_run_on_restart_test.txt")
p.write_text(str(random.randint(1, 100)))
