"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, title (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Title (должность) на базе класса Worker;
в классе Title реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Title,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name, surname, title, income):
        self.name = name
        self.surname = surname
        self.title = title
        self.income = income

class Title(Worker):
    def __init__(self, name, surname, title, income):
        super().__init__(name, surname, title, income)
    def get_full_name(self):
        print(f"The worker's full name is {self.name} {self.surname}.")
    def get_job_title(self):
        return f"The worker's lob title {self.title}."
    def get_total_income(self):
        print(f"The worker's total income results in {sum(self.income.values())}.")

a = Title('Anna', 'Popova', 'Manager', income = {"wage": 100000, "bonus": 200000})
a.get_full_name()
print(a.get_job_title())
a.get_total_income()

