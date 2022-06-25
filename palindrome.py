def is_palindrome(word):
    right = ""
    # return len(word)
    for left in range(0, len(word)):
        
        right += word[len(word)-left-1]
    if word == right:
        return True;
    else:
        return False
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
