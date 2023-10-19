score = int(input())

if score >= 90:
    print("A")
    # break
elif score < 90 and score >= 80:
    print("B")
    # break
elif score < 80 and score >= 70:
    print("C")
    # break
elif score < 70 and score >= 60:
    print("D")
    # break
else:
    print("F")