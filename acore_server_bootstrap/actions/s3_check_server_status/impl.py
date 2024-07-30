# -*- coding: utf-8 -*-

"""
todo: add docstring
"""

from light_emoji import common
from acore_paths.api import (
    path_log_to_ec2_tag_cron_job_script,
    path_measure_worldserver_cron_job_script,
)

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
    运行服务器状态健康检查定时脚本. 这个 cron job 的详细信息请参考
    `measure_server_status <https://acore-soap-app.readthedocs.io/en/latest/search.html?q=measure_server_status&check_keywords=yes&area=default>`_.
    """
    file_logger = get_logger()
    file_logger.debug(
        f"{common.play_or_pause} run {path_server_monitor_sh} in screen session"
    )
    logger.info(f"run {path_server_monitor_sh} in screen session")
    run_script(path_server_monitor_sh, name="servermonitor", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def stop_check_server_status_cron_job():
    """
    停止服务器状态健康检查定时脚本. 关闭由 :func:`run_check_server_status_cron_job` 启动的 cron job.
    """
    stop_script(name="servermonitor", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def run_log_to_ec2_tag_cron_job():
    """
    运行服务器状态监控定时脚本. 这个 cron job 的详细信息请参考 todo ...
    """
    file_logger = get_logger()
    file_logger.debug(
        f"{common.play_or_pause} run {path_log_to_ec2_tag_cron_job_script} in screen session"
    )
    logger.info(f"run {path_log_to_ec2_tag_cron_job_script} in screen session")
    run_script(
        path_log_to_ec2_tag_cron_job_script,
        name="LogToEc2TagCronJob",
        print_func=logger.info,
    )


@logger.start_and_end(msg="{func_name}")
def stop_log_to_ec2_tag_cron_job():
    """
    停止服务器状态监控定时脚本. 关闭由 :func:`run_log_to_ec2_tag_cron_job` 启动的 cron job.
    """
    stop_script(name="LogToEc2TagCronJob", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def run_measure_worldserver_cron_job():
    """
    运行服务器状态数据采集定时脚本. 这个 cron job 的详细信息请参考 todo ...
    """
    file_logger = get_logger()
    file_logger.debug(
        f"{common.play_or_pause} run {path_measure_worldserver_cron_job_script} in screen session"
    )
    logger.info(f"run {path_measure_worldserver_cron_job_script} in screen session")
    run_script(
        path_measure_worldserver_cron_job_script,
        name="MeasureWorldserverCronJob",
        print_func=logger.info,
    )


@logger.start_and_end(msg="{func_name}")
def stop_measure_worldserver_cron_job():
    """
    停止服务器状态数据采集定时脚本. 关闭由 :func:`run_measure_worldserver_cron_job` 启动的 cron job.
    """
    stop_script(name="MeasureWorldserverCronJob", print_func=logger.info)
