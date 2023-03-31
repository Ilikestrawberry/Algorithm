def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    for i, p in enumerate(photo):
        for person in p:
            if person in name:
                answer[i] += yearning[name.index(person)]
    return answer