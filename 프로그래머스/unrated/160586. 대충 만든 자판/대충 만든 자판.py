def solution(keymap, targets):
    answer = [0 for _ in range(len(targets))]
    for idx, target in enumerate(targets):
        cnt = 0
        for t in target:
            tmp = [key.find(t) for key in keymap]
            if set(tmp) == {-1}:
                answer[idx] = -1
                break
            else:
                cnt = min([n for n in tmp if n != -1]) + 1
            answer[idx] += cnt
    return answer