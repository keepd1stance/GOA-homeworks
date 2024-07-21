def even(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    return sum

numbers = [1, 2, 3, 4, 5, 6]
print(even(numbers))



def reverse(s):
    rev_s = ""
    for i in s:
        rev_s = i + rev_s
    return rev_s

s = "goal oriented academy"
print(reverse(s))






def factorial(i):
    if i == 0 or i == 1:
        return 1
    return i * factorial(i - 1)


i = 4
print(factorial(i))






def together(list1, list2):
    together = []
    for element in list1:
        if element in list2 and element not in together:
            together.append(element)
    return together

list1 = [1, 2, 2, 4, 5]
list2 = [4, 5, 2, 4, 8]
print(together(list1, list2))  




def bigS(s):
    bigSS = 'aeiouAEIOU'
    return sum(1 for i in s if i in bigSS)


s = "GOAL oriented ACADEMY"
print(bigS(s))


def permutations(str1,str2):
    if sorted(str1) == sorted(str2):
        print(sorted(str1))
        print(sorted(str2))
        return True
    else:
        return False
    
print(permutations("goddamn", "damngod"))


def prime(num):
    counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter = counter + 1
    if counter == 2:
        return True
    else:
        return False
    
print(prime(11))


def sorted_by_lenght(listn):
    return sorted(listn, key=len)

print(sorted_by_lenght(["one", "two", "three", "four"]))
