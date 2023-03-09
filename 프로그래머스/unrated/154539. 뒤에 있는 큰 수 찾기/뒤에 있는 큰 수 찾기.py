from collections import deque

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    queue = deque()
    
    for i, num in enumerate(numbers):
        if queue:
            while queue and queue[-1][1] < num:
                answer[queue[-1][0]] = num
                queue.pop()
        queue.append((i, num))

    return answer