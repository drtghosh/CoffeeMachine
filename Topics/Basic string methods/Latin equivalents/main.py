name = input()


def normalize(n):
    diacritics = {
        'é': 'e',
        'ë': 'e',
        'á': 'a',
        'å': 'a',
        'œ': 'oe',
        'æ': 'ae',
    }

    # put your code here
    for key in diacritics:
        n = n.replace(key, diacritics[key])

    return n


print(normalize(name))