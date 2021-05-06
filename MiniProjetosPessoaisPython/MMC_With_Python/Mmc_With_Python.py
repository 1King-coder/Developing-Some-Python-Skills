class Prime_Numbers:

    @staticmethod
    def is_prime(number_sent: int) -> bool:
        """
        Verify if the received number is prime.
        """

        divisors = 0
        for i in range(1, number_sent-1):
            if number_sent % i == 0:
                divisors += 1

        return divisors < 2

    def prime_numbers(self, number_sent: int) -> list:
        """
        Return all the prime numbers in the range sent .
        """
        prime_numbers: list = []
        for num in range(2, number_sent):
            if self.is_prime(num):
                prime_numbers.append(num)

        return prime_numbers


class MMC:
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

        for number_sent in self.numbers:
            if Prime_Numbers.is_prime(number_sent):
                _results[number_sent] = 1

            for prime_number in self.prime_numbers.prime_numbers(number_sent):
                if number_sent % prime_number == 0:
                    _results[prime_number] = self._multiple_exponent(
                        number_sent,
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
    def _multiple_exponent(number_sent: int, prime_number: int,
                           results_number: int = 0) -> int:
        """
        Calculate the how many times can the prime number divide
        the number sent.
        """

        while number_sent // prime_number != 0:
            results_number += 1
            number_sent = number_sent // prime_number

        return results_number


if __name__ == "__main__":
    mmc_nums = MMC([125, 17, 256, 625])

    print()
    print(mmc_nums.values_dict)
    print()
    print(mmc_nums.value)
    print()
