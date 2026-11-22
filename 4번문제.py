# 4번 문제 : 유연근문제(프로그래머스)

def solution(schedules, timelogs, startday):
    answer = 0

    # 직원들을 한 명씩 확인
    for i in range(len(schedules)):

        # 직원의 희망 출근 시간
        time = schedules[i]

        hour = time // 100
        minute = time % 100

        # 출근 인정 시각 (희망 시간 + 10분)
        limit = hour * 60 + minute + 10

        # 선물을 받을 수 있는 직원인지 확인
        success = True

        # 7일 동안 출근 기록 확인
        for j in range(7):

            # 현재 요일 계산
            day = (startday + j - 1) % 7 + 1

            # 토요일, 일요일은 건너뛰기
            if day == 6 or day == 7:
                continue

            # 실제 출근 시각 가져오기
            real_time = timelogs[i][j]

            # 실제 출근 시각을 분으로 변환
            real_hour = real_time // 100
            real_minute = real_time % 100

            total = real_hour * 60 + real_minute

            # 인정 시각보다 늦었다면 지각!
            if total > limit:
                success = False
                break

        # 평일 5일 모두 지각하지 않았다면
        if success == True:
            answer += 1

    return answer
