# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 예제 입력 1
# 3 16

# 예제 출력 1
# 3
# 5
# 7
# 11
# 13

# for i in range(2, int(n ** 0.5)):
#     a = 1
#     while True:
#         if a < n:
#             a += 1
#             index = (i * a) - m
#             prime_num[index] = False
#         else:
#             break

m, n = map(int, input().split())

prime_num = [True] * (n + 1)

for i in range(int((n ** 0.5) + 1)):
    a = 2
    while True:
        if i < 2:
            prime_num[i] = False
            break
        elif (i * a) < (n + 1):
            prime_num[i * a] = False
            a += 1
        else:
            break

for i in range(m, n + 1):
    if prime_num[i] == True:
        print(i)