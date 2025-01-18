num = int(input("Enter a number: "))
number = num
sum = 0
while num > 0:
    sum += num%10
    num //= 10

print(f"The sum of the digits in {number} is {sum}.")