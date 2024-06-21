Remote Bootstrap
==============================================================================
在 :ref:`bootstrap-actions` 一文中我们介绍了所有的 bootstrap action 的功能, 在 :ref:`cheat-sheet` 一文中我们介绍了所有要在 EC2 上运行的命令. 而本文则介绍了作为开发者, 如何在不 SSH 到 EC2 的情况下, 从开发者电脑或是 AWS EC2, Lambda 等计算平台上上远程执行 bootstrap 命令.


How it work
------------------------------------------------------------------------------
远程执行的本质是用 `aws_ssm_run_command <https://github.com/MacHu-GWU/aws_ssm_run_command-project>`_ 工具把 bootstrap 命令行命令发送到 EC2 上远程执行.


Example
------------------------------------------------------------------------------
:class:`~acore_server_bootstrap.remoter.Remoter` 类实现了远程执行的功能. 我们这里有一个脚本 `debug/remote_bootstrap.py <https://github.com/MacHu-GWU/acore_server_bootstrap-project/blob/main/debug/remote_bootstrap.py>`_, 介绍了这个类该怎么用.

.. dropdown:: debug/remote_bootstrap.py.py

    .. literalinclude:: ../../../debug/remote_bootstrap.py
       :language: python
       :linenos:
