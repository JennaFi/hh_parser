from abc import ABC, abstractmethod


class BaseParser(ABC):
    # base_url = ""
    #
    # def __init__(self, base_url):
    #     self.base_url = base_url

    @abstractmethod
    def get_connection_to_api(self, **params):
        pass


    @classmethod
    @abstractmethod
    def get_vacancies(cls, **params):
        pass