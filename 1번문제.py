# 1번 문제 : 나머지 한 점의 좌표를 구해 직사각형 만들기

def solution(v):
    answer = []
    x_list = []
    y_list = []
    
    for point in v:
        x_list.append(point[0])
        y_list.append(point[1])
        
    for x in x_list:
        if x_list.count(x) == 1:
            answer.append(x)
            break
    
    for y in y_list:
        if y_list.count(y) == 1:
            answer.append(y)
            break

    return answer