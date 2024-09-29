from src.vacancy.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    __slots__ = (
        "id",
        "name",
        "area",
        "salary_from",
        "salary_to",
        "currency",
        "url",
        "employer",
        "requirement",

    )

    def __init__(self, id, name, area, salary_from, salary_to, currency, url, employer, requirement):
        self.id = id
        self.name = name
        self.area = area
        self.salary_from = self.__is_valid_salary(salary_from)
        self.salary_to = self.__is_valid_salary(salary_to)
        self.currency = currency
        self.url = url
        self.employer = employer
        self.requirement = requirement if requirement else ""


    def __str__(self):
        return (
            f"id: {self.id}. Vacancy: {self.name}. Employer: {self.employer}. City: {self.area}. Salary: {self.salary_from}-{self.salary_to}, {self.currency}."
            f" URL: {self.url}. Requirements: {self.requirement}")


    def __lt__(self, other):
        return self.salary_to < other.salary_to


    @classmethod
    def __verify_data(cls, other):

        if not isinstance(other, (int, cls)):
            raise ValueError("Сравнение возможно только между объектами класса или между объектами класса и числами.")
        return other if isinstance(other, int) else other.salary_to


    @staticmethod
    def __is_valid_salary(salary: float):

        if not salary:
            return 0

        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        return salary


    def __le__(self, other):
        salary_to = self.__verify_data(other)
        return self.salary_to <= salary_to

    def __ge__(self, other):
        salary_to = self.__verify_data(other)
        return self.salary_to >= salary_to


    def vacancy_to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'area': self.area,
            'employer': self.employer,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'url': self.url,
            "currency": self.currency,
            'requirement': self.requirement
        }


    @classmethod
    def vacancy_processing(cls, vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            vacancy_dict = {
                "id": vacancy.get("id"),
                "name": vacancy.get("name"),
                "area": vacancy.get("area").get("name"),
                "url": vacancy.get("alternate_url"),
                "employer": vacancy.get("employer").get("name"),
                "salary_from": vacancy.get("salary").get("from")
                if vacancy.get("salary") and vacancy.get("salary").get("from")
                else 0,
                "salary_to": vacancy.get("salary").get("to")
                if vacancy.get("salary") and vacancy.get("salary").get("to")
                else 0,
                "currency": vacancy.get("salary").get("currency")
                if vacancy.get("salary") and vacancy.get("salary").get("currency")
                else None,
                "requirement": vacancy.get("snippet").get("requirement"),
            }
            vacancies_list.append(vacancy_dict)
        return vacancies_list


    @classmethod
    def new_vacancy(cls, vacancy: dict):
        if type(vacancy) is dict and all(i in vacancy.keys() for i in cls.__slots__):
            return cls(**vacancy)


    @staticmethod
    def get_top_vacancies(vacancies: list[dict], top):

        sorted_vacancies = sorted(vacancies, key=lambda v: v.get('salary_to', 0), reverse=True)[:top]

        for top_vacancy in sorted_vacancies:
            return top_vacancy


    @staticmethod
    def filter_by_word(vacancies: list[dict], keywords: list):

        result = []

        for vacancy in vacancies:
            for keyword in keywords:
                if (keyword.lower() in vacancy.get("name", "").lower()
                        or keyword.lower() in vacancy.get("employer", "").lower() or keyword.lower()
                        in (vacancy.get("requirement") or "").lower()):
                    result.append(vacancy)

        return result


