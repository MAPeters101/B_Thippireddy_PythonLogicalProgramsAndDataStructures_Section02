number = input("Enter a number: ")
print(f"{number} is{' ' if number == number[::-1] else " not "}a palindrome")