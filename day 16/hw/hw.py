integers = [123, 14214, 1000, 51253]
integers.pop(3)
print(integers[2])



strings = ['huh', 'idk', 'ez', 'lol']
x = strings.pop(0)
print(x)
print(strings)


characters = ['banji', 'aomine', 'kaneki', 'tanjiro', 'hiro']
characters.pop(2)
z = characters.pop(3)
print(z)


integers1 = [1, 4, 5, 1, 5, 6, 5 ,3]
count = integers1.count(5)
print(count)


list1 = ['apple', 'juice', 'gumball', 'darwin', 'donald trump']
a = 0

for i in list1:
    a += i.count('a')

print(a)




booleans = [True, False, True, True, False]

true = 0

for true in booleans:
    if true:
        true += 1

print(count)





nested_list = [[1, 2], [3, 4], [3, 4], [5, 6, 7], [3, 4, 5]]

count = 0


for threefor in nested_list:
    if threefor == [3, 4]:
        count += 1



randomlist = [10, 12, 99, 51, 44, 32, 16, 64, 15, 42]

x = len(randomlist)
print(x)



daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

y = len(daysofweek)
print(y)


nested_list2 = [[1, 2], [3, 4], [3, 4], [5, 6, 7], [3, 4, 5]]

o = len(nested_list2)
print(o)