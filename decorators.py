import os

os.system('COLOR B')


def is_prime(func):
    def wrapper(a, b, c):
        n = func(a, b, c)

        for i in range(2, n):
            if not n % i:
                return 'Составное'

        return 'Простое'

    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


result = sum_three(2, 3, 6)
print(result)

try:
    os.system('PAUSE')
except:
    os.system('CLS')
