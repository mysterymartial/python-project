def string_concat(first_string, second_string):
    my_string = ""
    new_string = second_string + first_string
    return new_string[0:2] + new_string[5] + new_string[3:5] + new_string[2]


def string_addition(string, CONSTANT):
    string_lenght = len(string)
    middle = string_lenght // 2
    if string_lenght % 2 == 0:

        new_string = string[0:middle] + CONSTANT + string[middle:]
        return new_string
    else:
        return string + CONSTANT

    return string + CONSTANT


def string_manipulation(string):
    new_string1 = ""
    new_string2 = ""
    for char in string:
        if char.isupper():
            new_string1 += char
        if char.islower():
            new_string2 += char
    return new_string1 + new_string2


def character_count(string, letter):
    return (letter, string.count(letter))


def character_clean(string):
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char
    return new_string














