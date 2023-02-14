hour, minute = map(int, input().split())
d = int(input())

minute += d

while minute >= 60:
    minute -= 60
    hour += 1
    
if hour >= 24:
    hour -= 24
    
print(hour, minute)