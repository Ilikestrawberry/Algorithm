def solution(sequence):
    pos_dp = [sequence[0]]
    neg_dp = [-sequence[0]]
    
    for i in range(1, len(sequence)):
        pos_dp.append(max(sequence[i] * (-1) ** i, (pos_dp[-1] + sequence[i] * (-1) ** i)))
        neg_dp.append(max(sequence[i] * (-1) ** (i+1), (neg_dp[-1] + sequence[i] * (-1) ** (i+1))))

    answer = max(pos_dp + neg_dp)
    return answer