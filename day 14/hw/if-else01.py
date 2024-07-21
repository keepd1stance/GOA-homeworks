year = int(input("enter year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("its leap year.")
else:
    print("its not leap year.")







print("")
print("")
print("")
print("")
print("")







num = int(input("enter number: "))


if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")