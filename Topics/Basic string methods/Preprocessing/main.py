text = input()
for p in ',.!?':
    text = text.replace(p, '')
text = text.lower()
print(text)