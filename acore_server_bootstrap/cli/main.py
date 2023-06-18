# -*- coding: utf-8 -*-

import fire
from ..s1_configure_db.api import configure_db


class Command:
    def info(self):
        print("Hello acore server bootstrap user!")

    def s01_configure_db(self):
        """
        Step 1. Configure database.
        """
        configure_db()


def run():
    fire.Fire(Command)
