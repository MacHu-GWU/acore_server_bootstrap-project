# -*- coding: utf-8 -*-

import acore_paths.api as acore_paths
from acore_conf.api import apply_changes

from ..logger import logger


@logger.start_and_end(msg="{func_name}")
def apply_server_config():
    from ..server import Server

    server = Server.from_ec2_inside()

    # authserver.conf
    data = server.config.authserver_conf.copy()
    data.update(
        {
            "LoginDatabaseInfo": f"{server.metadata.rds_inst.endpoint};3306;{server.config.db_username};{server.config.db_password};acore_auth",
        }
    )
    apply_changes(
        path_input=acore_paths.path_azeroth_server_authserver_conf_dist,
        path_output=acore_paths.path_azeroth_server_authserver_conf,
        data={"authserver": data},
    )

    # worldserver.conf
    data = server.config.worldserver_conf.copy()
    data.update(
        {
            "DataDir": f"{acore_paths.dir_azeroth_server_data}",
            "LogsDir": f"{acore_paths.dir_azeroth_server_logs}",
            "LoginDatabaseInfo": f"{server.metadata.rds_inst.endpoint};3306;{server.config.db_username};{server.config.db_password};acore_auth",
            "WorldDatabaseInfo": f"{server.metadata.rds_inst.endpoint};3306;{server.config.db_username};{server.config.db_password};acore_world",
            "CharacterDatabaseInfo": f"{server.metadata.rds_inst.endpoint};3306;{server.config.db_username};{server.config.db_password};acore_characters",
        }
    )
    apply_changes(
        path_input=acore_paths.path_azeroth_server_worldserver_conf_dist,
        path_output=acore_paths.path_azeroth_server_worldserver_conf,
        data={"worldserver": data},
    )

    # mod_LuaEngine.conf
    data = server.config.mod_lua_engine_conf.copy()
    data.update(
        {
            "Eluna.ScriptPath": f"{acore_paths.dir_server_lua_scripts}",
        }
    )
    apply_changes(
        path_input=acore_paths.path_mod_eluna_conf_dist,
        path_output=acore_paths.path_mod_eluna_conf,
        data={"worldserver": data},
    )
