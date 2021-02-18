import language_tables.sinhala as sinhala_table

def parse_letter(phonetic_code):
    vowel_code = phonetic_code % 20
    consanant_code = phonetic_code - vowel_code

    if consanant_code:
        return sinhala_table.consanants[consanant_code][0] + sinhala_table.gadgets[vowel_code]
    else:
        return sinhala_table.vowels[vowel_code]

    return '';

def parse_word(phonetic_codes):
    word = ''

    for phonetic_code in phonetic_codes:
        word += parse_letter(phonetic_code)

    return word