import sys

from language_tables import english, sinhala
from tokenizers import phonetic_tokenizer
from parsers import phonetic_parser, language_parser


word = sys.argv[1]
tokens = phonetic_tokenizer.tokenize(word)
phonetic_codes = phonetic_parser.parse_tokens(tokens)
sinhala_word = language_parser.sinhala.parse_word(phonetic_codes)

print(sinhala_word)