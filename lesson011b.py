num = int(input('Enter a number: '))
result = 0
while num != 0:
    digit = num%10
    if digit in (2,3,5,7):
        result += digit
    num //= 10
print('Sum of prime digits is', result)