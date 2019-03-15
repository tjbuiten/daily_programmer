def encode(text):
    characters = list(text)
    encoded = list("")
    for character in characters:
        number = ord(character)
        if 88 < number <= 90:
            number = 65 - (90 - number)
        if 120 < number <= 122:
            number = 97 - (122 - number)
        encoded.append(chr(number + 2))
    return ''.join(encoded)


def decode(text):
    characters = list(text)
    decoded = list("")
    for character in characters:
        number = ord(character)
        if 65 <= number < 67:
            number = 90 + (number - 65)
        if 97 <= number < 99:
            number = 122 + (number - 97)
        decoded.append(chr(number - 2))
    return ''.join(decoded)


inputText = input("Post your text:\n")
inputFunction = input("Do you want to decode or encode?: \n")

if inputFunction == 'encode':
    print(encode(inputText))
else:
    print(decode(inputText))
