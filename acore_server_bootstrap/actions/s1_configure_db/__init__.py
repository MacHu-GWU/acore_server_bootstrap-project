# -*- coding: utf-8 -*-

"""
这一步是配置游戏数据库. 用于让 EC2 和 RDS 互相之间认识. 包括创建让 EC2 用的数据库 User,
配置 Realmlist.address 等动作. 这一步是幂等的, 也就是说输入不变 (配置数据不变), 造成的结果
也不变, 并且多次重复运行无副作用, 也没有什么性能影响.
"""