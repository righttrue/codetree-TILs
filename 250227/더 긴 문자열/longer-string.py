word_1, word_2 = input().split(" ")

if len(word_1) > len(word_2):
    print(word_1, len(word_1))
elif len(word_1) == len(word_2):
    print("same")
else:
    print(word_2, len(word_2))