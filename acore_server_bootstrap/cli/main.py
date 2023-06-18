# -*- coding: utf-8 -*-

import fire
from ..s1_configure_db.api import configure_db
from ..s2_apply_server_config.api import apply_server_config


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


def run():
    fire.Fire(Command)
