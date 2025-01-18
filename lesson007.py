score = int(input("Please enter the credit score: "))

if 400 <= score < 600:
    print(f"{score} = Silver Card")
elif 600 <= score < 800:
    print(f"{score} = Gold Card")
elif 800 <= score <= 850:
    print(f"{score} = Platinum Card")
else:
    print(f"{score} = Invalid credit score")

