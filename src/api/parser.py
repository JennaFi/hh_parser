from src.api.base_parser import BaseParser
import requests

class Parser(BaseParser):
    def __init__(self):
        super().__init__()

    def get_connection_to_api(self):


        url = 'https://api.hh.ru/vacancies'
        headers = {"User-Agent": "HH-User-Agent"}

        response = requests.get(url, headers=headers, params=self)

        if response.status_code != 200:
            raise requests.RequestException(f'{response.status_code}')
        return response

    @classmethod
    def get_vacancies(cls, search_text):
        params = {
            'text': search_text,
            'search_field': 'name',
            'area': 1,
            'period': 1,
            'only_with_salary': True,
            'page': 0,
            'per_page': 100,
        }
        vacancies = []

        while params.get('page') != 20:
            vacancies_per_page = cls.get_connection_to_api(params).json()['items']
            vacancies.extend(vacancies_per_page)
            params['page'] += 1

        # for vacancy in vacancies:
        #     print(
        #         f"Вакансия: {vacancy['name']}, Компания: {vacancy['employer']['name']}, URL: {vacancy['alternate_url']}")
        return vacancies

hh_cl = Parser()

print(hh_cl.get_vacancies('python'))










