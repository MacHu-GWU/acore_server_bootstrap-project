
.. .. image:: https://readthedocs.org/projects/acore-server-bootstrap/badge/?version=latest
    :target: https://acore-server-bootstrap.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/acore_server_bootstrap-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project/actions?query=workflow:CI

.. .. image:: https://codecov.io/gh/MacHu-GWU/acore_server_bootstrap-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/acore_server_bootstrap-project

.. image:: https://img.shields.io/pypi/v/acore-server-bootstrap.svg
    :target: https://pypi.python.org/pypi/acore-server-bootstrap

.. image:: https://img.shields.io/pypi/l/acore-server-bootstrap.svg
    :target: https://pypi.python.org/pypi/acore-server-bootstrap

.. image:: https://img.shields.io/pypi/pyversions/acore-server-bootstrap.svg
    :target: https://pypi.python.org/pypi/acore-server-bootstrap

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/acore_server_bootstrap-project

------

.. .. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://acore-server-bootstrap.readthedocs.io/en/latest/

.. .. image:: https://img.shields.io/badge/Link-API-blue.svg
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
在大规模游戏服务器部署的流程中, 我们通常会将其分为以下几个步骤:

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

这一连串步骤在每次开新服, 或是修改了配置文件的时候都需要进行, 非常的麻烦. 为了解决这个问题, 我们开发了 ``acore_server_bootstrap`` 这个工具, 它可以帮助我们自动完成上述的所有步骤.

**Note**

    注意, 该工具建立在特定的服务器的文件目录结构之上. 如果服务器的目录结构不符合预期, 则无法使用该工具.

.. code-block:: bash

    python3 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"
    python3.8 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/acore_server_bootstrap-project/main/install.py)"

.. _install:

Install
------------------------------------------------------------------------------

``acore_server_bootstrap`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install acore-server-bootstrap

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade acore-server-bootstrap
