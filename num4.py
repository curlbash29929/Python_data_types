#num 4
items = [
("apple", "fruit"),
("banana", "fruit"),
("carrot", "vegetable"),
("tomato", "vegetable"),
("milk", "dairy")
]

data = {}
for item, c in items:
    if data.get(c):
        data[c].append(item)
    else:
        data[c] = [item]

print(data)


