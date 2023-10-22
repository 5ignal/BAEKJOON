def prime(n):
    for i in range(2, n + 1):
        while True:
            if n % i == 0:
                n = n / i
                print(i)
            elif n == 1:
                return 0
            else:
                break

if __name__ == "__main__":
    prime(int(input()))