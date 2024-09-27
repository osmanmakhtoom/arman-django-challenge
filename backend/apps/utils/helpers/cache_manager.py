import logging

from django.core.cache import cache

logger = logging.getLogger(__name__)


class CacheManager:

    def __init__(self, key: str):
        self.__period = None
        self.__key = key

    @property
    def key(self) -> str:
        return self.__key

    @property
    def value(self) -> any:
        return None if self.key not in cache else cache.get(self.key)

    @property
    def period(self) -> int:
        return self.__period

    @value.setter
    def value(self, value: any):
        cache.set(self.key, value, self.period)

    @period.setter
    def period(self, period: int):
        self.__period = period

    @property
    def is_expired(self) -> bool:
        if self.key in cache:
            return False
        return True

    def delete(self) -> bool:
        if not self.is_expired:
            cache.delete(self.key)
            return True
        return False
