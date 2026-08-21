students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
highest=float('-inf')
for name,marks in students.items():
    if marks>highest:
        highest=marks
        s_name=name
print(highest)
print(name)