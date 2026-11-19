# 2번 문제 : 사라진 출석번호 찾기

def solution(n, numbers):
    answer = 0
    
    total = n * (n+1) // 2
    current = sum(numbers)
    
    answer = total - current
    
    return answer