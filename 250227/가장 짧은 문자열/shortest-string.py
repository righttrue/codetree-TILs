words = []
for _ in range(3):
    word = input()
    words.append(len(word))

len_n = -min(words) + max(words)
print(len_n)
