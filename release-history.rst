.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.2.1 (2023-06-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Automatically configure `acore_soap_app <https://github.com/MacHu-GWU/acore_soap_app-project>`_ SOAP agent.


0.1.1 (2023-06-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First release
- Add ``acorebs`` command line interface.

.. code-block:: bash

    NAME
        acorebs - acore server bootstrap command line interface.


    SYNOPSIS
        acorebs COMMAND

    DESCRIPTION
        acore server bootstrap command line interface.


    COMMANDS
        COMMAND is one of the following:

         info
           Print welcome message.

         bootstrap
           Bootstrap a new EC2 server.

         apply_authserver_conf
           Update the authserver.conf.

         apply_worldserver_conf
           Update the worldserver.conf.

         apply_mod_lua_engine_conf
           Update the mod_LuaEngine.conf.

         apply_server_config
           Update the authserver.conf, worldserver.conf and mod_LuaEngine.conf.

         create_database
           Create the database user for game server and three initial databases.

         create_user
           Create the database user for game server.

         update_realmlist
           Update 'acore_auth.realmlist.address'.

         configure_db
           Configure the database for game server.

         disable_ubuntu_auto_upgrade
           Disable Ubuntu auto upgrade (don't upgrade mysql).

         run_server
           Run the game server in screen session.

         list_session
           List all screen sessions.

         enter_worldserver
           Enter the worldserver screen session.

         stop_server
           Stop the game server.
