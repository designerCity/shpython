# 사전  (dictionary)
# list 는 순서의 개념이 있지만 사전에는 순서의 개념이 없다
# list 의 index 는 0,1,2,3 등의 정수값 # 사전의 key 는 정수형일 필요가 없다.

# pair 쌍 (key - value 쌍) (키 - 값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))
print(my_dictionary[3])

# 새로운 쌍을 추가

my_dictionary[9] = 81 # 9:81을 추가하는 것과 같다.
print(my_dictionary)


# 실습과제
vocab_dictionary = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab_dictionary)
# 문자열은 ''나, "" 안에 넣는 것 까먹지 않기
# vocab_dictionary['privilege', 'principle'] = '특권', '원칙'  # 이렇게 묶으면 묶여서 나온다
vocab_dictionary['privilege'] = '특권'
vocab_dictionary['principle'] = '원칙'
print(vocab_dictionary)


# 사전 활용법
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동인',
    '딸': '이지영'
}

# 1_목록 확인법
print('이지영' in my_family.values())  # 이지영이 목록에 있는지 확인하는 법
print(my_family.keys())

for value in my_family.values():
    print(value)

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

for key, value in my_family.items():
    print(key, value)


# 사전을 뒤집어블기
# 아예 모르겠었음

def reverse_dict(dict):
    new_dict = {}

    # dict 의 key 와 value 를 뒤집어서 new_dict 에 저장
    for key, value in dict.items():
        new_dict[value] = key

    return new_dict  # 변환한 새로운 사전 리턴

# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환한 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))  # \n 은 문자열에서 줄바꿈을 의미한다.

# 투표 솔루션
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자',
         '최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수',
         '강승기', '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기',
         '김영자']

x = 0
y = 0
z = 0
# 후보별 득표수
for name in votes:
    if name == '김영자':
        x += 1
    if name == '강승기':
        y += 1
    if name == '최만수':
        z += 1


vote_counter = {'김영자': x,
                '강승기': y,
                '최만수': z
                }
print(vote_counter)


# 모범답안
# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)