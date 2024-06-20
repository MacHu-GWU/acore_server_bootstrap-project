Bootstrap Actions
==============================================================================


Overview
------------------------------------------------------------------------------


1. Configure Ubuntu
------------------------------------------------------------------------------


1.1 Disable Ubuntu Auto Upgrade
------------------------------------------------------------------------------
:func:`~acore_server_bootstrap.actions.s0_configure_ubuntu.impl.disable_ubuntu_auto_upgrade`

.. admonition:: 如何判断 Auto Upgrade 是否已经被禁用
    :class: note

    .. code-block:: bash

        cat /etc/apt/apt.conf.d/20auto-upgrades

    如果你看了如下内容, 说明 **自动升级没有被禁用**

    .. code-block::

        APT::Periodic::Update-Package-Lists "1";
        APT::Periodic::Unattended-Upgrade "1";

    如果你看了如下内容, 说明 **自动升级没有被禁用**

    .. code-block::

        APT::Periodic::Update-Package-Lists "0";
        APT::Periodic::Unattended-Upgrade "0";
