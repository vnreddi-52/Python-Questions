S = input()
words = S.lower().split()
small = words[0]
for i in range(len(words)):
    if words[i]<small:
        small=words[i]
print(small)


