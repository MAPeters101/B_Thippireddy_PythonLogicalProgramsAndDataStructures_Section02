number = input("Please enter a number: ")
sum = 0

for digit in number:
    value = int(digit)
    if value <= 3:
        sum += value
    else:
        for i in range(2, value):
            if value%i == 0:
                break
            if i == value-1:
                sum += value
print(sum)


