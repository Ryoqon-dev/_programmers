# 7번문제 : 노란불 신호등
# 작성일 : 2026-11-23
# 난이도 : 레벨 1

from math import lcm


def solution(signals):
    # 모든 신호등의 상태가 반복되기까지 걸리는 시간
    last_second = 1
    for green, yellow, red in signals:
        period = green + yellow + red
        last_second = lcm(last_second, period)

    # range의 끝값은 포함되지 않으므로 1을 더해요.
    for second in range(1, last_second + 1):
        all_yellow = True

        for green, yellow, red in signals:
            period = green + yellow + red
            position = (second - 1) % period + 1

            is_yellow = green + 1 <= position <= green + yellow
            if not is_yellow:
                all_yellow = False
                break

        if all_yellow:
            return second

    return -1