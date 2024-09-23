from random import choice

from src.api.parser import HHParser
from src.file_working.json_file import JSONfile
from src.vacancy.vacancy import Vacancy



# json_saver = JSONfile()


class UI:

    @staticmethod
    def user_interaction():
        print("Вы используете помощник для поиска и обработки вакансий с сайта hh.ru")
        print("Выберите действие: ")
        print("1. Загрузить новые вакансии с сайта")
        print("2. Выбрать топ вакансий по зарплате")
        print("3.Отфильтровать вакансии по ключевым словам")
        print("4. Удалить вакансию из файла")
        print("5. Очистить файл")

        key_word = input("Введите слово для поиска: ")
        vacancies = HHParser.load_vacancies(key_word)
        vacancies_list = Vacancy.vacancy_processing(vacancies)
        print(f"Найдено {len(vacancies_list)} вакансий")

        json_worker = JSONfile(vacancies_list)


        print("Файл успешно сохранен")

        choice = 0

        while choice not in [1, 2, 3, 4]:
            try:
                choice = int(input("Введите 1, 2, 3 или 4: "))
                if choice not in [1, 2, 3, 4]:
                    print("Неправильная команда")
            except ValueError:
                print("Повторите ввод")

        match choice:

            case 1:
                key_word = input("Введите слово для нового поиска: ")
                vacancies = HHParser.load_vacancies(key_word)
                vacancies_list = Vacancy.vacancy_processing(vacancies)
                print(f"По новому запросу найдено {len(vacancies_list)} вакансий")

                JSONfile(vacancies_list)

                print("Файл успешно сохранен")

            case 2:
                top_v = int(input("Введите количество топ вакансий: "))
                top_vacancies = Vacancy.get_top_vacancies(vacancies_list, top_v)
                print(f"Топ-{top_v}-вакансии такие: {top_vacancies}")

            case 3:
                keywords = input("Введите слова для поиска: ").strip().split()
                filtred_vacancies = Vacancy.filter_by_word(vacancies=vacancies_list, keywords=keywords)
                print(f"Вакансии по вашему запросу такие: {filtred_vacancies}")

            case 4:

                vacancy_id = input('Введите id вакансиb: ')
                json_worker.delete_vacancy(vacancy_id)

                print(f"Вакансия с id {vacancy_id} была удалена.")




