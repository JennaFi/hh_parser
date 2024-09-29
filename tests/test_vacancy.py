import pytest

from src.vacancy.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    assert vacancy_1.id == 1
    assert vacancy_1.name == "Python Developer"
    assert vacancy_1.area == "Москва"
    assert vacancy_1.employer == "Компания A"
    assert vacancy_1.url == "https://hh.ru/vacancy/1"
    assert vacancy_1.salary_from == 100000
    assert vacancy_1.salary_to == 150000

def test_vacancy_without_salary(vacancy_without_salary):
    assert vacancy_without_salary.salary_from == 0.0
    assert vacancy_without_salary.salary_to == 0.0

def test_vacancy_str(vacancy_1):
    expected_str = (
        "id: 1. Vacancy: Python Developer. Employer: Компания A. City: Москва. "
        "Salary: 100000-150000, RUR. URL: https://hh.ru/vacancy/1. "
        "Requirements: разаработка бэкенд"

    )
    assert str(vacancy_1) == expected_str


def test_vacancy_new_vacancy(vacancy_dict):

    vacancy = Vacancy.new_vacancy(vacancy_dict)
    assert vacancy.id == "106931996"
    assert vacancy.name == "PHP-разработчик"
    assert vacancy.url == "https://hh.ru/vacancy/106931996"


def test_vacancy_comparison(vacancy_2, vacancy_without_salary):
    assert vacancy_without_salary < vacancy_2


def test_vacancy_to_dict(vacancy_1):
    expected_dict = {
        'id': 1,
        'name': "Python Developer",
        'area': "Москва",
        'employer': "Компания A",
        'salary_from': 100000,
        'salary_to': 150000,
        'currency': 'RUR',
        'url': "https://hh.ru/vacancy/1",
        'requirement': "разаработка бэкенд"

    }
    assert vacancy_1.vacancy_to_dict() == expected_dict



def test_get_top_vacancies(vacancy_objects_list):

    top_vacancies = Vacancy.get_top_vacancies(vacancy_objects_list, 1)
    assert top_vacancies['id'] == '3'

def test_filter_by_word(vacancy_objects_list):

    keywords = ["Django"]
    result = Vacancy.filter_by_word(vacancy_objects_list, keywords)
    assert len(result) == 1
    assert result[0]['name'] == 'Django-разработчик'


def test_vacancy_salary_error(vacancy_dict):

    vacancy_dict["salary_to"] = -800
    with pytest.raises(ValueError, match="Зарплата не может быть отрицательной."):
        Vacancy.new_vacancy(vacancy_dict)

def test_vacancy_salary_comparison_wrong_object(vacancy_1, vacancy_dict):

    with pytest.raises(
        ValueError, match="Сравнение возможно только между объектами класса или между объектами класса и числами."
    ):
        print(vacancy_1 >= vacancy_dict)

