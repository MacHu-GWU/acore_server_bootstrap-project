How Bootstrap Works
==============================================================================


What is Bootstrap
------------------------------------------------------------------------------
Bootstrap 在计算机领域常用来表示在一个系统启动的最初阶段执行一小段程序, 用于初始化系统. 而在魔兽世界服务器运维项目中, 则是一段用于将一台全新的 EC2 实例, 自动配置成一台对外进行服务的魔兽世界服务器的脚本.

回顾我们的运维流程, 每个礼拜当服务器的源码更新后, 我们都会构建全新的 AMI. 运维的最佳实践告诉我们, 我们的 "运行环境", 也就是 AMI, 和 "运维工具", 也就是 `PyPI 上 <https://pypi.org/search/?q=acore_>`_ 我们维护的各种以 ``acore_`` 开头的库, 和 "运维数据", 也就是由 `acore_server_config <https://github.com/MacHu-GWU/acore_server_config-project>`_ 管理的配置数据, 这三个部分是解耦和的. 当我们需要创建全新的 EC2 时, 例如用来开发一段 eluna 脚本, 例如用来开发 database app (需要对数据库进行修改), 那么我们自然的就需要再创建全新的 EC2 和 DB 环境. 这时就需要对新服务器进行重新配置. 这个时候, Bootstrap 脚本就能大大提高我们的效率, 可以用简单的配置化的方式, 指定 "运维工具" 的版本, 指定 "运维数据" 的版本, 然后就可以配置好一套全新的游戏服务器了.

在我们介绍具体我们是如何实现 bootstrap 之前, 我们先来介绍一下 :ref:`ec2-user-data`, :ref:`cloud-init`, :ref:`root-user` 这三个相关的核心技术.


.. _ec2-user-data:

EC2 User Data
------------------------------------------------------------------------------
EC2 User Data 是我们实现 bootstrap 的核心技术之一. 它允许我们在启动一台全新的 EC2 时, 自动执行一系列我们指定的脚本. 但是也仅限于第一次启动.

简而言之, 你可以在调用 `boto3.client("ec2").run_instances(..., UserData="...", ...) <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html>`_ 的时候传入一个命令行命令. 注意, 这个命令会以 root 用户的身份执行, 请参考 :ref:`root-user` 中的注意事项.

Reference:

- `Run commands on your Linux instance at launch <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html>`_
- `Work with instance user data <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data>`_.html


.. _cloud-init:

Cloud Init
------------------------------------------------------------------------------
Cloud Init 是我们实现 bootstrap 的另一个核心技术. 它允许我们在每次 EC2 重启的时候, 自动执行一系列我们指定的脚本.

简单来说 Cloud Init 是一个社区主导的开源软件, 用于各家云厂商在创建托管的 Linux 服务器时执行初始化脚本, 基本上所有的云服务器厂商的托管服务器都会默认安装这个软件. 而你只要将 shell script 放到 ``/var/lib/cloud/scripts/per-boot/`` 这个目录下, 再确保第一行有 ``#!/bin/bash`` 这个声明, 那么这个脚本就会在每次重启的时候被执行. 我们可以用它来实现很多自动化功能.

简单来说 Cloud Ini
    EC2 可以用 User Data 来指定在第一次 Launch EC2 的时候运行一些自动化脚本来配置机器.
    但是这只限于第一次 Launch. 作为游戏服务器, 我们是有一些自动化脚本需要在每次重启时运行的.
    这里我们使用了 AWS 官方提议的方法, 将我们需要运行的自动化脚本放到
    ``/var/lib/cloud/scripts/per-boot/`` 目录下. 这样每次重启的时候, 这个目录下的脚本都会被
    ``cloud-init`` 这个每个 EC2 都会自动运行的启动程序所运行. 值得注意的是, 默认该目录下
    的脚本会以 root 用户的身份运行, 而如果你的脚本需要创建一些给 ubuntu 用户使用的文件, 那么
    就要注意用 ``sudo -H -u ubuntu ...`` 命令来切换用户了.

Reference:

- `How can I utilize user data to automatically run a script with every restart of my Amazon EC2 Linux instance? <https://repost.aws/knowledge-center/execute-user-data-ec2>`_
- `Cloud init open source <https://cloud-init.io/>`_


.. _root-user:

Root User
------------------------------------------------------------------------------
无论是用 :ref:`ec2-user-data` 还是 :ref:`cloud-init`, 又或是用 `AWS SSM Run Command <https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html>`_ 运行命令, 都是以 root 用户的身份执行的. 例如, 你可以用 ``sudo`` 来执行一些需要 root 权限的命令. 如果你的 Command 的目的是创建一些文件或是 CLI 工具以后供普通用户调用, 那么这些 Command 你需要用 ``sudo -H -u ubuntu ${Command}`` 来切换到普通用户执行.


Bootstrap Script
------------------------------------------------------------------------------
实现这一目标的核心脚本呢是一个叫 `bootstrap script <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/install.py>`_ 的脚本. 你只要在 EC2 上运行 **下面这个命令**, 既可把一个刚从 AMI 启动的 EC2 实例, 变成一个正在运行游戏服务器的 EC2 实例. 这个脚本是一个无任何依赖的纯 Python 脚本, 而下面这个命令则是会将这个脚本的内容从 GitHub 下载下来然后用系统的 Python 运行它.

.. code-block:: bash

    sudo /home/ubuntu/.pyenv/shims/python3 -c \
        "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"'

这个脚本里做了很多很多事情, 包括从 GitHub 上拉取一些需要的 repository, 并创建虚拟环境, 安装好依赖. 以及对 Ubuntu 系统进行一些配置, 包括关闭自动更新 (防止 mysql 被自动升级), 配置好启动时自动运行的 `cloud init 脚本 <https://repost.aws/knowledge-center/execute-user-data-ec2>`_, 从 S3 上拉取当前服务器的 configuration, 然后根据 configuration 配置好 ``authserver.conf``, ``worldserver.conf``, 以及配置好数据库, 更新数据库中的 realmlist 字段, 并最后在 screen session 中启动 authserver 和 worldserver, 还有系统健康监控脚本. 这整个流程就叫做 ``bootstrap``.


.. _bootstrap-on-first-launch-ec2:

Bootstrap on First Launch EC2
------------------------------------------------------------------------------
我们第一次创建的时候, 会使用一些 :ref:`ec2-user-data` 来在启动后自动执行 bootstrap 命令. 这个命令的内容如下:

.. code-block:: bash

    sudo /home/ubuntu/.pyenv/shims/python3 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"'

这个命令的本质就是用系统自带的 Python 来运行一个 `install.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/install.py>`_ 脚本 (会用 curl 将脚本的内容下载到内存). 这个脚本会做非常多的事情, 包括:

1. 执行操作系统 bootstrap: 这一步主要是将操作系统本身配置好. 在服务器上安装的必要的 Python 项目, 包括 `acore_soap_app <https://github.com/MacHu-GWU/acore_soap_app-project>`_, `acore_db_app <https://github.com/MacHu-GWU/acore_db_app-project>`_, `acore_server_bootstrap <https://github.com/MacHu-GWU/acore_server_bootstrap-project>`_ (这个项目本身). ``acore_server_bootstrap`` 项目的 CLI 工具实现了自动化配置游戏服务器的逻辑.
2. 执行服务器 bootstrap: 这一步主要是将游戏服务器配置好. 由于前面我们已经安装好了 ``acore_server_bootstrap`` 工具 (这个项目本身), 那么所有的配置游戏服务器的任务也就是一条命令的事. 这些任务包括:
    1. 关闭 ubuntu 的自动更新, 防止它自动升级 mysql 版本导致游戏服务器无法启动 (需要 sudo).
    2. 配置好 :ref:`cloud-init` 要用到的脚本, 使得以后每次 EC2 重启后也能自动启动游戏服务器 (需要 sudo).
    3. 从 S3 拉取配置数据.
    4. 配置好数据库 (主要是 create database, create database user, update realmlist).
    5. 配置好 authserver.conf 和 worldserver.conf.
    6. 启动游戏服务器健康状态监控脚本.
    7. 启动游戏服务器.

.. important::

    这里最重要的一部是 2.2. 它会用 sudo 运行 :func:`~acore_server_bootstrap.actions.s0_configure_ubuntu.impl.setup_ec2_run_on_restart_script` 这个函数. 这个函数会将 `wserver-run-on-restart.sh <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/acore_server_bootstrap/actions/s0_configure_ubuntu/wserver-run-on-restart.sh>`_ 脚本拷贝到 ``/var/lib/cloud/scripts/per-boot/wserver-run-on-restart.sh``, 这样 :ref:`cloud-init` 就会自动在每次启动 EC2 的时候执行这个脚本.

    通过观察这个脚本的内容, 你会发现它会在 EC2 启动后用 ``ubuntu`` 用户运行 `wserver_run_on_restart.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/acore_server_bootstrap/actions/s0_configure_ubuntu/wserver_run_on_restart.py>`_, 以及用 ``root`` 用户运行 `wserver_run_on_restart_as_sudo.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/acore_server_bootstrap/actions/s0_configure_ubuntu/wserver_run_on_restart_as_sudo.py>`_. 而这两个脚本的里的逻辑其实就是 2.1, 2.2, ... 的子集.

    .. dropdown:: wserver-run-on-restart.sh

        .. literalinclude:: ../../../acore_server_bootstrap/actions/s0_configure_ubuntu/wserver-run-on-restart.sh
           :language: bash
           :linenos:

这种设计的美妙之处在于, 你不仅能在创建 EC2 时用 User data 执行 bootstrap. 你还可以手动 SSH 到 EC2 上然后复制粘贴命令执行 bootstrap. 这样使得你可以临时对 Git 上的代码或是 configuration 进行修改, 然后无需重启 EC2 就能重新应用这些修改.


.. _bootstrap-on-restart-ec2:

Boostrap on Restart EC2
------------------------------------------------------------------------------
在 EC2 已经被创建后, 我们可能会关机开机或是重启. 这时 :ref:`cloud-init` 里的脚本 `wserver-run-on-restart.sh <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/acore_server_bootstrap/actions/s0_configure_ubuntu/wserver-run-on-restart.sh>`_ 就会被执行. 这个脚本则是在我们第一次启动 EC2 时的 bootstrap 脚本放进去的.

这个脚本的内容本质上是 ``install.py`` 的子集, 主要是 :ref:`执行服务器 bootstrap <bootstrap-on-first-launch-ec2>` 中的任务.


.. _rerun-bootstrap-on-first-launch-ec2:

Rerun Bootstrap on First Launch EC2
------------------------------------------------------------------------------
如果你在第一次 launch EC2 的时候的 bootstrap 脚本有 bug, 你可以在更新代码或配置之后使用 :class:`acore_server_bootstrap.api.Remoter.install <acore_server_bootstrap.remoter.Remoter.install>` 重新执行一次. 示例代码可以参考 `remote_bootstrap.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/debug/remote_bootstrap.py#L36>`_.


.. _restart-worldserver-with-updated-configuration:

Restart worldserver with Updated Configuration
------------------------------------------------------------------------------
如果想要在不重启 EC2 的情况下更新 worldserver.conf 并重启 worldserver, 或是更新 database config, 例如你要调整经验倍率, 又或者修改了 database 的密码, 那么你可以用 `deploy_parameter.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/deploy_parameters.py>`_ (另一个项目中的脚本) 把最新配置部署到 S3 之后, 然后依次运行下面几个 remote bootstrap 命令既可:

- :meth:`acore_server_bootstrap.api.Remoter.stop_server <acore_server_bootstrap.remoter.Remoter.stop_server>`: 先停止 authserver 和 worldserver.
- :meth:`acore_server_bootstrap.api.Remoter.create_user <acore_server_bootstrap.remoter.Remoter.create_user>`: 如果更新了数据库密码, 则需要重新配置 database user.
- :meth:`acore_server_bootstrap.api.Remoter.update_realmlist <acore_server_bootstrap.remoter.Remoter.update_realmlist>`: 如果你的 EC2 的 elastic ip 变了, 则要更新 realmlist.
- :meth:`acore_server_bootstrap.api.Remoter.apply_server_config <acore_server_bootstrap.remoter.Remoter.apply_server_config>`: 更新各种 ``*.conf`` 文件.
- :meth:`acore_server_bootstrap.api.Remoter.run_server <acore_server_bootstrap.remoter.Remoter.run_server>`: 重新运行 authserver 和 worldserver.
- :meth:`acore_server_bootstrap.api.Remoter.list_session <acore_server_bootstrap.remoter.Remoter.list_session>`: 检查 authserver 和 worldserver 是否已经运行了.

过个十几秒游戏服务器就可以登录了. 你可以直接用游戏客户端登录. 如果你不放心, 你还可以 ``sshec2 ssh`` SSH 到 EC2 上, 然后运行 ``/home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs enter_worldserver`` 来进入 worldserver 交互式 shell.

示例代码可以参考 `remote_bootstrap.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/debug/remote_bootstrap.py#L50>`_.
