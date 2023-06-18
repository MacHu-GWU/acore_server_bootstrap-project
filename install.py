#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script automatically setup the acore_server_bootstrap project on a brand new
EC2 instance.
"""

import typing as T
import os
import sys
import shutil
import subprocess
import contextlib
from pathlib import Path


@contextlib.contextmanager
def temp_cwd(path: T.Union[str, Path]):
    """
    Temporarily set the current working directory (CWD) and automatically
    switch back when it's done.

    Example:

    .. code-block:: python

        with temp_cwd(Path("/path/to/target/working/directory")):
            # do something
    """
    path = Path(path).absolute()
    if not path.is_dir():
        raise NotADirectoryError(f"{path} is not a dir!")
    cwd = os.getcwd()
    os.chdir(str(path))
    try:
        yield path
    finally:
        os.chdir(cwd)


PY_VER_MAJOR = sys.version_info.major
PY_VER_MINOR = sys.version_info.minor

# enumerate important paths
dir_here = Path.cwd().absolute()
dir_home = Path.home()
dir_git_repos = dir_home / "git_repos"
dir_acore_server_bootstrap_project = dir_git_repos / "acore_server_bootstrap-project"
dir_venv = dir_acore_server_bootstrap_project / ".venv"
dir_venv_bin = dir_venv / "bin"
path_venv_bin_python = dir_venv_bin / "python"
path_venv_bin_pip = dir_venv_bin / "pip"
path_acorebs_cli = dir_venv_bin / "acorebs"
# subprocess.run()


dir_git_repos.mkdir(parents=True, exist_ok=True)


def clean_up():
    print(f"--- Cleaning up '{dir_acore_server_bootstrap_project}' folder...")
    shutil.rmtree(dir_acore_server_bootstrap_project, ignore_errors=True)


def clone_acore_server_bootstrap_git_repo():
    print("--- Cloning acore_server_bootstrap git repo...")
    with temp_cwd(dir_git_repos):
        args = [
            "git",
            "clone",
            "https://github.com/MacHu-GWU/acore_server_bootstrap-project.git",
        ]
        subprocess.run(args, check=True)


def create_virtualenv():
    print("--- Creating virtualenv...")
    args = ["virtualenv", "-p", f"python{PY_VER_MAJOR}.{PY_VER_MINOR}", f"{dir_venv}"]
    subprocess.run(args, check=True)


def install_dependencies():
    print("--- Installing dependencies...")
    with temp_cwd(dir_acore_server_bootstrap_project):
        args = [f"{path_venv_bin_pip}", "install", "-e", "."]
        subprocess.run(args, check=True)


def show_info():
    print("--- Showing info...")
    args = [f"{path_acorebs_cli}", "info"]
    subprocess.run(args, check=True)


def run_bootstrap():
    print("--- Run bootstrap...")
    args = [f"{path_acorebs_cli}", "s01_configure_db"]
    subprocess.run(args, check=True)

    args = [f"{path_acorebs_cli}", "s02_apply_server_config"]
    subprocess.run(args, check=True)

    args = [f"{path_acorebs_cli}", "s03_run_server"]
    subprocess.run(args, check=True)


def run():
    clean_up()
    clone_acore_server_bootstrap_git_repo()
    create_virtualenv()
    install_dependencies()
    show_info()
    run_bootstrap()


if __name__ == "__main__":
    run()
