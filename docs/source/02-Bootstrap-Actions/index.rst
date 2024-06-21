Bootstrap Actions
==============================================================================


Overview
------------------------------------------------------------------------------


1. Configure Ubuntu
------------------------------------------------------------------------------
这一步主要是对 Ubuntu 系统进行一些配置.

.. dropdown:: s0_configure_ubuntu/impl.py

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s0_configure_ubuntu/impl.py
       :language: python
       :linenos:


1.1 Disable Ubuntu Auto Upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:func:`~acore_server_bootstrap.actions.s0_configure_ubuntu.impl.disable_ubuntu_auto_upgrade`

.. admonition:: 如何判断 Auto Upgrade 是否已经被禁用
    :class: note

    .. code-block:: bash

        cat /etc/apt/apt.conf.d/20auto-upgrades

    如果你看了如下内容, 说明 **自动升级没有被禁用**

    .. code-block::

        APT::Periodic::Update-Package-Lists "1";
        APT::Periodic::Unattended-Upgrade "1";

    如果你看了如下内容, 说明 **自动升级已经被禁用**

    .. code-block::

        APT::Periodic::Update-Package-Lists "0";
        APT::Periodic::Unattended-Upgrade "0";


1.2 Setup EC2 Run On Restart Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:func:`~acore_server_bootstrap.actions.s0_configure_ubuntu.impl.setup_ec2_run_on_restart_script`

.. admonition:: 如何判断自动化脚本已经被部署
    :class: note

    .. code-block:: bash

        ls /var/lib/cloud/scripts/per-boot

    .. code-block::

        cat /var/lib/cloud/scripts/per-boot/wserver-run-on-restart.sh

    如果你看到了 ``wserver-run-on-restart.sh`` 文件, 说明已经被成功部署了.


2. Configure DB
------------------------------------------------------------------------------
这一步主要是对游戏数据库进行一些配置.

.. dropdown:: s1_configure_db/impl.py

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s1_configure_db/impl.py
       :language: python
       :linenos:


2.1 Create Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
在第一次开服的时候, 游戏数据库中是没有 ``acore_auth``, ``acore_characters``, ``acore_world`` 三个数据库的, 我们需要创建他们.

:func:`~acore_server_bootstrap.actions.s1_configure_db.impl.create_database`

.. dropdown:: s1_configure_db/create/create_mysql_database.sql.aws_rds_mode.jinja2

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s1_configure_db/create/create_mysql_database.sql.aws_rds_mode.jinja2
       :language: sql
       :linenos:


2.2 Create User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
游戏服务器连接数据库不是用的 Admin User (这样安全隐患太大了), 而是用我们创建的 Acore DB User. 在第一次开服的时候我们需要创建这些 User 并且给它们对应的 database 的访问权限. 并且, 如果我们修改了 configuration, 其中就包含了数据库用户名和密码, 我们同样要删掉旧的 DB User 并重新配置. 这个任务就是做这件事的.

, 游戏数据库中是没有 ``acore_auth``, ``acore_characters``, ``acore_world`` 三个数据库的, 我们需要创建他们.

:func:`~acore_server_bootstrap.actions.s1_configure_db.impl.create_database`

.. dropdown:: s1_configure_db/create/create_mysql_user.sql.aws_rds_mode.jinja2

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s1_configure_db/create/create_mysql_user.sql.aws_rds_mode.jinja2
       :language: sql
       :linenos:


2.3 Update Realmlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
在 ``acore_auth.realmlist`` 表中我们需要设定我们的游戏服务器的 IP. 这样登录服务器鉴权成功后才能将游戏客户端的连接导向到我们的游戏服务器. 而由于我们的 IP 地址可能在 EC2 重启后发生变化, 所以我们需要在每次重启 EC2 后更新这个表.


:func:`~acore_server_bootstrap.actions.s1_configure_db.impl.update_realmlist`

.. dropdown:: s1_configure_db/create/update_realmlist_address.sql.jinja2

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s1_configure_db/create/update_realmlist_address.sql.jinja2
       :language: sql
       :linenos:


2.4 Configure DB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这个任务可以依次完成 2.1, 2.2, 2.3 三个任务.



3. Apply Server Config
------------------------------------------------------------------------------
这一步主要是对游戏服务器进行一些配置.

.. dropdown:: s2_apply_server_config/impl.py

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s2_apply_server_config/impl.py
       :language: python
       :linenos:


3.1 Apply authserver Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
从 S3 上拉取 configuration 数据, 并把 `acore_server_config.api.Server.authserver_conf <https://acore-server-config.readthedocs.io/en/latest/acore_server_config/config/define/server.html#acore_server_config.config.define.server.Server>`_ 中的数据应用到 ``authserver.conf`` 文件中.

:func:`~acore_server_bootstrap.actions.s2_apply_server_config.impl.apply_authserver_conf`


3.2 Apply worldserver Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
从 S3 上拉取 configuration 数据, 并把 `acore_server_config.api.Server.worldserver_conf <https://acore-server-config.readthedocs.io/en/latest/acore_server_config/config/define/server.html#acore_server_config.config.define.server.Server>`_ 中的数据应用到 ``worldserver.conf`` 文件中.

:func:`~acore_server_bootstrap.actions.s2_apply_server_config.impl.apply_worldserver_conf`


3.3 Apply mod_lua_engine Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
从 S3 上拉取 configuration 数据, 并把 `acore_server_config.api.Server.mod_lua_engine_conf <https://acore-server-config.readthedocs.io/en/latest/acore_server_config/config/define/server.html#acore_server_config.config.define.server.Server>`_ 中的数据应用到 ``mod_LuaEngine.conf`` 文件中.

:func:`~acore_server_bootstrap.actions.s2_apply_server_config.impl.apply_mod_lua_engine_conf`


3.4 Apply Server Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这个任务可以依次完成 3.1, 3.2, 3.3 三个任务.


4. Check Server Status
------------------------------------------------------------------------------
这一步主要是运行检查游戏服务器健康状态的定时任务.

.. dropdown:: s3_check_server_status/impl.py

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s3_check_server_status/impl.py
       :language: python
       :linenos:


5. Run Server
------------------------------------------------------------------------------
这一步主要运行游戏服务器.

.. dropdown:: s4_run_server/impl.py

    .. literalinclude:: ../../../acore_server_bootstrap/actions/s4_run_server/impl.py
       :language: python
       :linenos:

.. note::

    在服务器上长期运行一个进程的核心技术是 GNU Screen Session, 建议仔细阅读 `Keep Long Live Session Using GNU Screen <https://dev-exp-share.readthedocs.io/en/latest/search.html?q=Keep+Long+Live+Session+Using+GNU+Screen&check_keywords=yes&area=default>`_ 做进一步了解.


5.1 Run Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
用 screen session 运行游戏服务器.

:func:`~acore_server_bootstrap.actions.s4_run_server.impl.run_server`


5.2 List Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
列出所有在运行中的 screen session.

:func:`~acore_server_bootstrap.actions.s4_run_server.impl.list_session`


5.3 Enter worldserver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
通过 screen session 进入进入 worldserver 的交互式命令行.

:func:`~acore_server_bootstrap.actions.s4_run_server.impl.enter_worldserver`


5.4 Stop Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
用 screen session 杀死游戏服务器.

:func:`~acore_server_bootstrap.actions.s4_run_server.impl.stop_server`
