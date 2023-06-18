# -*- coding: utf-8 -*-

from pathlib import Path

from ..vendor.screen_session_manager import (
    run_script,
    list_session as _list_session,
    enter_session,
    stop_script,
)
from ..logger import logger

_dir_here = Path(__file__).absolute().parent
path_auth_sh = _dir_here / "auth.sh"
path_world_sh = _dir_here / "world.sh"


@logger.start_and_end(msg="{func_name}")
def run_server():
    """
    启动 auth 和 world 服务器.
    """
    run_script(path_auth_sh, name="auth")
    run_script(path_world_sh, name="world")


@logger.start_and_end(msg="{func_name}")
def list_session():
    _list_session()


@logger.start_and_end(msg="{func_name}")
def enter_worldserver():
    """
    进入 world 服务器的交互式 shell.
    """
    enter_session(name="world")


@logger.start_and_end(msg="{func_name}")
def stop_server():
    """
    停止 auth 和 world 服务器.
    """
    stop_script(name="auth")
    stop_script(name="world")
