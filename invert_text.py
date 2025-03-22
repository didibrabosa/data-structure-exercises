my_word = "pipa"
print(my_word)

word_4 = "a"
word_3 = "p"
word_2 = "i"
word_1 = "p"

if word_4 in my_word:
    print("have a latter 'a' here!")

if word_3 in my_word:
    print("have a latter 'p' here!")

if word_2 in my_word:
    print("have a latter 'i' here!")

if word_1 in my_word:
    print("have a latter 'p' here!")

while my_word:
    print(word_4 + word_3 + word_2 + word_1)
