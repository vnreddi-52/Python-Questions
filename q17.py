numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in numbers:
    for num in row:
        total += num

print(total)