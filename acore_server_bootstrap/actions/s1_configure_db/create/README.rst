该文件夹存放了对数据库的自动化配置所需的 SQL 文件. 一共有这么几个文件:

- ``.create_mysql.sql.jinja2``: 来自于 AzerothCore 官方 GitHub 仓库 https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql, 我加入了更多的注释, 以及将其进行了参数化. 该文件只是用于说明, 留档备份. 真正的业务代码则是基于该例子修改而来.
- ``create_mysql_database.sql.aws_rds_mode.jinja2``: 为第一次启动的 EC2 创建数据库, 配置 User
- ``create_mysql_user.sql.aws_rds_mode.jinja2``: 为已经存在的 EC2 更新 User 账号密码
- ``update_realmlist_address.sql.jinja2``: 更新 realmlist address
