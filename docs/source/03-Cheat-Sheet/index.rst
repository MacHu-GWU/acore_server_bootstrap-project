.. _cheat-sheet:

Cheat Sheet
==============================================================================
你可以用本文档来快速查询常用的 bootstrap 命令, 并复制粘贴.

.. note::

    **本文档中的所有命令都需要 SSH 到 EC2 游戏服务器上运行**. 除了 :ref:`just-bootstrap` 中的命令, 其他命令都要确保你已经下载安装了 `acore_server_bootstrap <https://github.com/MacHu-GWU/acore_server_bootstrap-project>`_. 如果你还没有安装, 你可以参考 :ref:`just-bootstrap` 来一键安装.


.. _just-bootstrap:

BootStrap
------------------------------------------------------------------------------
Just Bootstrap:

.. code-block:: bash

    sudo /home/ubuntu/.pyenv/shims/python3 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"

如果你需要指定用特定的 Python 版本来运行 (例如用 3.11), 你可以这样做:

.. code-block:: bash

    sudo /home/ubuntu/.pyenv/shims/python3.11 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"

Bootstrap 的过程中需要将这几个项目安装到服务器上 `acore_server_bootstrap <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/release-history.rst>`_, `acore_soap_app <https://github.com/MacHu-GWU/acore_soap_app-project/blob/main/release-history.rst>`_, 如果你需要指定它们的特定版本 (**推荐这么做, 以增加确定性**), 你可以用下面的命令, 只要修改对应项目的版本即可 (版本号就是 Git Tag 例如 ``0.1.1``):

.. code-block:: bash

    sudo /home/ubuntu/.pyenv/shims/python3.11 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)" --acore_server_bootstrap_version 1.2.1 --acore_soap_agent_version 0.2.1 --acore_soap_app_version 0.3.6 --acore_soap_app_version 0.3.6 --acore_server_monitoring_measurement_version 0.2.1 --acore_db_app_version 0.2.3


1. Configure Ubuntu
------------------------------------------------------------------------------
.. image:: ../_static/icons/ec2.png


1.1 Disable Ubuntu Auto Upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    sudo /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs disable_ubuntu_auto_upgrade


1.2 Setup EC2 Run On Restart Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    sudo /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs setup_ec2_run_on_restart_script


2. Configure DB
------------------------------------------------------------------------------
.. image:: ../_static/icons/rds.png


2.1 Create Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs create_database


2.2 Create User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs create_user


2.3 Update Realmlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs update_realmlist


2.4 Configure DB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs configure_db



3. Apply Server Config
------------------------------------------------------------------------------
.. image:: ../_static/icons/config.png


3.1 Apply authserver Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_authserver_conf


3.2 Apply worldserver Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_worldserver_conf


3.3 Apply mod_lua_engine Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_mod_lua_engine_conf


3.4 Apply Server Config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_server_config


3.5 Sync Lua Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs sync_lua_scripts


4. Check Server Status
------------------------------------------------------------------------------
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs run_check_server_status_cron_job

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs stop_check_server_status_cron_job

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs run_log_to_ec2_tag_cron_job

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs stop_log_to_ec2_tag_cron_job

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs run_measure_worldserver_cron_job

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs stop_measure_worldserver_cron_job


5. Run Server
------------------------------------------------------------------------------
.. image:: ../_static/icons/wow.png


5.1 Run Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs run_server


5.2 List Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs list_session


5.3 Enter worldserver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs enter_worldserver


5.4 Stop Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs stop_server
