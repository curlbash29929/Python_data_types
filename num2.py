#num2
text = input('text: ').split()
data = {}
for _ in text:
    data[_.lower()] = len([word.lower() for word in text if word == _.lower()])

print('statistics: ', data)
print('top 5 words: ', sorted(data)[:5])
