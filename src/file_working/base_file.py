from abc import ABC, abstractmethod


class BaseFile(ABC):

    @abstractmethod
    def add_to_file(self, data: dict):
        pass


    @abstractmethod
    def get_from_file(self, *args, **kwargs):
        pass



    @staticmethod
    @abstractmethod
    def delete_vacancy(self, vacancy_to_delete):
        pass
