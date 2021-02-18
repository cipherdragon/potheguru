import language_tables.english as english_table

vowels_table = {**english_table.vowels, **english_table.vowel_combinations}
consanants_table = {**english_table.consanants, **english_table.consanant_combinations}

def parse_token(token):
    consanants = token[0]
    vowels = token[1]

    if len(vowels) > 2:
        vowels = vowels[:2]

    return consanants_table[consanants][0] + vowels_table[vowels][0]

def parse_tokens(tokens):
    phonetics = []

    for token in tokens:
        phonetics.append(parse_token(token))
    
    return phonetics


    