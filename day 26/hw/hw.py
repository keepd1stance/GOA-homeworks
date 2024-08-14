# .upper() ფუნქცია გამოიყენება ტექსტის ყველა ასოს გასადიდებლად
text = "hello world"
print(text.upper())  # შედეგი: "HELLO WORLD"

# .lower() ფუნქცია გამოიყენება ტექსტის ყველა ასოს დასაპატარავებლად
text = "HELLO WORLD"
print(text.lower())  # შედეგი: "hello world"

# .capitalize() ფუნქცია პირველ ასოს ადიდებს, ხოლო დანარჩენებს ამცირებს
text = "hello world"
print(text.capitalize())  # შედეგი: "Hello world"


# append() ფუნქცია სიის ბოლოში ამატებს ახალ ელემენტს
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # შედეგი: [1, 2, 3, 4]

# pop() ფუნქცია სიის ბოლო ელემენტს შლის და აბრუნებს მას
numbers = [1, 2, 3]
removed_element = numbers.pop()
print(numbers)  # შედეგი: [1, 2, 3]
print(removed_element)  # შედეგი: 3

# insert() ფუნქცია საშუალებას იძლევა სიის ნებისმიერ პოზიციაზე ჩასვათ ახალი ელემენტი
numbers = [1, 2, 3]
numbers.insert(1, 7)
print(numbers)  # შედეგი: [1, 7, 2, 3]