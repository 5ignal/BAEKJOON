# 첫째 줄에 N(2 ≤ N ≤ 100)이 주어진다.

# 2
# ** **
#  ***
# ** **

# 5
# *****       *****
#  *   *     *   *
#   *   *   *   *
#    *   * *   *
#     *   *   *
#    *   * *   *
#   *   *   *   *
#  *   *     *   *
# *****       *****

n = int(input())
first_space = 1
front_space = 1

if n > 2:
    a = n - 2
    for i in range(a):
        first_space += 2

print('*' * n + ' ' * first_space + '*' * n)

for i in range(0, n - 2):
    first_space -= 2
    print(' ' * front_space + "*" + " " * (n - 2) + "*" + " " * first_space + "*" + " " * (n - 2) + "*")
    front_space += 1

if n == 2:
    print(' ' * front_space + "*" + "*" + "*")
else:
    print(' ' * front_space + "*" + " " * (n - 2) + "*" + " " * (n - 2) + "*")

for i in range(n - 2, 0, -1):
    front_space -= 1
    print(' ' * front_space + "*" + " " * (n - 2) + "*" + " " * first_space + "*" + " " * (n - 2) + "*")
    first_space += 2

print('*' * n + ' ' * first_space + '*' * n)