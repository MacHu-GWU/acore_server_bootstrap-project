# -*- coding: utf-8 -*-

from light_emoji import common

from ...logger import logger
from ...logger_ubuntu import get_logger
from ...vendor.screen_session_manager import (
    run_script,
    stop_script,
)
from .paths import path_server_monitor_sh


@logger.start_and_end(msg="{func_name}")
def run_check_server_status_cron_job():
    """
    运行服务器状态健康检查定时脚本.
    """
    file_logger = get_logger()
    file_logger.debug(f"{common.play_or_pause} run {path_server_monitor_sh} in screen session")
    logger.info(f"run {path_server_monitor_sh} in screen session")
    run_script(path_server_monitor_sh, name="servermonitor", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def stop_check_server_status_cron_job():
    """
    停止服务器状态健康检查定时脚本.
    """
    stop_script(name="servermonitor", print_func=logger.info)
