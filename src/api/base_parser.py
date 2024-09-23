from abc import ABC, abstractmethod
from typing import Any


class BaseParser(ABC):

    @staticmethod
    @abstractmethod
    def __connection_to_api(self, params: dict) -> Any:
        pass

    @classmethod
    @abstractmethod
    def load_vacancies(cls, keyword: str) -> dict:

        pass