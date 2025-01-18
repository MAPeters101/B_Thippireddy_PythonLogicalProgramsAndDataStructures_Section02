num = int(input("Enter a number: "))
is_duck_number = False

while num != 0:
    digit = num % 10
    if digit == 0:
        is_duck_number = True
        break
    num = num // 10

if is_duck_number:
    print('Duck Number')
else:
    print('Not a Duck Number')