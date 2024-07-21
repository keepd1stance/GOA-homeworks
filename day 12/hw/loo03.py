a = int(input())
b = int(input())
c = int(input())

if a+b>c:
    print('one passes')
if a+c>b:
    print('two passes')
if b+c>a:
    print('three passes, and its a triangle')
else:
    print("its not a triangle")

    