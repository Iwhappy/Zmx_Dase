s = input()
x = 0
y = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        x += 1
    else:
        y = max(y,x)
        x = 0
y = max(y,x)
if y == 0:
    print('不包含两个或两个以上连续出现的相同字符组成的字符串')
else:
    print('包含两个或两个以上连续出现的相同字符组成的字符串',y+1)
