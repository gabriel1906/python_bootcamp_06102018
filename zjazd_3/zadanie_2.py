class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.worked_hours = 0

    def pay_salary(self):
        if self.worked_hours <= 8:
            to_pay = self.worked_hours * self.stawka
        else:
            to_pay = 8 * self.stawka + (self.worked_hours - 8) * self.stawka * 2
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours += hours

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}"


class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        # Employee.__init__(self, imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus = amount

    def pay_salary(self):
        to_pay = super().pay_salary()
        return to_pay + self.bonus

class Company:

    def __init__(self, name):
        self.name = name
        self.employees = set()

    def add_employee(self, employee):
        self.employees.add(employee)

    def size(self):
        return len(self.employees)

    def pay_all_salary(self):
        sum_ = 0
        for e in self.employees:
            sum_ += e.pay_salary()
        return sum_


def test_employee():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.imie == "Jan"
    assert employee.nazwisko == "Nowak"
    assert employee.stawka == 100.0


def test_employee_pay_salary_with_no_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0


def test_employee_pay_salary_with_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500


def test_employee_pay_salary_with_worked_hours_two_registrations():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(2)
    employee.register_time(3)
    assert employee.pay_salary() == 500


def test_employee_pay_salary_after_salary_was_payed():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


def test_employee_pay_salary_overhours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 8 * 100 + 2 * 2 * 100


def test_employee_pay_salary_overhours_two_registrations():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.register_time(5)
    assert employee.pay_salary() == 8 * 100 + 2 * 2 * 100


def test_premium_employee_pay_salary_with_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    assert employee.pay_salary() == 1500.0


def test_premium_employee_pay_salary_without_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500


def test_company():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google = Company("google")
    google.add_employee(employee)
    assert google.size() == 1
    assert google.pay_all_salary() == 500
    assert google.pay_all_salary() == 0
    employee2 = Employee('Krzysztof', 'Nowak', 200.0)
    employee2.register_time(5)
    employee.register_time(10)
    # google.pay_all_salary()
    google.add_employee(employee2)
    assert google.pay_all_salary() == 2200
