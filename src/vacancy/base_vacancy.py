
from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    id: int
    name: str
    area: str
    salary_from: float
    salary_to: float
    url: str
    employer: str

    requirement: str

    @abstractmethod
    def vacancy_to_dict(self):
        pass
