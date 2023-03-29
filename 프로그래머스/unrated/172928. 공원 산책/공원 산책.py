def solution(park, routes):
    answer = [0, 0]
    for idx, p in enumerate(park):
        if 'S' in p:
            answer[0] = idx
            answer[1] = p.index('S')
            break
    
    for route in routes:
        direction, step = route.split()
        if direction == 'E':
            for s in range(int(step)):
                if answer[1]+1 > len(park[0])-1 or park[answer[0]][answer[1]+1] == 'X':
                    answer[1] -= s
                    break
                if answer[1]+1 <= len(park[0])-1 and park[answer[0]][answer[1]+1] != 'X':
                    answer[1] += 1
                    
        elif direction == 'W':
            for s in range(int(step)):
                if 0 > answer[1]-1 or park[answer[0]][answer[1]-1] == 'X':
                    answer[1] += s
                    break
                if 0 <= answer[1]-1 and park[answer[0]][answer[1]-1] != 'X':
                    answer[1] -= 1
                
        elif direction == 'S':
            for s in range(int(step)):
                if answer[0]+1 > len(park)-1 or park[answer[0]+1][answer[1]] == 'X':
                    answer[0] -= s
                    break
                if answer[0]+1 <= len(park)-1 and park[answer[0]+1][answer[1]] != 'X':
                    answer[0] += 1
        
        elif direction == 'N':
            for s in range(int(step)):
                if 0 > answer[0]-1 or park[answer[0]-1][answer[1]] == 'X':
                    answer[0] += s
                    break
                if 0 <= answer[0]-1 and park[answer[0]-1][answer[1]] != 'X':
                    answer[0] -= 1

    return answer