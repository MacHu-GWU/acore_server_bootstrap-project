# -*- coding: utf-8 -*-

import fire
from ..s1_configure_db.api import configure_db
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

    def s01_configure_db(self):
        """
        Step 1. Configure database.
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

    def list_session(self):
        list_session()

    def enter_worldserver(self):
        enter_worldserver()

    def stop_server(self):
        stop_server()


def run():
    fire.Fire(Command)
