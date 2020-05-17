from typing import Dict

import redis


class Redis:
    def __init__(self, host: str, port: int):
        self.db_redis = redis.Redis(
            host=host,
            port=port,
            decode_responses=True
        )

    def set(self, key: str, value: int):
        self.db_redis.set(key, value)

    def get(self, key: str) -> int:
        return self.db_redis.get(key)

    def clear(self):
        for key in self.db_redis.keys():
            self.db_redis.delete(key)

    def get_values(self):
        values: Dict[str, int] = {}
        for key in self.db_redis.keys():
            values[key] = int(self.db_redis.get(key))

        return values
