# class vps_test():
#     def __init__(self):
#         self.vps_list = list()
#         self.for_num = int(input())

#     def input(self):
#         for i in range(self.for_num):
#             vps_input = input()
#             self.vps_list.append(vps_input)

#     def print(self):
#         for i in range(self.for_num):
#             vps = self.vps_list[i]
#             for j in range(len(vps)):
#                 vps = vps.replace("()", "")
#             if vps == "":
#                 print("YES")
#             else:
#                 print("NO")


# if __name__ == "__main__":
#     test = vps_test()
#     test.input()
#     test.print()


# class stack():
#     def __init__(self) -> None:
#         self.front_num = 0
#         self.stack_list = list()
#         for i in range(50):
#             self.stack_list.append(None)

#     def push(self, s:str):
#         self.stack_list[self.front_num] = s
#         self.front_num += 1

#     def pop(self):
#         print(self.stack_list[self.front_num - 1])
#         self.front_num -= 1
#         if self.front_num < 0:
#             print("NO")


class stack():
    def __init__(self) -> None:
        self.front_num = 0

    def push(self):
        self.front_num += 1
        return self.front_num

    def pop(self):
        self.front_num -= 1
        return self.front_num


if __name__ == "__main__":
    for_num = int(input())
    vps_list = list()
    
    for i in range(for_num):
        vps_input = input()
        vps_list.append(vps_input)
    
    for i in range(for_num):
        st = stack()
        result = 0
        break_flag = False
        vps = vps_list[i]
        for j in range(len(vps)):
            if "(" == vps[j]:
                result = st.push()
            else:
                result = st.pop()
                if result < 0:
                    print("NO")
                    break_flag = True
                    break
        if result == 0:
                print("YES")
        elif break_flag == True:
            break_flag = False
        else:
            print("NO")
            

# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()