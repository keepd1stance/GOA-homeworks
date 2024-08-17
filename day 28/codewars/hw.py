#codewarsss
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = 5
    

def make_upper_case(s):
    return s.upper()

s = "hello"



def multiply(a, b):
    return a * b

a = 5 
b = 10




def invert(lst):
    inverted_list = []
    
    for x in lst:
        inverted_value = -x
        
        inverted_list.append(inverted_value)
    return inverted_list




def find_smallest_int(arr):
    smallest = arr[0]
    
    for num in arr:
        if num < smallest:
            smallest = num
    
    return smallest