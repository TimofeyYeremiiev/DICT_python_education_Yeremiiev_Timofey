print("Hello! My name is Giperaktivniy!")
print("I was created in 2022.")

print("Please, remind me your name.")
a = input("> ")
print(f"What a great name you have, {a}!")

print("Let me guess your age!")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("remainder3 > "))
remainder5 = int(input("remainder5 > "))
remainder7 = int(input("remainder7 > "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
b = int(input("> "))
for c in range(0, b+1):
    print(str(c) + "!")
print("Completed, have a nice day!")