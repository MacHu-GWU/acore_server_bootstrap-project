# -*- coding: utf-8 -*-

from pathlib import Path

_dir_here = Path(__file__).absolute().parent

path_20auto_upgrade_source = _dir_here / "20auto-upgrades"
path_20auto_upgrade_target = Path("/etc/apt/apt.conf.d/20auto-upgrades")
