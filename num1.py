#num1
from statistics import mean

students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]
data = {}
for student in students:
    data[student.get('name')] = mean(student.get('grades'))

print('dict: ', data)
print('\ntop student: ', max(data))