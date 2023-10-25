T = int(input())
for i in range(T):
    word = list(input())
    if len(word) == 1:
        print(word[0]+word[0])
    else:
        print(word[0]+word[-1])
