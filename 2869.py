import math

# (top - down)
# 정상에 올라가서는 미끄러지지 않으니 미리 미끄러지는 미터를 빼줌
# 이걸 안하면 정상에 올라가서도 미끄러지기 때문에 회수가 증가됨
# (up - down)
# 하루에 올라갈 수 있는 미터

# math.ceil를 통해서 숫자 올림
# 5 1 6일때 1.25이 나옴 1 초과이니 2로 올려줌
# print(math.ceil(a))

def test(result):
    a = result * 10
    b = a % 10
    return int(b)

def result():
    up, down, top = map(int, input().split())
    result = (top - down) / (up - down)
    print(math.ceil(result))
    a = int(result)
    if test(result) >= 1:
        return a + 1
    else:
        return a

if __name__ == "__main__":
    print(result())
