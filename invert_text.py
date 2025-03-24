# example 1:
def invert_text(word):
    return word[::-1]


# example 2:
def invert_text_2(word):
    invert = "".join(reversed(word))
    return invert


# example 3:
def invert_text_3(word):
    invert = ""
    for ch in word:
        invert = ch + invert
    return invert


test = invert_text_3(word="itaquaquisetuba")

print(test)
