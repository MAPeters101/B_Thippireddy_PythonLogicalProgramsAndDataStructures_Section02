number = input("Enter a number: ")
start_checking = False
duck_number = False

for char in number:
    if char == '0':
        if start_checking:
            duck_number = True
            break
    else:
        start_checking = True;

print(f"{number} is a duck number: {duck_number}")

