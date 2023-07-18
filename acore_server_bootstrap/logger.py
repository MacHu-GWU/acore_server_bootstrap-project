# -*- coding: utf-8 -*-

from loguru import logger as file_logger
from .vendor.nested_logger import NestedLogger
from .paths import path_log

logger = NestedLogger(name="acore_server_bootstrap", log_format="%(message)s")

file_logger.remove()
file_logger.add(
    str(path_log),
    format="{time: YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}",
    rotation="1 MB",
)
