number = int(input("Please enter a number: "))
result = 0
while number != 0:
    digit = number%10
    if digit in (3,6,9):
        result += digit
    number //= 10
print(f"The result is {result}")
