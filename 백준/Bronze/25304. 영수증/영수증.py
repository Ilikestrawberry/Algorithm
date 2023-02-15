bill = int(input())
products = int(input())
price = 0
for i in range(products):
    p, n = map(int, input().split())
    price += p * n
if bill == price:
    print('Yes')
else:
    print('No')