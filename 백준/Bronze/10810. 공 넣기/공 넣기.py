n_bucket, n_balls = map(int, input().split())
result = [0 for _ in range(n_bucket)]

for i in range(n_balls):
    s_i, e_i, n = map(int, input().split())
    result[s_i-1:e_i] = [n for _ in range((e_i-s_i+1))]
    
print(' '.join([str(_) for _ in result]))