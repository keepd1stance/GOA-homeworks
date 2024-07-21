num = 2

while num <= 20:
    print(num)
    num += 2






print("")
print("")
print("")
print("")
print("")








correct = 7

guessed = False

while not guessed:
    guess = int(input("guess number from 1 to 10: "))
    
    if guess == correct:
        print("you guessed!", correct)
        guessed = True
    else:
        print("try again")









print("")
print("")
print("")
print("")
print("")








correctpassword = "password123"


enteredpassword = ""

# Используем цикл while для запроса пароля у пользователя
while enteredpassword != correctpassword:
    enteredpassword = input("enter password: ")
    
    if enteredpassword != correctpassword:
        print("invalid password. try again!.")

print("access granted.")
