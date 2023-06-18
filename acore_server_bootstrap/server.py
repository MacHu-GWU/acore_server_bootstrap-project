# -*- coding: utf-8 -*-

import dataclasses

from acore_server_metadata.api import Server as ServerMetadata
from acore_server_config.api import bsm, Server as ServerConfig
from acore_server_config.api import get_server as get_server_config


@dataclasses.dataclass
class Server:
    config: ServerConfig
    metadata: ServerMetadata

    @classmethod
    def from_ec2_inside(cls) -> "Server":
        config = get_server_config()
        metadata = ServerMetadata.get_server(
            id=config.id,
            ec2_client=bsm.ec2_client,
            rds_client=bsm.rds_client,
        )
        return cls(
            config=config,
            metadata=metadata,
        )
