# -*- coding: utf-8 -*-

from light_emoji import common

from ...logger import logger
from ...logger_ubuntu import get_logger

from ...vendor.screen_session_manager import (
    run_script,
    list_session as _list_session,
    enter_session,
    stop_script,
)
from .paths import path_auth_sh, path_world_sh


@logger.start_and_end(msg="{func_name}")
def run_server():
    """
    启动 auth 和 world 服务器.
    """
    file_logger = get_logger()
    file_logger.debug(f"{common.play_or_pause} run server ...")
    logger.info(f"run {path_auth_sh} and {path_auth_sh} in screen session")
    run_script(path_auth_sh, name="auth", print_func=logger.info)
    run_script(path_world_sh, name="world", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def list_session():
    """
    列出所有 screen session.
    """
    _list_session()


@logger.start_and_end(msg="{func_name}")
def enter_worldserver():
    """
    进入 world 服务器的交互式 shell.
    """
    enter_session(name="world", print_func=logger.info)


@logger.start_and_end(msg="{func_name}")
def stop_server():
    """
    停止 auth 和 world 服务器.
    """
    stop_script(name="auth", print_func=logger.info)
    stop_script(name="world", print_func=logger.info)
