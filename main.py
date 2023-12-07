from datetime import datetime


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Calculator Object: x = {self.x}, y = {self.y}"

    def divide(self):
        if self.y != 0:
            return self.x // self.y
        else:
            return "Error: Division by zero"

calc = Calculator(10, 3)
print(calc)
result = calc.divide()
print(result)

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Calculator Object: x = {self.x}, y = {self.y}"

    def divide(self):
        if self.y != 0:
            return self.x // self.y
        else:
            return "Error: Division by zero"

# Создание и использование объекта класса-родителя
calc = Calculator(10, 5)
print(calc)  # Вывод информации об объекте
print("Result of divide:", calc.divide())  # Вычисление и вывод результата

# Создание и использование объекта класса-потомка
def EnhancedCalculator(param, param1, param2):
    pass


enhanced_calc = EnhancedCalculator(10, 5, 2.0)
print(enhanced_calc)  # Вывод информации об объекте
print("Result of process_data:", enhanced_calc.process_data())  # Вычисление и вывод результата

class Automobile:
    def __init__(self, brand, power, seats):
        self.brand = brand
        self.power = power
        self.seats = seats

    def calculate_quality(self):
        Q = 0.1 * self.power * self.seats
        return Q

    def __str__(self):
        return f"Brand: {self.brand}, Power: {self.power} kW, Seats: {self.seats}, Quality: {self.calculate_quality()}"


class AdvancedAutomobile(Automobile):
    def __init__(self, brand, power, seats, year_of_manufacture):
        super().__init__(brand, power, seats)
        self.year_of_manufacture = year_of_manufacture

    def calculate_quality(self):
        current_year = datetime.datetime.now().year
        Q = super().calculate_quality()
        Qp = Q * 1.5 * (current_year - self.year_of_manufacture)
        return Qp

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Year of Manufacture: {self.year_of_manufacture}, Advanced Quality: {self.calculate_quality()}"

# Создание объекта базового класса
auto = Automobile("Tesla", 300, 4)
print(auto)

# Создание объекта класса-потомка
advanced_auto = AdvancedAutomobile("Tesla", 300, 4, 2018)
print(advanced_auto)
