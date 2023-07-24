from Crypto.Util import number


def main():
    p = 2137
    q = 7321
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 0
    while number.GCD(e, phi) != 1:
        e = number.getPrime(8)

    d = number.getRandomInteger(7)
    while (e*d - 1) % phi != 0:
        d += 1

    print('\n')
    print(f'p = {p}, q = {q}')
    print(f'n = {n}, phi = {phi}')

    print('\n')
    print(f'Private key: e = {e}, n = {n}')
    print(f'Public key: d = {d}, n = {n}')

    message = "Nie to jest mała różnica, to by nic nie dało bo on był drugi w kulach. Nawet jak bym był pierwszy nie dało by nic. Bo ja bym musiał być pierwszy on by musiał być czwarty."
    print('\n', 'Original message:', message)

    ciphertext = [pow(ord(m), e, n) for m in message]
    print('\n', 'Ciphertext: ', ciphertext)

    decrypted = [pow(c, d, n) for c in ciphertext]
    print('\n', 'Decrypted: ', decrypted)

    decoded = ''.join([chr(c) for c in decrypted])
    print('\n', 'Decoded message:', decoded)


if __name__ == "__main__":
    main()
