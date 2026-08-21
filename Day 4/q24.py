students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
total_sum=0;
for marks in students.values():
    total_sum +=marks
n = len(students)
print(total_sum/n)
