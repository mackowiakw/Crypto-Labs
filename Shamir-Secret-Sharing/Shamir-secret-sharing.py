from Crypto.Util import number
from numpy.linalg.linalg import solve
from secrets import randbits
from sys import exit


def stringify_pylonomial(coeffs):
    res = "f(x) = "
    for i in reversed(range(len(coeffs))):
        res += f"{coeffs[i]}x^{i} + "
    res = res.replace("^1", "")
    res = res.replace("x^0 + ", "")
    return res


def generate_shares(secret, n, t):
    """
    n - number of shares
    t - minimal number of shares reuqired to reconstruct secret
    """
    shares = []

    p = 0   # p size of the finite filed (p is prime)
    while not (p > n and p > secret):
        p = number.getPrime(len(bin(secret)) + 2)

    a = [secret] + [randbits(16)] * (t-1)   # 0 <= a_i <= 65536

    for i in range(n):
        share = sum(coeff * ((i+1)**power)
                    for power, coeff in enumerate(a)) % p
        shares.append(share)

    return shares, p


def reconstruct_secret(shares, n, t, p):
    A = []
    b = []

    for i in range(len(shares)):
        if shares[i] >= 0:
            A.append([(i+1)**k for k in range(t)])
            b.append(shares[i])
        if len(A) >= t:
            break

    if len(shares) != n:
        return "Invalid length of shares list"

    if len(A) < t:
        return f"Need at least {t} shares. Provided: {len(A)}"

    reconstructed_secret = int(solve(A, b)[0])
    while reconstructed_secret < 0:
        reconstructed_secret += p

    return f"Succes! Secret: {reconstructed_secret}"


def main():
    print("""
    Options:
    1. Generate shares
    2. Reconstruct secret
    0. Exit
    """)
    inp = input("Option number: ").strip().lower()
    print("\n")

    if inp in ("0", "q", "exit"):
        exit("Terminated by user")

    elif inp == "1":
        secret = int(input("Secret: ").strip())
        if secret > 2**16:
            exit(f"Secret too big. It must be lower than 2^16 ({2**16})")

        n = int(input("Number of shares: ").strip())
        t = int(input("Shares required to reconstruct secret: ").strip())

        if t > n:
            exit("Invalid number of shares requried to reconstruct secret")
            

        shares, prime = generate_shares(secret, n, t)

        print("\n" + f"{stringify_pylonomial(shares)}")
        print("\n" + f"prime: {prime}" + "\n")

        for i in range(len(shares)):
            print(f"s_{i+1}: {shares[i]}")

    elif inp == "2":
        n = int(input("Number of shares: ").strip())
        t = int(input("Shares required to reconstruct secret: ").strip())
        p = int(input("Prime used in modulo operation: ").strip())

        print(f"\nEnter know shares. If value is not know enter -1")

        shares = []
        for i in range(n):
            s = int(input(f"s_{i+1}: ").strip())
            shares.append(s)

        print("\n")
        secret = reconstruct_secret(shares, n, t, p)
        print(secret)

    else:
        exit("Invalid option number")


if __name__ == "__main__":
    main()
