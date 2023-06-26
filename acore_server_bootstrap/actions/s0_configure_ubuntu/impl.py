# -*- coding: utf-8 -*-

import subprocess

from ...logger import logger
from .paths import path_20auto_upgrade_source, path_20auto_upgrade_target


@logger.start_and_end(msg="{func_name}")
def disable_ubuntu_auto_upgrade():
    """
    关闭 Ubuntu 的自动更新. 主要是为了防止 Ubuntu 更新 MySQL Client 的小版本. 因为游戏服务器
    要求 MySQL Client 的版本跟服务器编译时的版本以及数据库的版本一摸一样.

    Reference:

    - https://askubuntu.com/questions/1322292/how-do-i-turn-off-automatic-updates-completely-and-for-real
    """
    logger.info(f"Apply changes to {path_20auto_upgrade_target}")

    args = [
        "sudo",
        "cp",
        f"{path_20auto_upgrade_source}",
        f"{path_20auto_upgrade_target}",
    ]
    subprocess.run(args, check=True)
