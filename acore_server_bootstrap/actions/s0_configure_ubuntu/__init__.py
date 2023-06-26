# -*- coding: utf-8 -*-

"""
这一步是配置 EC2 服务器的第一步, 配置 Ubuntu 系统. 其中具体步骤包括

- 关闭 Ubuntu 的自动更新. 主要是为了防止 Ubuntu 更新 MySQL Client 的小版本. 因为游戏服务器
    要求 MySQL Client 的版本跟服务器编译时的版本以及数据库的版本一摸一样.
"""