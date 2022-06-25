# 파이션에서  = 는 '같다'라는 의미가 아니라 지정 연산자(aggignment operator)라는 의미라고 볼 수 있다.

x = 7

x = x + 1 # 지정연산자가 있으면 왼쪽은 보지말고, 처음에 오른쪽만 보면 된다. 따라서 8
x = x - 3 # 4
# x = 7 을 할당하게 되면 메모리 주소 어딘가에 7이 저장될 것입니당.

# 여기서 x + 1 을 하게 되면 8이 되는데, 이 8이 7이 저장된 메모리 주소가 아니라 다른 메모리 주소에 값이 저장됩니다.
# 그래서 이 x 가 7이 저장된 메모리 주소가 아닌 8이 저장된 메모리 주소를 가리키게 되기 때문에 충돌이 없다.


# 함수의 실행 순서

def hello():
    print("hello!")
    print("welcome to codeit!")
# python에서는 들여쓰기로 함수의 범위를 나타낸다.

# ex_1
print("함수 호출 전")
hello()
print("함수 호출 후")

# ex_2
def square(x):
    return x * x
print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")
# ex_3
def square(x):
    print("함수 시작")
    return x * x
    print("함수 끝") # return 문 이후의 dead code(죽은 코드)
# return 문 : 1_(함수가)무언가를 돌려주는 것. / 2_함수 즉시 종료하기
print(square(3))
print("hello world!")

# print 문과 return 문 비교
def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print_square(3)
print(print_square(3))  # return 값이 없기때문에 print_square(3) -> none으로 대체된다.
                        # 따라서 print(none)이기 떄문에 none이 나타난다.

get_square(3)  # 함수 호출 부분이 9로 대체 되지만, 출력을 나라내는 print 문이 없기 때문에 아무것도 출력이 되지 않는다.
print(get_square(3))  # 함수 호출 부분이 9로 대체되고, print(9)가 되기에 9가 출력이 된다.


# 옵셔널 파라미터(optional parameter) :
