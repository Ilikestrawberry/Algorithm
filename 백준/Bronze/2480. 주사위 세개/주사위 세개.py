input_ = list(map(int, input().split()))
cnt = 0
for idx, num in enumerate(input_):
    if cnt < input_.count(num):
        cnt = input_.count(num)
        pick_num = num

if cnt == 1:
    print(max(input_) * 100)
elif cnt == 2:
    print(1000 + pick_num * 100)
else:
    print(10000 + pick_num * 1000) 