from Crypto.Util import number
import re


def single_bits_test(n_str):
    return 9725 <= n_str.count('1') <= 10275


def long_series_test(n_str):
    return not ('1'*26 in n_str or '0'*26 in n_str)


def series_test(n_str):
    a = 2315 <= sum(1 for _ in re.finditer('(?=010)', n_str)) <= 2685
    b = 1114 <= sum(1 for _ in re.finditer('(?=0110)', n_str)) <= 1386
    c = 527 <= sum(1 for _ in re.finditer('(?=01110)', n_str)) <= 723
    d = 240 <= sum(1 for _ in re.finditer('(?=011110)', n_str)) <= 384
    e = 103 <= sum(1 for _ in re.finditer('(?=0111110)', n_str)) <= 209
    f = 103 <= sum(1 for _ in re.finditer('(?=0111111+0)', n_str)) <= 209

    g = 2315 <= sum(1 for _ in re.finditer('(?=101)', n_str)) <= 2685
    h = 1114 <= sum(1 for _ in re.finditer('(?=1001)', n_str)) <= 1386
    i = 527 <= sum(1 for _ in re.finditer('(?=10001)', n_str)) <= 723
    j = 240 <= sum(1 for _ in re.finditer('(?=100001)', n_str)) <= 384
    k = 103 <= sum(1 for _ in re.finditer('(?=1000001)', n_str)) <= 209
    l = 103 <= sum(1 for _ in re.finditer('(?=1000000+1)', n_str)) <= 209

    return all([a, b, c, d, e, f, g, h, i, j, k, l])


def poker_test(n_str):
    keys = [bin(x)[2:].rjust(4, '0') for x in range(16)]
    counts = dict.fromkeys(keys, 0)

    for i in range(len(n_str)//4):
        current = n_str[4*i: 4*(i+1)]
        counts[current] += 1

    return 2.16 <= 16/5000 * sum([i**2 for i in counts.values()]) - 5000 <= 46.17


def tests(n):
    n_str = bin(n)[2:]
    a = single_bits_test(n_str)
    b = series_test(n_str)
    c = long_series_test(n_str)
    d = poker_test(n_str)

    passed = "PASS" if all([a, b, c, d]) else "FAIL"

    a = "PASS" if a else "FAIL"
    b = "PASS" if b else "FAIL"
    c = "PASS" if c else "FAIL"
    d = "PASS" if d else "FAIL"

    print(f'Single bits test: {a}')
    print(f'Series test: {b}')
    print(f'Long series test: {c}')
    print(f'Poker test: {d}')
    print(f'ALL: {passed}')

    return all([a, b, c, d])


def main():
    p = number.getPrime(64)
    q = number.getPrime(64)

    while p % 4 != 3:
        p = number.getPrime(64)
    while q % 4 != 3:
        q = number.getPrime(64)

    N = p * q

    x = number.getRandomInteger(64)
    while x % p == 0 or x % q == 0:
        x = number.getRandomInteger(64)

    x0 = x ** 2 % N
    xi = x0 ** 2 % N

    result = ''
    while len(result) < 20000:
        xi_1 = xi ** 2 % N
        xi = xi_1
        result += bin(xi_1)[2:]

    result = result[:20000]
    result = int(result, 2)

    tests(result)


if __name__ == "__main__":
    main()
