def word_converter(word):
    count = 0
    mychar = {}

    if word.isalpha():
        word = word.lower()
        for count in range(len(word)):
            character = word[count]

            character_count = 0
            for char in word:
                if char == character:
                    character_count += 1
            mychar[character] = character_count
    return mychar


def word_convert(word):
    if word.isalpha():
        word = word.lower()
        return {character: word.count(character) for character in word}








