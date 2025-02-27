words = []
for _ in range(3):
    word = input()
    words.append(word)

min_len = 20
for word in words:
    if min_len >= len(word):
        min_len = len(word)
    else:
        continue

print(min_len)
