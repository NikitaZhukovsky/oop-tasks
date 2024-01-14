class SuperStr(str):
    def is_repeatance(self, s):
        if self == '':
            return False
        if len(self) % len(s) == 0 and (self[:len(s)] * (len(self) // len(s))) == self:
            return True
        return False

    def is_palindrom(self):
        if self.lower() == self.lower()[::-1]:
            return True
        return False


repeatance = SuperStr('abcabcabc')
some_str = 'abc'
print(f"Текущая строка {repeatance} может быть получена повторениями {some_str}: {repeatance.is_repeatance(some_str)}")

palindrom = SuperStr('abccba')
print(f"Строка является палиндромом: {palindrom.is_palindrom()}")
