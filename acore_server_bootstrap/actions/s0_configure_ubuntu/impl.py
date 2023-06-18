# -*- coding: utf-8 -*-

import subprocess

from ...logger import logger
from .paths import path_20auto_upgrade_source, path_20auto_upgrade_target


@logger.start_and_end(msg="{func_name}")
def disable_ubuntu_auto_upgrade():
    logger.info(f"Apply changes to {path_20auto_upgrade_target}")

    args = [
        "sudo",
        "cp",
        f"{path_20auto_upgrade_source}",
        f"{path_20auto_upgrade_target}",
    ]
    subprocess.run(args, check=True)
