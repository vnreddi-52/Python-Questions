dict_a = {
    "Anil":89,
    "Bhagya":57,
    "Catherine":70,
    "Darshan":49
}

highest=0;

for i in dict_a.values():
    if i>highest:
        highest=i

print(highest)

