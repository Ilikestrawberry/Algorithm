def solution(n, m, section):
    answer = 1
    start = section[0]
    for s in section:
        if start + m <= s:
            answer += 1
            start = s
    return answer