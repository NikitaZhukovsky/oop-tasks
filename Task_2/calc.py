class Math:
    def addition(self, first_number, second_number):
        try:
            return first_number + second_number
        except TypeError:
            print("Неверный ввод")

    def subtraction(self, first_number, second_number):
        try:
            return first_number - second_number
        except TypeError:
            print("Неверный ввод")

    def multiplication(self, first_number, second_number):
        try:
            return first_number * second_number
        except TypeError:
            print("Неверный ввод")

    def division(self, first_number, second_number):
        try:
            if second_number != 0:
                return first_number / second_number
            else:
                print("Деление на 0 недопустимо")
        except TypeError:
            print("Неверный ввод")


math_object = Math()

print(f"Cумма чисел: {math_object.addition(5, 4)}")
print(f"Разность чисел: {math_object.subtraction(5, 4)}")
print(f"Произведение чисел: {math_object.multiplication(5, 4)}")
print(f"Частное чисел: {math_object.division(5, 4)}")
print(f"Частное чисел: {math_object.division(5, 0)}")
