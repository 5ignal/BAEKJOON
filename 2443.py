n = int(input())
a = 1
c = 0

for i in range(n, 0, -1):
    b = 2 * n - a
    print(' ' * c + '*' * b)
    a += 2
    c += 1