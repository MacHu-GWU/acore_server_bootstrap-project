# -*- coding: utf-8 -*-

from ...logger import logger
from ...vendor.screen_session_manager import (
    run_script,
    stop_script,
)
from .paths import path_server_monitor_py


@logger.start_and_end(msg="{func_name}")
def run_check_server_status_cron_job():
    """
    运行服务器状态健康检查定时脚本.
    """
    logger.info(f"run {path_server_monitor_py} in screen session")
    run_script(path_server_monitor_py, name="servermonitor", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def stop_check_server_status_cron_job():
    """
    停止服务器状态健康检查定时脚本.
    """
    stop_script(name="servermonitor", print_func=logger.info)
