# -*- coding: utf-8 -*-

import fire


class Command:
    def info(self):
        print("Hello acore server bootstrap user!")


def run():
    fire.Fire(Command)
