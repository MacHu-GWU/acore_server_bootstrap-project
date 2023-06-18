# -*- coding: utf-8 -*-

from ...logger import logger
from .paths import path_20auto_upgrade_source, path_20auto_upgrade_target


@logger.start_and_end(msg="{func_name}")
def disable_ubuntu_auto_upgrade():
    logger.info(f"Apply changes to {path_20auto_upgrade_target}")
    path_20auto_upgrade_target.write_text(path_20auto_upgrade_source.read_text())
