def f(x):
    if x%2 == 0:
        return 0
    else:
        return 1
j = 1
for i in range(101):
    if f(i) == 1:
        print(i,end=' ')
        if i <=50:
            j *= i
print('\n')
print(j)
