score = int(input("Please enter your mark: "))
if 50 <= score < 60:
    print("Pass")
elif 60 <= score < 70:
    print("Merit")
elif score >= 70:
    print("Distinction")
else:
    print("Fail")