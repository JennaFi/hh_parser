import json
import os
from ctypes import pydll

import pytest

from src.vacancy.vacancy import Vacancy


@pytest.fixture
def get_request():
    return {'items': [{'id': '1010101213', 'name': 'API backend developer'}]}

@pytest.fixture
def get_vacancies_upload():
    return [{'id': '1010101213', 'name': 'API backend developer'} for i in range(20)]


@pytest.fixture
def vacancies():
    with open(os.path.abspath('../tests/vacancies_test.json'),'r') as f:
        return json.load(f)['items']


@pytest.fixture
def vacancy_1():
    return Vacancy(
        1, "Python Developer", "Москва", 100000, 150000, 'RUR', "https://hh.ru/vacancy/1",
        "Компания A","разаработка бэкенд"
    )
@pytest.fixture
def vacancy_2():
    return Vacancy(
        2, "Django разработчик", "Тверь", 120000, 200000, 'RUR', "https://hh.ru/vacancy/2",
        "Компания Б","разаработка приложений"
    )



@pytest.fixture
def vacancy_without_salary():
    return Vacancy(
        3, "Backend Developer", "Санкт-Петербург", 0.0, 0.0, 'RUR', "https://hh.ru/vacancy/3", "Компания C",
        "be cool")


@pytest.fixture
def vacancy_dict():
    return {
        "id": "106931996",
        "name": "PHP-разработчик",
        "employer": "KUBER",
        "url": "https://hh.ru/vacancy/106931996",
        "area": "Москва",
        "salary_from": 120000,
        "salary_to": 160000,
        "currency": "RUR",
        "requirement": "Опытом в коммерческой разработке от года. Уверенными знаниями <highlighttext>PHP</highlighttext> "
                       "7.4. Пониманием принципов ООП. Системами управления версиями Git. "
    }


@pytest.fixture
def vacancies_list():
        return [
            Vacancy(1, "Python Developer", "Москва", "https://hh.ru/vacancy/1","Компания A",
                     "Опыт работы с Python 3+,", 100000, 150000, 'RUR'
                    ),
            Vacancy(2, "Backend Developer", "Санкт-Петербург", "https://hh.ru/vacancy/2", "Компания B",
                    "Знание Python и Django", 80000, 120000, 'RUR'
                    ),
            Vacancy(3, "Frontend Developer", "Москва", "https://hh.ru/vacancy/3", "Компания C",
                    "Опыт работы с JavaScript, React",
                   90000, 130000, 'RUR')

        ]


@pytest.fixture
def vacancy_objects_list():

    return[


        {
            "id": "3",
            "name": "Django-разработчик",
            "employer": "KUBER",
            "url": "https://hh.ru/vacancy/106931996",
            "area": "Москва",
            "salary_from": 120000,
            "salary_to": 180000,
            "currency": "RUR",
            "requirement": "Опытом в коммерческой разработке от года. Уверенными знаниями <highlighttext>PHP</highlighttext> "
                           "7.4. Пониманием принципов ООП. Системами управления версиями Git. "
        },
        {
            "id": "2",
            "name": "PHP-разработчик",
            "employer": "KUBER",
            "url": "https://hh.ru/vacancy/106931996",
            "area": "Москва",
            "salary_from": 120000,
            "salary_to": 160000,
            "currency": "RUR",
            "requirement": "Опытом в коммерческой разработке от года. Уверенными знаниями <highlighttext>PHP</highlighttext> "
                           "7.4. Пониманием принципов ООП. Системами управления версиями Git. "
        },
        {
            "id": 1,
            "name": "PHP-разработчик",
            "employer": "KUBER",
            "url": "https://hh.ru/vacancy/106931996",
            "area": "Москва",
            "salary_from": 120000,
            "salary_to": 150000,
            "currency": "RUR",
            "requirement": "Опытом в коммерческой разработке от года. Уверенными знаниями <highlighttext>PHP</highlighttext> "
                           "7.4. Пониманием принципов ООП. Системами управления версиями Git. "
        }

    ]