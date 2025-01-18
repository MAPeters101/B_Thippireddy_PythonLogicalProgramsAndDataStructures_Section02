num = int(input("Enter a number: "))
number = num
odd_sum = 0
even_sum = 0

while num > 0:
    digit = num%10
    if digit%2==0:
        even_sum += digit
    else:
        odd_sum += digit
    num //= 10

print(f"""The sum of the odd digits of {number} is {odd_sum}.
The sum of the even digits of {number} is {even_sum}.""")
