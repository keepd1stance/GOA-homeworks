def longest_word1(words):
    if not words:
        return ""
    
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


words = ["apple", "banana", "cherry", "date", "elderberry"]
print(longest_word1(words))  


def nums(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number * number)
        else:
            new_list.append(number * 2)
    return new_list


numbers = [1, 2, 3, 4, 5, 6]
transformed = nums(numbers)
print(transformed) 