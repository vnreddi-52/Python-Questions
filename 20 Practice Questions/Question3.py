S = input()
lowered = S.lower().split()
# print(S)
# print(lowered)
# lowered.sort()
first=lowered[0]

for word in lowered:
    if word < first:
        first=word
print(first)