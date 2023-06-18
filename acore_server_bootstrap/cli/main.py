# -*- coding: utf-8 -*-

import fire
from ..s1_configure_db.api import (
    run_create_mysql_database_sql_in_rds_mode,
    run_create_mysql_user_sql_in_rds_mode,
    run_update_realmlist_address_sql,
    configure_db,
)
from ..s2_apply_server_config.api import apply_server_config
from ..s3_run_server.api import (
    run_server,
    list_session,
    enter_worldserver,
    stop_server,
)


class Command:
    def info(self):
        print("Hello acore server bootstrap user!")

    def bootstrap(self):
        """
        Bootstrap a new EC2 server.
        """
        configure_db()
        apply_server_config()
        run_server()

    def db_configure(self):
        """
        Configure database.
        """
        configure_db()

    def s02_apply_server_config(self):
        """
        Step 2. Apply server config.
        """
        apply_server_config()

    def s03_run_server(self):
        """
        Step 3. Run server.
        """
        run_server()

    def run_server(self):
        run_server()

    def list_session(self):
        list_session()

    def enter_worldserver(self):
        enter_worldserver()

    def stop_server(self):
        stop_server()


def run():
    fire.Fire(Command)
