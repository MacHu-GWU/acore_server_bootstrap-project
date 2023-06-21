.. image:: https://readthedocs.org/projects/acore-server-bootstrap/badge/?version=latest
    :target: https://acore-server-bootstrap.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/acore_server_bootstrap-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project/actions?query=workflow:CI

.. .. image:: https://codecov.io/gh/MacHu-GWU/acore_server_bootstrap-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/acore_server_bootstrap-project

.. .. image:: https://img.shields.io/pypi/v/acore-server-bootstrap.svg
    :target: https://pypi.python.org/pypi/acore-server-bootstrap

.. .. image:: https://img.shields.io/pypi/l/acore-server-bootstrap.svg
    :target: https://pypi.python.org/pypi/acore-server-bootstrap

.. .. image:: https://img.shields.io/pypi/pyversions/acore-server-bootstrap.svg
    :target: https://pypi.python.org/pypi/acore-server-bootstrap

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project

.. image:: https://img.shields.io/badge/awesome_Acore!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/awesome-acore

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://acore-server-bootstrap.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://acore-server-bootstrap.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/acore-server-bootstrap#files


Welcome to ``acore_server_bootstrap`` Documentation
==============================================================================
**项目背景**

在大规模游戏服务器 (Azerothcore) 部署的流程中, 我们通常会将其分为以下几个步骤:

1. 游戏服务器核心的编译.
2. 将编译好的游戏服务器打包成镜像.
3. 对用镜像启动的游戏服务器进行自动配置.

而 #3 这一步又可以分为以下几个步骤:

1. 创建数据库的 user.
2. 创建三个数据库 (auth, characters, world), 如果还没创建过的话.
3. 将必要的配置写入数据中 (realmlist).
4. 将最新的配置写入 ``*.conf`` 文件中.
5. 禁止 ubuntu 的自动升级.
6. 对游戏服务器的启动脚本赋予可执行权限.
7. 启动游戏服务器.
8. 安装其他服务器组件, 例如 SOAP Agent, DB Agent 等.

这一连串步骤在每次开新服, 或是修改了配置文件的时候都需要进行, 非常的麻烦. 为了解决这个问题, 我们开发了 ``acore_server_bootstrap`` 这个工具, 它可以帮助我们自动完成上述的所有步骤.

**Note**

    注意, 该工具建立在特定的服务器的文件目录结构之上. 如果服务器的目录结构不符合预期, 则无法使用该工具.

**如何进行 Bootstrap**

在 EC2 上复制以下脚本即可运行该命令. 其原理是通过 ``curl`` 命令下载 `install.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/install.py>`_ 自动化脚本. 这个自动化脚本能 ``git clone ...`` 本项目, 安装依赖, 并用命令行工具运行 ``acorebs bootstrap`` 命令.

.. code-block:: bash

    python3 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"

如果你需要指定用特定的 Python 版本来运行 (例如用 3.8), 你可以这样做:

.. code-block:: bash

    python3.8 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"

Bootstrap 的过程中需要将这几个项目安装到服务器上 `acore_server_bootstrap <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/release-history.rst>`_, `acore_soap_app <https://github.com/MacHu-GWU/acore_soap_app-project/blob/main/release-history.rst>`_, 如果你需要指定它们的特定版本 (推荐这么做, 以增加确定性), 你可以用下面的命令, 只要修改对应项目的版本即可 (版本号就是 Git Tag 例如 ``0.1.1``):

.. code-block:: bash

    python -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)" --acore_server_bootstrap_version 0.1.1 --acore_soap_app_version 0.1.1

**acorebs 命令行工具**

用 Python 安装了本项目后就可以使用 ``acorebs`` 命令行工具了. 所有在 bootstrap 期间做的事情都可以单独用命令行再做一次. 下面是所有命令的列表.

``acorebs``

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs

``acorebs info``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs info

.. image:: ./docs/source/_static/icons/ec2.png

``acorebs bootstrap``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs bootstrap

``acorebs disable_ubuntu_auto_upgrade``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs disable_ubuntu_auto_upgrade

.. image:: ./docs/source/_static/icons/rds.png

``acorebs create_database``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs create_database

``acorebs create_user``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs create_user

``acorebs update_realmlist``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs update_realmlist

``acorebs configure_db``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs configure_db

.. image:: ./docs/source/_static/icons/config.png

``acorebs apply_authserver_conf``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_authserver_conf

``acorebs apply_worldserver_conf``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_worldserver_conf

``acorebs apply_mod_lua_engine_conf``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_mod_lua_engine_conf

``acorebs apply_server_config``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs apply_server_config

.. image:: ./docs/source/_static/icons/wow.png

``acorebs run_server``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs run_server

``acorebs list_session``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs list_session

``acorebs enter_worldserver``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs enter_worldserver

``acorebs stop_server``:

.. code-block:: bash

    /home/ubuntu/git_repos/acore_server_bootstrap-project/.venv/bin/acorebs stop_server


.. _install:

Install
------------------------------------------------------------------------------

``acore_server_bootstrap`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install acore-server-bootstrap

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade acore-server-bootstrap

https://img.shields.io/badge/any_✅-you_like-blue