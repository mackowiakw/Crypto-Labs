from Crypto.Util import number


def primitive_root(modulo):
    required_set = set(num for num in range (1, modulo) if number.GCD(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            return g


def main():
    # Generating n-g parameters
    n = number.getPrime(10)
    g = primitive_root(n)
    print(f'n = {n}, g = {g}')

    # Generating private keys
    x_private = number.getRandomInteger(16)
    y_private = number.getRandomInteger(16)
    print(f'x_private = {x_private}, y_private = {y_private}')

    # Generating public keys
    X_public = g ** x_private % n
    Y_public = g ** y_private % n
    print(f'X_public = {X_public}, Y_public = {Y_public}')

    # Generating common key
    x_key = Y_public ** x_private % n
    y_key = X_public ** y_private % n
    print(f'Common secret: {x_key} == {y_key}')


if __name__ == "__main__":
    main()
