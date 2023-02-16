def solution(t, p):
    answer = 0
    window = len(p)
    condi = [t[idx:idx+window] for idx in range(len(t)-window+1)]
    for c in condi:
        if int(c) <= int(p):
            answer += 1
    return answer