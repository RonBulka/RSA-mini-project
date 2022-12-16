import number_theory_functions


def question1():
    a = 911
    b = 7879
    gcd, x, y = number_theory_functions.extended_gcd(a, b)
    print(f"gcd: {gcd}, x: {x}, y: {y}. (gcd = 911 * x + 7879 * y)")
    '''gcd: 1, x: -2733, y: 316 -> There is a way to exchange the money, Loki needs to give spiderman
       316,000,000 bills each one worth 7879 and spiderman needs to give Loki 2,733,000,000 bills each
       one worth 911 each'''


def question2():
    phi = 400  # Euler function on 1000
    d = number_theory_functions.modular_exponent(7896543, 74365753, phi)
    solution = number_theory_functions.modular_exponent(456456, d, 1000)
    print(solution)
    """The hundred digit of the number 456456^(7896543^74365753) is 0, we know from euler that 
       456456^(phi(1000)) mod 1000 = 1, so we want to look at only the relevant exponent which wont turn into 1 after
       mod 1000, that number is represented by d. So we then check solution = 456456^d mod 1000 and we get 16.
       is other words the hundred digit is 0."""


def question3():
    # We need to find q, p which give us N = q*p - p = 3491, q = 3499
    N = 12215009
    K = 3490 * 3498
    e = 3499
    c = 42
    d = number_theory_functions.modular_inverse(e, K)
    m = number_theory_functions.modular_exponent(c, d, N)
    print(m)  # 3023178
    """The encrypted massage is 42 and the decrypted massage is 3023178, only needed to find the prime factorization 
       of N and from there just follow the algorithm to decrypt a massage."""


def question4():
    # 991 is already a prime so |U991| = 990
    pass


def question5():
    p = 7919
    q = 6841
    N = p * q
    K = (p - 1) * (q - 1)
    e = number_theory_functions.generate_prime(10)
    d = number_theory_functions.modular_inverse(e, K)
    while not d:
        e = number_theory_functions.generate_prime(10)
        d = number_theory_functions.modular_inverse(e, K)
    m = 1337
    c = number_theory_functions.modular_exponent(m, e, N)
    print(f"massage: {m}, public key: {e}, encrypted massage: {c}")
    """massage: 1337, public key: 6328147487, encrypted massage: 43617655"""


if __name__ == '__main__':
    # question1()
    # question2()
    # question3()
    question5()
