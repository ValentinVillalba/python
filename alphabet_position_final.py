def alphabet_position(text):
    return ' '.join(str(ord(i.lower()) - ord("a") + 1) for i in text if i.isalpha())

print(alphabet_position("ab c d efg ?? ! -"))