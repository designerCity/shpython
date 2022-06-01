
# greetings 리스트의 원소를 모두 출력하는 프로그램을 작성
n = 0 # 인덱스
greeting = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
while n <= 6:
    print(greeting[n])
    n+=1

# 화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램
temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
def fahrenheit_to_celsius(temperature_list):
    return (temperature_list - 32) * 5 / 9
x = 0
while x < 6:
    temperature_list[x] = round(fahrenheit_to_celsius(temperature_list[x]), 1)
    x+=1
    if x == 6:
        print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력

# 모범 답안
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1
print("섭씨 온도 리스트: {}".format(temperature_list))


# 환전 서비스
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: {}".format(prices))
def krw_to_usd(krw):
    return krw /1000

def usd_to_jpy(usd):
    return usd / 8 * 1000

n = 0
while n < len(prices):
    prices[n] = krw_to_usd(prices[n])  # 좌변의 변수를 다르게 정의해서 print를 사용하면 적용이 되지 않는다.
    n+=1

print("미국 화폐: {}".format(prices))


n = 0
while n < len(prices):
    prices[n] = usd_to_jpy(prices[n])
    n+=1

print("일본 화폐: {}".format(prices))

# numbers라는 빈 리스트를 만들고 리스트를 출력한다.
numbers = []
print(numbers)
# append를 이용해서
# numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)

print(numbers)

# numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
x = 0
while x < len(numbers):
    if numbers[x] % 2 != 0:
        del numbers[x]
    else:
        x+=1
print(numbers)

# numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
numbers.insert(0, 20)
print(numbers)

# numbers 리스트를 정렬한 후 출력한다.
numbers.sort()
print(numbers)


# 리스트에서 값의 존재 확인하기 : 어떤 값이 리스트에 있는지 확인하는 함수를 써보자!

# value 가 some_list 의 요소인지 확인

def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True 를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False 를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))

# 리스트에 값의 존재를 확인하는 법_2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

# 거꾸로 값이 없는지 확인하려면 in 앞에 not을 붙이면 됩니다.
print(7 not in primes)
print(12 not in primes)

# Nested list(리스트 안의 리스트)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)



# sort method
# some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔줍니다.
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)


# reverse method
# some_list.reverse()는 some_list 의 원소들을 뒤집어진 순서로 배치합니다
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)


# index 메소드
# some_list.index(x)는 some_list 에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

# remove 메소드
# some_list.remove(x)는 some_list 에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)


# for 반복문 (while 문과 비슷하지만 상황에 따라 더 깔끔할 수 있음)

my_list = [2, 3, 5, 7, 11]

for number in my_list:  # 변수 number 는 for 반복문에서 사용되는 루프변수 # 조건 부분이 없음
    print(number)  # for 반복문의 수행부분  # 반복적으로 실행되는 부분

i = 0
while i < len(my_list):
    print(my_list[i])
    i+=1


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)
# range 함수 : 1_파라티머를 한 개 쓰는 버전 2_파라미터를 2개 3_ 3개 쓰는 버전
# 간편하고 깔끔하고 메모리를 효율성이 좋음

# 1_파라미터를 1개
# for i in range(stop):
#     print(i) = 0부터 (stop -1)까지의 범위  # stop 번 반복하여 실행한다는 뜻임!
for i in range(10):
    print(i)

# 2_파라미터를 2개
# for i in range(start, stop):
#     print(i)
for i in range(3, 20):  # 3 ~ 10까지임!!!
    print(i)

# 3_파라미터를 3개
# for i in range(start, stop, step):
#     print(i)  = start 부터 stop - 1 까지의 범위, 간격 step
for i in range(3, 17, 3):
    print(i)


# 인덱스와 원소 출력
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in numbers:
    print("{} {}".format(numbers.index(i), i))

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력(모범답안)
for i in range(len(numbers)):
    print(i, numbers[i])


#
for i in range(11):
    x = 2 ** i
    print("2^{} = {}".format(i, x))

# 구구단
n = 1
for i in range(1, 10):
    for n in range(1, 10):
        x = n * i
        print("{} * {} = {}".format(i, n, x)) # 더 안에 있는 for 반복문이 주기를 결정한다.

# 피타고라스 삼조
for c in range(1, 400):
    for b in range(1, 400):
        for a in range(1, 400):
            if a < b < c and a ** 2 + b ** 2 == c ** 2 and a + b + c == 400:
                x = a * b * c
                print(x)

# 피타고라스 삼조(효율적인 모범답안)
for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)


# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers)):
    right = len(numbers) - left - 1
    numbers[right], numbers[left] = numbers[left], numbers[right]  # 위치 바꾸기
print("뒤집어진 리스트: "+ str(numbers))



