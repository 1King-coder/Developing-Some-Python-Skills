from Lcm_With_Python import Prime_Numbers


class LCD:
    def __init__(self, number_1: int, number_2: int):
        self.numbers = [number_1, number_2]
        self.prime_numbers = Prime_Numbers()

    @property
    def values_dict(self) -> dict:
        _results: dict = {}

        for prime_number in self.prime_numbers.prime_numbers(
                self.larger(self.numbers)):

            if self.numbers[0] % prime_number == 0 and \
                    self.numbers[1] % prime_number == 0:

                _results[prime_number] = self._multiple_exponent(
                    self.numbers,
                    prime_number
                )

        if not _results:
            return {'common denominators': None}

        return _results

    @property
    def value(self):
        """
        Returns the MMC result.
        """

        _total: int = 1

        for number, exponent in self.values_dict.items():
            if exponent is None:
                return None

            _total *= number**exponent

        return _total

    @staticmethod
    def larger(numbers: list) -> int:
        if numbers[0] < numbers[1]:
            return numbers[1]

        return numbers[0]

    @staticmethod
    def _multiple_exponent(sent_numbers: list, prime_number: int,
                           results_number: int = 0) -> int:
        """
        Calculate the how many times can the prime number divide
        both sent numbers.
        """

        while sent_numbers[0] % prime_number == 0 and \
                sent_numbers[1] % prime_number == 0:

            results_number += 1
            sent_numbers[0] //= prime_number
            sent_numbers[1] //= prime_number

        return results_number


print(LCD(8, 64).value)
