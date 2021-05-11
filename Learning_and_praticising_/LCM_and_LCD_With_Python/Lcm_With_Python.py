class Prime_Numbers:

    @staticmethod
    def is_prime(sent_number: int) -> bool:
        """
        Verify if the received number is prime.
        """

        divisors = 0
        for i in range(1, sent_number-1):
            if sent_number % i == 0:
                divisors += 1

        return divisors < 2

    def prime_numbers(self, sent_number: int) -> list:
        """
        Return all the prime numbers in the sent range.
        """

        prime_numbers: list = []
        for num in range(2, sent_number):
            if self.is_prime(num):
                prime_numbers.append(num)

        return prime_numbers


class LCM:
    def __init__(self, numbers: list):
        self.numbers: list = numbers
        self.prime_numbers = Prime_Numbers()

    @property
    def values_dict(self) -> dict:
        """
        Returns the least multiple numbers (prime numbers) and it's respective
        exponent in a dict form.
        """

        _results: dict = {}

        for sent_number in self.numbers:
            if Prime_Numbers.is_prime(sent_number):
                _results[sent_number] = 1

            for prime_number in self.prime_numbers.prime_numbers(sent_number):
                if sent_number % prime_number == 0:
                    _results[prime_number] = self._multiple_exponent(
                        sent_number,
                        prime_number
                    )

        return _results

    @property
    def value(self) -> int:
        """
        Returns the MMC result.
        """

        _total: int = 1

        for number, exponent in self.values_dict.items():
            _total *= number**exponent

        return _total

    @staticmethod
    def _multiple_exponent(sent_number: int, prime_number: int,
                           results_number: int = 0) -> int:
        """
        Calculate the how many times can the prime number divide
        the sent number.
        """

        while sent_number // prime_number != 0:
            results_number += 1
            sent_number //= prime_number

        return results_number


if __name__ == "__main__":
    mmc_nums = LCM([8, 64, 72])

    print('\n', mmc_nums.values_dict, '\n')

    print('\n', mmc_nums.value, '\n')
