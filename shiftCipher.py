import string


def create_shift_substitutions(n: int):
    """Make substitution tables of a shift of n."""
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n) % alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding


def encode(message, subst):
    return "".join(subst.get(x, x) for x in message.upper())


def printable_substitution(subst):
    mapping = sorted(subst.items())
    alphabet_line = "".join(letter for letter, _ in mapping)
    cipher_line = "".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)


def cryptoanalysis(message: str) -> str:
    """Try to find the key-shift of an english encrypted message."""
    # this needs improving
    matches = []
    words = []
    with open('words.txt', 'r') as f:
        for word in f:
            words.append(word[:-1].upper())
    for key in range(1, 27):
        _, decoding = create_shift_substitutions(key)
        x = encode(message.upper(), decoding)
        count = 0
        for word in words:
            if word in x:
                count += 1
        matches.append(count)
    return matches.index(max(matches)) + 1

                


if __name__ == "__main__":
    with open('text', 'r') as f:
        x = f.read()
    encoding, _ = create_shift_substitutions(10)
    y = encode(x, encoding)
    print(y)
    n = cryptoanalysis(y)
    _, decoding = create_shift_substitutions(n)
    x = encode(y, decoding)
    print(x)

