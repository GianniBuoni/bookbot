from os import path
from lib.helpers import count_char, count_words

file_path = path.join("books", "frankenstein.txt")

def main(input_file):
    with open(input_file) as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        char_count = count_char(file_contents)

        print(f"--- Begin report of {input_file} ---\n")
        print(f"{word_count} word(s) found in this document.\n")
        
        for letter in char_count:
            print(f"The letter '{letter["char"]}' was found '{letter["count"]}' times.")

main(file_path)
