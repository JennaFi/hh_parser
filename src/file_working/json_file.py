import json
import os

from src.file_working.base_file import BaseFile


class JSONfile(BaseFile):
    file_name: str
    path: str = '../data/'
    vacancies: list
    vacancies_ids: list
    full_path: str

    BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)

    def __init__(self, vacancies, file_name=None):
        self.__file_name = self.file_name if file_name else 'vacancies.json'
        self.__file_path = os.path.join(self.BASE_PATH, self.__file_name)
        self.__vacancies, self.__vacancies_ids = self.get_from_file()
        self.__vacancies.extend(vacancies)

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__vacancies, f, ensure_ascii=False, indent=4)

    def get_from_file(self):
        with open(self.__file_path, 'r', encoding="utf-8") as f:
            self.__vacancies = json.load(f)
            self.__vacancies_ids = [vacancy.get("id") for vacancy in self.__vacancies]

        return self.__vacancies, self.__vacancies_ids

    def save_to_file(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__vacancies, f, ensure_ascii=False, indent=4)

    def add_to_file(self, data: dict):
        self.get_from_file()
        if data.get('id') not in self.__vacancies_ids:
            self.__vacancies.append(data)
            self.__vacancies_ids.append(data.get('id'))

            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump(self.__vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy_id):
        self.__vacancies = [vacancy for vacancy in self.__vacancies if vacancy.get('id') != vacancy_id]
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__vacancies, f, ensure_ascii=False, indent=4)

    def delete_all(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            pass
