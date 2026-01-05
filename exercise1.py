name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age")
else:
    ageGroup= "Underage" if age<18 else "Adult"
    print(f"Hello {name}, you are {age} years old and you are {ageGroup}")