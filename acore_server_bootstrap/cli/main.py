# -*- coding: utf-8 -*-

import fire

from .. import api
from ..logger import logger


class Command:
    """
    acore server bootstrap command line interface.
    """
    def info(self):
        """
        Print welcome message.
        """
        print("Hello acore server bootstrap user!")

    @logger.pretty_log()
    def bootstrap(self):
        """
        Bootstrap a new EC2 server.
        """
        api.disable_ubuntu_auto_upgrade()

        server = api.Server.from_ec2_inside()
        api.configure_db(server)
        api.apply_server_config(server)
        api.run_server(server)

    def disable_ubuntu_auto_upgrade(self):
        """
        Disable Ubuntu auto upgrade (don't upgrade mysql).
        """
        api.disable_ubuntu_auto_upgrade()

    def create_database(self):
        """
        Create the database user for game server and three initial databases.
        """
        api.create_database()

    def create_user(self):
        """
        Create the database user for game server.
        """
        api.create_user()

    def update_realmlist(self):
        """
        Update 'acore_auth.realmlist.address'.
        """
        api.update_realmlist()

    def configure_db(self):
        """
        Configure the database for game server.
        """
        api.configure_db()

    def apply_authserver_conf(self):
        """
        Update the authserver.conf.
        """
        api.apply_authserver_conf()

    def apply_worldserver_conf(self):
        """
        Update the worldserver.conf.
        """
        api.apply_worldserver_conf()

    def apply_mod_lua_engine_conf(self):
        """
        Update the mod_LuaEngine.conf.
        """
        api.apply_mod_lua_engine_conf()

    def apply_server_config(self):
        """
        Update the authserver.conf, worldserver.conf and mod_LuaEngine.conf.
        """
        api.apply_server_config()

    def run_server(self):
        """
        Run the game server in screen session.
        """
        api.run_server()

    def list_session(self):
        """
        List all screen sessions.
        """
        api.list_session()

    def enter_worldserver(self):
        """
        Enter the worldserver screen session.
        """
        api.enter_worldserver()

    def stop_server(self):
        """
        Stop the game server.
        """
        api.stop_server()


def run():
    fire.Fire(Command)
