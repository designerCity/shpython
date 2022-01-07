# 제어문

# while 반복문 : 반복적인 일을 할 때 사용!
# 반복문의 구조 : while 조건 부분:
#                     수행부분

i = 1
while i <= 3:
    print("im handsome!")
    i+=1

# while 반복문 문법
# 조건 부분 : 불린 값으로 계산되는 식. 조건부분이 참이면 수행 부분이 계속 반복하여 실행됨. ex) x < 3
# 수행 부분 : 반복적으로 실행하고 싶은 명령 (들여쓰기 필수!)

x = 0
while (x % 2) < 1 and x < 99:
    print(x + 2)
    x+=2

i = 1
while i <= 50:
    print(i * 2)
    i += 1

# 느므느므 어렵스므니다
i = 100
while i % 23 !=0: # != 아닐떄
    i+=1

print(i)



def is_evenly_divisible(number):
    return (number % 2 == 0) # =는 대입연산자 오른쪽의 값을 왼쪽에 대입시키는 것
                             # ==가 비교에x`서 같다. 즉, 왼쪽의 값과 오른쪽의 값이 같은가?라고 묻는 것.
    # 코드를 작성하세요.

    # 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(216))
print(is_evenly_divisible(317))




def calculate_change(payment, cost):
    # 코드를 작성하세요.
    x = payment - cost
    y = x // 50000
    print("50000원 지폐: {}장".format(y))
    z = (x- y * 50000) // 10000
    print("10000원 지폐: {}장".format(z))
    p = (x - y * 50000 - z * 10000) // 5000
    print("5000원 지폐: {}장".format(p))
    q = (x - y * 50000 - z * 10000 - p * 5000) // 1000
    print("1000원 지폐: {}장".format(q))


calculate_change(100000, 33000)

def calculate_change(payment, cost):
    change = payment - cost # 거스름돈 총액

    fifty_count = change // 50000 # 50000원 지폐
    ten_count = (change % 50000) // 10000 # 10000원 지폐
    five_count = (change % 10000) // 5000 # 5000원 지폐
    one_count = (change % 5000) // 1000 # 1000원 지폐
    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))

calculate_change(100000, 22000)
calculate_change(500000, 378000)

# if(만약~한다면) / else(그렇지 않으면) 문
# if 문 구조 : if 조건 부분: # 조건 부분 : 불린 값으로 계산되는 식
#            (들여쓰기)수행부분  # 수행 부분 : 조건을 충족하였을 때, 실행하고 싶은 명령
#            else:
#            수행부분 # 수행 부분 : 조건을 충족하지 않았을 때, 실행하고 싶은 명령

temperature = 16
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")

if temperature <= 10:
    print("자켓을 입는다.")
else:
    if temperature <= 15:
        print("긴팔을 입는다.")
    else:
        print("반팔을 입는다.")

score = 50
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

# elif 문 : if와 else 가 반복되는 비교적 복잡한 식에서 if + else = elif
if score >= 90:
    print("a")
elif score >= 80:
    print("b")
elif score >= 70:
    print("c")
elif score >= 60:
    print("d")
else:
    print("f")

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 코드를 쓰세요.
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")

# if 조건문:
#     # 들여써야 합니다.
# elif 조건문: #들여쓰면 안됩니다.
#     # 들여써야 합니다.
# else: # 들여쓰면 안됩니다.
print_grade(40, 45)

# 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력
number_8 = 0

while number_8 < 96:
    number_8 += 8
    if number_8 % 12 != 0:
        print(number_8)

# 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램
i = 1
total = 0
while i < 999:
    i += 1
    if i % 2 == 0 or i % 3 == 0:
        total += i
print(total)

# 모범 답안
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:  # == 는 명제를 판별할 때 사용하는 것임. == / =을 구별하자!
        total += i  # i = i + 1과 동일
    i += 1  # i = i + 1과 동일

print(total)

# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요. 아래처럼 콘솔에 출력
x = 0
y = 0 # 약수 개수
n = 120

while x <= 120:
    x+=1
    if n % x == 0:
        print(x)
        y+=1 # 출력이 될 때마다, y값에 1개씩 더해진다.!!!

print("{}의 약수는 총 {}개입니다.".format(n, y))


# 1988년 은행에 5,000만원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,
# 동일 아저씨와 미란 아주머니 중 누구의 말을 듣는 것이 좋았을지 판단
x = 50000000 # 1988년의 최초 자본금

n = 1 # n = 몇 년쨰인지
while n <= 28:
    x*=1.12 # 은행 이율 = 12%
    n+=1

if x <= 1100000000:
   y = round(1100000000 - x)
   print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(y))
else:
   z = round(x - 1100000000)
   print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(z))
# feedback
# round 함수 대신에 int 를 표현하여 정수로 표현할 수도 있다.
# 상수 표현은 대문자로 하기 / 변수 표현도 똑바로
# 타인이 알아볼 수 있는 표현 사용하기.



# 모범답안

# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))



previous = 0
current = 1
n = 1 # n은 항

while n <= 50:
    print(current)
    temp = previous
    previous = current
    current = previous + temp
    n += 1


previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1

previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1


i=1
j=1
count = 0
print(i)
print(j)
while count <= 23:
    i = i + j
    print(i)
    j = j + i
    print(j)
    count += 1

x = 0  # x 단
y = 1  # 두 번째 곱하는 수

i = 1
while i <= 9:
    j = 1
    while j < 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    print("{} * {} = {}".format(i, j, i * j))
    i +=1

x = 0  # x 단
y = 1  # 두 번째 곱하는 수

i = 1
while i <= 9:
    j = 1
    while j < 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    i +=1
    print("{} * {} = {}".format(i, j, i * j))


# break 문 : 만약 while문의 조건 부분과 상관 없이 반복문에서 나오고 싶을 떄 사용.
#  while True:
#   i가 23의 배수면 반복문을 끝냄
#     if i % 23 == 0:
#         break
#     i = i + 1
## 115

#  continue 문 : 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶을 떄
#  i = 0
#
# while i < 15:
#     i = i + 1
#
#     # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
#     if i % 2 == 1:
#         continue
#     print(i)
# 2
# 4
# 6
# 8
# 10
# 12
# 14
