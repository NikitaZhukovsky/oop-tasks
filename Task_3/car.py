class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    @staticmethod
    def start_car():
        print("Автомобиль заведён")

    @staticmethod
    def turn_off_car():
        print("Автомобиль заглушен")

    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            raise ValueError("Год должен быть положительным целым числом.")

    def set_type(self, car_type):
        if isinstance(car_type, str):
            self.car_type = car_type
        else:
            raise ValueError("Ошибочный ввод!")

    def set_color(self, color):
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Ошибочный ввод!")


car = Car("Black", "Universal", 2021)

car.start_car()
car.turn_off_car()

print(f"Год выпуска автомобиля: {car.year}")
car.set_year(2022)
print(f"Год выпуска автомобиля: {car.year}")

print(f"Тип автомобиля: {car.car_type}")
car.set_type("Sedan")
print(f"Тип автомобиля: {car.car_type}")

print(f"Цвет автомобиля: {car.color}")
car.set_color("Red")
print(f"Цвет автомобиля: {car.color}")
