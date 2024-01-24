class Math:
    @staticmethod
    def addition(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            return first_number + second_number
        else:
            print("Неверный ввод")

    @staticmethod
    def subtraction(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            return first_number - second_number
        else:
            print("Неверный ввод")

    @staticmethod
    def multiplication(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            return first_number * second_number
        else:
            print("Неверный ввод")

    @staticmethod
    def division(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            try:
                if second_number != 0:
                    return first_number / second_number
                else:
                    print("Деление на 0 недопустимо")
            except ZeroDivisionError:
                print("Деление на 0 недопустимо")
        else:
            print("Неверный ввод")


math_object = Math()

print(f"Cумма чисел: {math_object.addition(5, 4)}")
print(f"Разность чисел: {math_object.subtraction(5, 4)}")
print(f"Произведение чисел: {math_object.multiplication(5, 4)}")
print(f"Частное чисел: {math_object.division(5, 4)}")
print(f"Частное чисел: {math_object.division(5, 0)}")
