#num 5

data = [
{"student": "Alice", "subject": "Math", "grade": 5},
{"student": "Bob", "subject": "Math", "grade": 4},
{"student": "Alice", "subject": "History", "grade": 3},
{"student": "Bob", "subject": "History", "grade": 5},
]
data2 = {}

for _ in data:
    sub = _.get('subject')
    if sub not in data2:
       data2[sub] = {}
    data2[sub][_.get('student')] = _.get('grade')

print(data2)
