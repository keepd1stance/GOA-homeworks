numbers = [3, 2, 1, 5, 7]
small = numbers[0]
for i in numbers:
    if i < small:
        small = i
print(small)


numbers1 = [3, 2, 1, 5, 7]
big = numbers[0]
for x in numbers:
    if x > big:
        big = x
print(big)


list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [1, 2, 3, 5]
abc = [list1[i] for i in list2]
print(abc)


ints = [1, 3, 5, 7]
strs = ['a', 'b', 'c', 'd']
list3 = []
for i in range(min(len(ints), len(strs))):
    list3.append(strs[i])
    list3.append(ints[i])
print(list3)



mixed = ['apple', 3, 'banana', 5, 'cherry', 7, 10, 20]
ints1 = []
strs1 = []
for i in mixed:
    if isinstance(i, int):
        ints1.append(i)
    elif isinstance(i, str):
        strs1.append(i)
print(ints1)
print(strs1)



numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
odd = [num for num in numbers1 and numbers2 if num % 2 != 0]
even = [num for num in numbers1 and numbers2 if num % 2 == 0]
print(sum(odd))
print(sum(even))


list11 = [1, 2, 3, 4, 5]
list22= [6, 7, 8, 9, 10]
list33= [11, 12, 13, 14, 15]
list44 = [16, 17, 18, 19, 20]

odd1 = []
even1 = []



lists = [list11, list22, list33, list44]

for lst in lists:
    for num in lst:
        if num % 2 == 0:
            even1.append(num)
        else:
            odd1.append(num)

print(odd1)
print(even1)



strings1 = ['apple', 'banana', 'cherry', 'date']
len1= [len(i) for i in strings1]
print(len1)




list13 = ['apple', 3, 'banana', 5]
list23= ['cherry', 7, 'date', 9]

int4 = [item for item in list13 + list23 if isinstance(item, int)]
str4 = [item for item in list13 + list23 if isinstance(item, str)]

print(int4)
print(str4)



listt = [1, 2, 3, 4, 5, 6]
listt1 = listt[::2]
print(listt1)