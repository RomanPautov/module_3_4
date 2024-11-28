def single_root_words(root_words, *other_words):
    root_words = root_words.lower()
    same_words = []

    for words in other_words:
        word = words.lower()
        if root_words in word or word in root_words:
            same_words.append(words)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)