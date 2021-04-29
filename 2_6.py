def palabra_mas_larga(texto):
    tmp_word = ''
    longst_word = ''
    flex_pt = 0
    for i in range (len(texto)):
        if texto[i:i+1] == ' ' or (i+1) == len(texto):
            if (i + 1) == len(texto):
               tmp_word = texto[flex_pt : i + 1]
            else:
               tmp_word = texto[flex_pt : i ]
            flex_pt = (i + 1)
            if len(tmp_word) > len(longst_word):
                longst_word = tmp_word
    
    return longst_word

print(palabra_mas_larga("Hola como te va refdfdfds"))


