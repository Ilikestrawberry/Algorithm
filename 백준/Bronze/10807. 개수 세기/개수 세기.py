length = int(input())
numbers = list(map(int, input().split()))
target = int(input())
result = numbers.count(target)
print(result)