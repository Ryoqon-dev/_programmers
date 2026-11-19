# 3번 문제 : 비밀번호의 숫자 합 구하기

def solution(password):
    answer = 0
    
    for i in range(0, len(password)):
        if password[i].isdigit():
            answer += int(password[i])
    
    return answer

# 테스트 코드
print(solution("a1b2c3"))     # 예상 결과: 6
print(solution("hello2026"))  # 예상 결과: 10
print(solution("ABC"))        # 예상 결과: 0
print(solution("9a8b7"))      # 예상 결과: 24
print(solution("12345"))      # 예상 결과: 15