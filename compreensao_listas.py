def compreensao_listas():
    word = "string"

    list_words = []
    for w in word:
        list_words.append(w)

    print("List_words: ", list_words)

    list_words_2 = [w for w in word]
    print(f"List_words com compreehension: {list_words_2}")

    list_2 = [(x**2) for x in range(10) if x % 2 == 0]

    print(f"List compreehension com condicional e cálculo: {list_2}")