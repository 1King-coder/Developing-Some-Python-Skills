import re


class Verify_CPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def __call__(self):
        return self._verify()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, num):
        num = re.sub(r'[^0-9]', '', num)
        if num[0]*11 == num:
            return False

        if len(num) < 11:
            return False

        self._cpf = num

    @staticmethod
    def formula(total):
        digit = 11 - (total % 11)
        return str(digit) if digit < 9 or digit > 2 else '0'

    def _digits(self):
        return self._digit_1(self.cpf)

    def _digit_1(self, cpf, total: int = 0, index: int = 0, seq: int = 10):
        if seq < 2:
            cpf_1 = cpf[:9] + self.formula(total)
            return self._digit_2(cpf_1)

        return self._digit_1(cpf, total+int(cpf[index])*seq, index+1, seq-1)

    def _digit_2(self, cpf, total: int = 0, index: int = 0, seq: int = 11):
        if seq < 2:
            cpf_2 = cpf[:10] + self.formula(total)
            return cpf_2

        return self._digit_2(cpf, total+int(cpf[index])*seq, index+1, seq-1)

    def _verify(self):
        if not self.cpf:
            return self.cpf

        return True if self._digits() == self.cpf else False


if __name__ == '__main__':
    cpf = Verify_CPF('850.657.930-93')()
    if cpf:
        print('\033[1;32mVALID\033[m')
        quit()

    print('\033[1;31mINVALID\033[m')
