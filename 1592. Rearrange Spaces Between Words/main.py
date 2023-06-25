def reorderSpaces(text):
    spaces_count = text.count(' ')

    while text[0] == ' ':
        text = text[1:]

    while text[-1] == ' ':
        text = text[:-1]

    while '  ' in text:
        text = text.replace('  ', ' ')

    words_count_minus_one = text.count(' ')
    if words_count_minus_one == 0:
        text = text.replace(' ', '')
        return text + ' ' * spaces_count
    avg = spaces_count // words_count_minus_one
    left = spaces_count % words_count_minus_one
    return (' ' * avg).join(text.split(' ')) + left * ' '




print(reorderSpaces("  this   is  a sentence "))
print(reorderSpaces("g"))
print(reorderSpaces(" g "))
print(reorderSpaces(" practice   makes   perfect"))

