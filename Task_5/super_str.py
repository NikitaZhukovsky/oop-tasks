class SuperStr(str):
    def is_repeatance(self, s):
        if self == '':
            return False
        return (len(self) % len(s) == 0) and (s * (len(self) // len(s)) == self)

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]


repeatance = SuperStr('abc')
some_str = 'abc'
print(f"Текущая строка {repeatance} может быть получена повторениями {some_str}: {repeatance.is_repeatance(some_str)}")

palindrom = SuperStr('Abccba')
print(f"Строка является палиндромом: {palindrom.is_palindrom()}")
