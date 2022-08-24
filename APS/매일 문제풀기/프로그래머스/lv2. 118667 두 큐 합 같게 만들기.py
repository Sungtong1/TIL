from collections import deque


def solution(queue1, queue2):
    answer = -2
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    target = (sum_queue1 + sum_queue2) // 2

    # 전부 합쳤을 때 홀수면 -1 리턴
    if (sum_queue1 + sum_queue2) % 2 == 1:
        answer = -1
        return answer

    for i in range(len(q1) * 3):
        if sum_queue1 == sum_queue2:
            return i
        if sum_queue1 > sum_queue2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum_queue1 -= tmp
            sum_queue2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            sum_queue2 -= tmp
            sum_queue1 += tmp

    return -1