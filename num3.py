list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

c1 = [x for x in list1 if x in list2]
u1 = [x for x in list1 if x not in list2]
u2 = [x for x in list2 if x not in list1]

print('есть в обоих списках', c1)
print('только в первом:', u1)
print('только во втором', u2)