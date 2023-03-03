def solution(wallpaper):
    answer = [None, len(wallpaper[0]), 0, 0]
    lux = 0
    for i, w in enumerate(wallpaper):
        if '#' in w and answer[0] == None:
            answer[0] = i
        if 0 <= w.find('#') and answer[1] > w.find('#'):
            answer[1] = w.find('#')
        if '#' in w and answer[2] < i + 1:
            answer[2] = (i + 1)
        if '#' in w and answer[3] < (len(w) - w[::-1].find('#')):
            answer[3] = (len(w) - w[::-1].find('#'))
    return answer