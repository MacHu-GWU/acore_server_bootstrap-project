# -*- coding: utf-8 -*-

from acore_server_bootstrap import api


def test():
    _ = api

    _ = api.Server
    _ = api.disable_ubuntu_auto_upgrade
    _ = api.create_database
    _ = api.create_user
    _ = api.update_realmlist
    _ = api.configure_db
    _ = api.apply_authserver_conf
    _ = api.apply_worldserver_conf
    _ = api.apply_mod_lua_engine_conf
    _ = api.apply_server_config
    _ = api.run_server
    _ = api.list_session
    _ = api.enter_worldserver
    _ = api.stop_server


if __name__ == "__main__":
    from acore_server_bootstrap.tests import run_cov_test

    run_cov_test(__file__, "acore_server_bootstrap.api", preview=False)
