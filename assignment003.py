number = input("Please enter th number to be searched: ")
search = input("Please enter the number to search for: ")
count = 0

for digit in number:
    if digit == search:
        count += 1

print(f"{search} occurs in {number} {count} times.")