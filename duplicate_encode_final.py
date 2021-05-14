def duplicate_encode(word):
    return "".join("(" if word.lower().count(c) == 1 else ")" for c in word.lower())

print(duplicate_encode(""))

#test para ver como funciona el join
print("".join("xdd 9559 we ggg aa zs dsd"))