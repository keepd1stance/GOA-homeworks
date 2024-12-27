num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))


operation = input("შეიყვანეთ ოპერაცია (+ ან -): ")

if operation == "+":
    result = num1 + num2
    print(f"ჯამი: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"გადაჭრა: {result}")
else:
    print("არასწორი ოპერაცია. შეიყვანეთ მხოლოდ + ან -.")