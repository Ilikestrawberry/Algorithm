def solution(plans):
    answer = []
    saved_plans = []
    start_info = {}
    
    for idx, plan in enumerate(plans):
        o, s, d = plan
        h, m = map(int, s.split(':'))
        s = h * 60 + m
        plans[idx] = [o, s, int(d)]
        start_info[s] = [o, int(d)]
    
    plans = sorted(plans, key=lambda x: x[1])
    time = plans[0][1]
    
    while not (len(answer) == len(plans)):
        if saved_plans:
            saved_plans[-1][1] -= 1
            if saved_plans[-1][1] == 0:
                answer.append(saved_plans[-1][0])
                saved_plans.pop()
                
        if time in start_info:
            saved_plans.append(start_info[time])

        time += 1

    return answer