# -*- coding: utf-8 -*-

"""
这是配置一台新创建的 EC2 (注意是新创建, 不是重启) 的脚本. 用于让 EC2 和 RDS 互相之间认识,
创建让 EC2 用的数据库 User, 配置 Realmlist.address 等. 该脚本也可以用于重新配置 EC2.
"""