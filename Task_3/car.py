class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start_car(self):
        print("Автомобиль заведён")

    def turn_off_car(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, car_type):
        self.car_type = car_type

    def set_color(self, color):
        self.color = color


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
