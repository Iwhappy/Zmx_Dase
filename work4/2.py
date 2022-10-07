li = [1,2,3,4,5]
for i in range(len(li)):
    print(li[len(li)-i-1],end=' ' )
print('\n')
j = 0
while j < len(li):
    print(li[len(li)-j-1],end=' ' )
    j += 1
print('\n')
print(li[::-1])#切片
