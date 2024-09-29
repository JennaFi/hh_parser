from typing import Any

import requests

from src.api.base_parser import BaseParser


# from src.file_working.json_file import JSONfile


class HHParser(BaseParser):
    def __init__(self, api_params=None):
        super(BaseParser, self).__init__()

        self._BaseParser__connection_to_api(api_params)

    @staticmethod
    def _BaseParser__connection_to_api(api_params: dict) -> Any:

        url = "https://api.hh.ru/vacancies"
        headers = {"User-Agent": "HH-User-Agent"}

        response = requests.get(url, headers=headers, params=api_params)

        if response.status_code != 200:
            raise requests.RequestException

        return response

    @classmethod
    def load_vacancies(cls, keyword: str) -> list:
        params = {"text": keyword, "page": 0, "per_page": 100, "area": 1}
        vacancies = []

        while params.get("page") != 20:
            vacancies_hh = cls._BaseParser__connection_to_api(params).json()['items']
            vacancies.extend(vacancies_hh)
            params["page"] += 1

        return vacancies
