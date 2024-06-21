# -*- coding: utf-8 -*-

from boto_session_manager import BotoSesManager
from acore_server.api import Server
from acore_server_bootstrap.api import Remoter

bsm = BotoSesManager(profile_name="bmt_app_dev_us_east_1")

server = Server.get(bsm=bsm, server_id="sbx-blue")

remoter = Remoter(ssm_client=bsm.ssm_client, server=server)

# remoter.hello()
# remoter.bootstrap_as_sudo()
# remoter.bootstrap()
# remoter.disable_ubuntu_auto_upgrade()
# remoter.create_database()
# remoter.create_user()
# remoter.update_realmlist()
# remoter.configure_db()
# remoter.apply_authserver_conf()
# remoter.apply_worldserver_conf()
# remoter.apply_mod_lua_engine_conf()
# remoter.apply_server_config()
# remoter.run_check_server_status_cron_job()
# remoter.stop_check_server_status_cron_job()
# remoter.run_server()
# remoter.list_session()
# remoter.stop_server()
