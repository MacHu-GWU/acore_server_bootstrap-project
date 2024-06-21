# -*- coding: utf-8 -*-

"""
这个脚本可以对魔兽世界数据库进行更新.

这个脚本可以手动的找出某个日期之后的 SQL 文件 (也就是你上一次更新数据的时间之后), 然后
在 EC2 上手动用 Mysql CLI 来执行这些 SQL 文件, 达到手动更新的效果.

注意, 你需要手动填写下面的三个数据库连接信息. 并且建议在更新后删除这个脚本, 免得暴漏数据库密码.

.. code-block:: bash

    sudo python3 update_database.py
"""

import typing as T
import subprocess
from pathlib import Path


def run_sql(
    path: Path,
    host: str,
    database: T.Optional[str] = None,
    username: T.Optional[str] = None,
    password: T.Optional[str] = None,
    timeout: T.Optional[int] = None,
):
    """
    Run a SQL statement via MySQL cli.

    一个调用 MySQL cli 来运行大段 SQL 的函数. 本质上是 CLI 命令的封装
    """
    args = [
        "sudo",
        "mysql",
        f"--host={host}",
    ]
    if database:
        args.append(f"--database={database}")
    if username:
        args.append(f"--user={username}")
        args.append(f"--password={password}")
    if timeout:
        args.append(f"--connect-timeout={timeout}")
    with path.open("r") as f:
        subprocess.run(args, stdin=f, text=True)


# ------------------------------------------------------------------------------
# 请手动填写下面的三个数据库连接信息
# ------------------------------------------------------------------------------
host = "..."  # RDS endpoint
username = "..."  # RDS Master username
password = "..."  # RDS Master password
dir_old = Path("/home/ubuntu/git_repos/azerothcore-wotlk/data/sql/old/")
dir_db_auth = dir_old / "db_auth" / "9.x"
dir_db_characters = dir_old / "db_characters" / "9.x"
dir_db_world = dir_old / "db_world" / "9.x"

date_threshold = "2023_03_26"
for dir_db, database in [
    (dir_db_auth, "acore_auth"),
    (dir_db_characters, "acore_characters"),
    (dir_db_world, "acore_world"),
]:
    path_list = []
    for relpath in dir_db.iterdir():
        path = dir_db.joinpath(relpath)
        # 注意我们这里是 >=
        if (
            path.is_file()
            and path.name.endswith(".sql")
            and path.name >= date_threshold
        ):
            path_list.append(path)
    path_list = list(
        sorted(
            path_list,
            key=lambda path: path.name,
            reverse=False,
        )
    )
    for path in path_list:
        print(f"execute: {path.relative_to(dir_old)}")
        run_sql(
            path=path,
            host=host,
            database=database,
            username=username,
            password=password,
            timeout=1,
        )
