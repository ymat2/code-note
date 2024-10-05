import cprime


def main():
    n = 50000
    cnt = 0
    for i in range(n):
        if cprime.isPrime(i + 1):
            cnt += 1

    print(cnt)


def isPrime(n):
    bool_ = True
    for i in range(2, n):
        if n % i == 0:
            bool_ = False
            break
    return bool_


def isPrimeSmart(n):
    bool_ = True
    for i in range(2, int(n**1 / 2) + 1):
        if n % i == 0:
            bool_ = False
            break
    return bool_


if __name__ == "__main__":
    main()
