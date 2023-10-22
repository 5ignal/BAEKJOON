# test_list = ["3 23 85 34 17 74 25 52 65",
#             "10 7 39 42 88 52 14 72 63",
#             "87 42 18 78 53 45 18 84 53",
#             "34 28 23 85 12 16 75 36 55",
#             "21 77 45 35 24 75 90 76 1",
#             "25 87 65 15 28 11 37 28 74",
#             "65 27 75 41 7 23 78 64 39",
#             "47 47 70 45 23 65 3 99 44",
#             "87 13 82 38 31 12 29 29 59"]

# def max(test_index):
#     num_list = map(int, test_list[test_index].split())
#     max_num = 0
#     index_num = 0
#     max_index_num = 0
#     for i in num_list:
#         if i > max_num:
#             max_num = i
#             max_index_num = index_num
#         index_num += 1
#     return [max_num, max_index_num]

# 입력 9개의 숫자에서 최대값이랑, 자리수를 가지고 있는 리스트를 리턴
# 그렇게 9개의 리턴 받은 리스트를 담고 있는 리스트에서
# 최대값을 가지고 있는 리스트[0]와 자리수를 가지고 있는 리스트[1]의 값을 프린트함

def max():
    num_list = map(int, input().split())
    max_num = 0
    index_num = 0
    max_index_num = 0
    for i in num_list:
        if i > max_num:
            max_num = i
            max_index_num = index_num
        index_num += 1
    return [max_num, max_index_num]

def max_list_max(max_list):
    max_num = 0
    index_num = 0
    max_index_num = 0
    max_index_num_col = 0
    for i in max_list:
        max_index_num_c = i[1]
        i = i[0]
        if i > max_num:
            max_num = i
            max_index_num = index_num
            max_index_num_col = max_index_num_c   
        index_num += 1
    print(max_num)
    print(max_index_num + 1, max_index_num_col + 1)

max_list = []

for i in range(9):
    max_list.append(max())

max_list_max(max_list)