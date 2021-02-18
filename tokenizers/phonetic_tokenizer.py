# A phonotic token will consist of information required to make a single sound. 
# so a combination of a consanant + vowel or just vowels or just consonants may contain.
# A token is a list [vowel part, consanant part]

from language_tables.english import consanant_combinations

vowel_symbols = ['a', 'e', 'i', 'o', 'u']

def tokenize(word):
    global vowel_symbols

    vowels, consanants = '', ''
    tokens = []

    def is_symbol_complete(letter):
        if letter == '|':
            return True

        if vowels and letter in vowel_symbols:
            return letter != vowels[-1]

        if letter not in vowel_symbols:
            if consanants:
                return consanants + letter not in consanant_combinations 
            if vowels:
                return True

        return False;

    def pack_token():
        nonlocal consanants, vowels

        tokens.append([consanants, vowels])
        consanants = ''
        vowels = ''

    word += '|'

    for letter in word:
        if is_symbol_complete(letter):
            pack_token()

        if letter in vowel_symbols:
            vowels += letter
        else:
            consanants += letter

    return tokens