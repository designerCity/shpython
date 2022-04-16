# aliasing

x = 5
y = x
y = 3
print(x)
print(y)


# python 에서 어떤 값을 변수에 저장하면 그 값에 이름표를 주는 것과 같다.
# 정수 5 는 x라는 이름표와 y라는 이름표를 동시에 달고 있는 것이다.
# 그랬다가 y = 3 을 지정해주면 5의 y 이름표가 3의 y 이름표로 이동
# 한 이름표는 한 곳에만 달릴 수 있다.

x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

# [2, 3, 5, 7, 11]list 에 x 라는 이름표가 붙고
# [2, 3, 5, 7, 11]list 에 y 라는 이름표가 붙어서 [2, 3, 5, 7, 11]list 는 x, y 이름표를 가지게 된다.
# [2, 3, 5, 7, 11]list 의 인덱스 2번이 4로 바뀌어서 [2, 3, 4, 7, 11]list 가 된다.
# 바꾼 리스트 [2, 3, 4, 7, 11]list 가 x, y 이름표를 가지고 있기 때문에
# print(x), print(y) 모두 [2, 3, 4, 7, 11]을 출력하게 된다.
# 이때 y 를 x 의 가명(alias)라고 한다.

# y 를 바꾸면서 x 값을 그대로 유지하기 위해서는 list 함수를 활용하면 된다.
x = [2, 3, 5, 7, 11]
y = list(x)
# list 함수의 역할은 기존의 리스트를 복사해주는 역할을 한다.
# 이떄의 y는 x 의 가명(alias) 가 아니다.
y[2] = 4
print(x)
print(y)


# list 와 문자열

# list 는 어떤 자료형을 나열한 것
# 문자열은 문자를 나열한 것

# 공통점
# 1_indexing

# list
alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

# 문자열
alphabet_sting = 'ABCDEFGHIJ'
print(alphabet_sting[0])
print(alphabet_sting[1])
print(alphabet_sting[4])
print(alphabet_sting[-1])

# 2_slicing
# 문자열도 list 슬라이싱처럼 문자열 슬라이싱 된다. 결과값이 새로운 문자열이냐 새로운 리스트이냐의 차이이다.

# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])


# 3_덧셈 연산
# 문자열을 연결하듯, list를 연결하는 것도 가능하다.

str_1 = 'hello'
str_2 = 'world'
str_3 = str_1 + str_2
print(str_3)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

# 3_len 함수
print(len(str_3))  # 문자열의 길이도 확인 가능하다.

print(len(list_3))

# 4_문자열은 리스트와 달리 수정이 불가능하다(이용가능하지만, 수정은 불가능하다.)

# 5_for 반복문
# 두 자료형은 공통적으로 인덱싱이 가능합니다. 따라서 for 반복문에도 활용할 수 있습니다.
# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)

# 실습과제 1-1000까지 각 자리수를 모두 더해라
# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)  # list 를 문자열로 바꾸기!

    for digit in str_num:
        total += int(digit)  # ()를 써야하는지, []를 써야하는지 구분 잘 하기!

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)

# 실습과제
# 주민등록번호 보안 프로그램
# 오답
# def mask_security_number(security_number):
#    list_security_number = list(security_number)
#    if len(security_number) == 13:
#        list_security_number[11] = "*"
#        list_security_number[12] = "*"
#        list_security_number[13] = "*"
#        list_security_number[14] = "*"
#        total = str(list_security_number)
#        return total
#    else:
#        list_security_number[10] = "*"
#        list_security_number[11] = "*"
#        list_security_number[12] = "*"
#        list_security_number[13] = "*"
#        total = str(list_security_number)
#        return total

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


# def is_palindrome(word):
#     # 리스트화
#     list_word = list(word)
#     # 뒤집기
#     if len(list_word) == 0:
#         x = len(list_word) / 2
#         for i in range(x):
#             j = len(list_word) - i - 1
#             list_word[i], list_word[j] = list_word[j], list_word[i]
#     if len(list_word) == 1:
#         y = (len(list_word) - 1) / 2
#         for i in range(y):
#             j = len(list_word) - i - 1
#             list_word[i], list_word[j] = list_word[j], list_word[i]
#         # 결과가 바뀐 list_word 이것도 리스트다.
#         # word 가 뒤집힘
#     total_str = ""
#     for i in range(len(word)):
#         total_str += list_word[i]
#
#     if total_str == word:
#         return True
#     else:
#         return False


def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

def is_palindrome(word):

  # 코드를 입력하세요.

  list_word = list(word)

  reversed_list = list_word[::-1]

  if list_word == reversed_list:

    return "true"

  else:

    return "false"


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
