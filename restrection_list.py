#  프로그래밍과 데이터 in python

# 리스트(list) : 변수에 값을 여러개 저장하고 싶을 떄 사용한다.

# 정수형이 담긴 리스트
numbers = [2, 3, 5, 7, 11, 13]   # 대괄호를 사용하여 변수 값을 여러개 지정할 수 있다.
# 이때, 2 3 5 7 11 13 을 리스트의 요소라고 한다.
# 문자형이 담긴 리스트
names = ["윤수", "혜린", "태호", "영훈"]
#    인덱스  0      1      2       3
# 마이너스 인덱스                   -1

# 인덱스(index) : 리스트의 요소의 위치(0부터 시작한다.)
# 인덱싱 (indexing) : 리스트 안의 요소를 하나씩 끄집어내고 싶을 때
print(names[1])
print(numbers[1] + numbers[3])
# 변수로 전환 가능하다
num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)

# 마이너스 인텍스 : 요소가 n개 인 경우 -n <= n-1 까지 사용 가능하다.
print(numbers[-1])

# 리스트 슬라이싱(list slicing) : 리스트의 일부를 잘라서 통째로 사용하는 방법
numbers[0:4]  # 리스트의 인덱스 0부터 3까지 자르는 것이다. [x:y] x 부터 y개 !
print(numbers[2:])  # 인덱스 2부터 끝까지 출력하자 !
print(numbers[:3])  # 인덱스 처음부터 3 - 1 인 요소까지 출력

new_list = numbers[:3]  # [2, 3, 5]
print(new_list[2])  # 5

# 요소 바꾸기
numbers[0] = 7  # 지정연산자 오른쪽에 있는 정수 7을 0번 요소 자리에 저장
print(numbers)

numbers[0] = numbers[0] + numbers[1]  # 지정연산자 오른쪽에 있는 인덱스 0번 + 1번
print(numbers)


# 리스트를 사용할 수 있는 함수
numbers = []
numbers.append(5)
numbers.append(8)  # 리스트의 값을 추가하고 싶을 떄 .append(추가하고 싶은 값)
print(numbers)
print(len(numbers))  # 리스트의 요소가 몇 개가 있는지 알 수 있음.
# length 의 줄임말

# 리스트 속 요소를 단순히 지우고 싶을 때 = del + list [삭제하고픈 요소의 인덱스번호 작성]
numbers = [2, 3, 5, 7, 11, 17, 19]
del numbers[3]
print(numbers)

# 리스트에 요소를 삽입하고 싶을 때
numbers.insert(4, 37)  # 4번 인덱스에 정수 37을 삽입한다.
# append는 무조건 오른쪽 끝에 값을 추가하는 것  (추가연산)
# insert는 원하는 위치에 값을 삽입하는 것입니다. (삽입연산)
print(numbers)

# 정렬
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# sorted
new_list = sorted(numbers)  # 정렬된 새로운 리스트가 리턴된다. sorted 함수는 기존의 numbers 리스트를 건드리지 않는다.
print(new_list)    # 리턴 해야함!

# 거꾸로 정렬
new_list = sorted(numbers, reverse=True)
print(new_list)


numbers = [19, 13, 2, 5, 3, 11, 7, 17]
print(numbers.sort())  # none   # sort 아무것도 리턴하지 않는다. numbers list 자체를 정렬하는 것

# sort
numbers.sort()
print(numbers)  # numbers 를 프린트해야함

numbers.sort(reverse=True)
print(numbers)
