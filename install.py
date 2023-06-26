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
import dataclasses
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

dir_git_repos.mkdir(parents=True, exist_ok=True)


@dataclasses.dataclass
class PythonProject:
    project_name: str = dataclasses.field()
    git_repo_url: str = dataclasses.field()
    dir_project_root: Path = dataclasses.field()
    git_tag: T.Optional[str] = dataclasses.field(default=None)

    @property
    def dir_venv(self) -> Path:
        return self.dir_project_root / ".venv"

    @property
    def dir_venv_bin(self) -> Path:
        return self.dir_venv / "bin"

    @property
    def path_venv_bin_python(self) -> Path:
        return self.dir_venv_bin / "python"

    @property
    def path_venv_bin_pip(self) -> Path:
        return self.dir_venv_bin / "pip"

    def clean_up(self):
        print(f"--- Cleaning up '{self.dir_project_root}' folder...")
        if self.dir_project_root.exists():
            shutil.rmtree(self.dir_project_root)

    def clone_git_repo(self):
        print(f"--- Cloning {self.project_name} git repo...")
        with temp_cwd(dir_git_repos):
            if self.git_tag is None:
                args = ["git", "clone", self.git_repo_url]
            else:
                args = [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    "--branch",
                    self.git_tag,
                    self.git_repo_url,
                ]
            subprocess.run(args, check=True)

    def create_virtualenv(self):
        print(f"--- Creating virtualenv for {self.project_name} ...")
        args = [
            "virtualenv",
            "-p",
            f"python{PY_VER_MAJOR}.{PY_VER_MINOR}",
            f"{self.dir_venv}",
        ]
        subprocess.run(args, check=True)

    def install_dependencies(self):
        print(f"--- Installing dependencies for {self.project_name} ...")
        with temp_cwd(self.dir_project_root):
            args = [f"{self.path_venv_bin_pip}", "install", "-e", "."]
            subprocess.run(args, check=True)


@dataclasses.dataclass
class AcoreServerBootStrapProject(PythonProject):
    @property
    def path_acorebs_cli(self) -> Path:
        return self.dir_venv_bin / "acorebs"

    def show_info(self):
        print(f"--- Showing {self.project_name} info ...")
        args = [f"{self.path_acorebs_cli}", "info"]
        subprocess.run(args, check=True)

    def run_bootstrap(self):
        print("--- Run bootstrap...")
        args = [f"{self.path_acorebs_cli}", "bootstrap"]
        subprocess.run(args, check=True)


def run(
    acore_server_bootstrap_git_tag: T.Optional[str] = None,
    acore_soap_app_git_tag: T.Optional[str] = None,
):
    acore_server_bootstrap_project = AcoreServerBootStrapProject(
        project_name="acore_server_bootstrap",
        git_repo_url="https://github.com/MacHu-GWU/acore_server_bootstrap-project.git",
        dir_project_root=dir_git_repos.joinpath("acore_server_bootstrap-project"),
        git_tag=acore_server_bootstrap_git_tag,
    )
    acore_soap_app_project = PythonProject(
        project_name="acore_soap_app",
        git_repo_url="https://github.com/MacHu-GWU/acore_soap_app-project.git",
        dir_project_root=dir_git_repos.joinpath("acore_soap_app-project"),
        git_tag=acore_soap_app_git_tag,
    )
    # acore_server_bootstrap_project.clean_up()
    # acore_server_bootstrap_project.clone_git_repo()
    # acore_server_bootstrap_project.create_virtualenv()
    # acore_server_bootstrap_project.install_dependencies()
    # acore_server_bootstrap_project.show_info()
    # acore_server_bootstrap_project.run_bootstrap()

    acore_soap_app_project.clean_up()
    acore_soap_app_project.clone_git_repo()
    acore_soap_app_project.create_virtualenv()
    acore_soap_app_project.install_dependencies()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(prog="acore_server_bootstrap")
    parser.add_argument("--acore_server_bootstrap_version", required=False)
    parser.add_argument("--acore_soap_app_version", required=False)
    args = parser.parse_args()
    run(
        acore_server_bootstrap_git_tag=args.acore_server_bootstrap_version,
        acore_soap_app_git_tag=args.acore_soap_app_version,
    )
