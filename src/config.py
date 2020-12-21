from cool_config import *

__all__ = ['config']


class Config(AbstractConfig):
    class rl(Section):
        api_url = String
        access_token = String

    class amqp(Section):
        url = String
        client_properties = Dict

    class storage(Section):
        # in s3 its a bucket name
        replays_path = String
        beatmaps_path = String

        # TODO: this
        current_storage = String

        class s3(Section):
            region_name = String

            secret_access_key = String
            access_key_id = String

            endpoint_url = String


config = Config()
