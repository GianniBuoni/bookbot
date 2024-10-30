def main(input_file):
    with open(input_file) as f:
        file_contents = f.read()
        main_word = word_count(file_contents)
        main_char = char_count(file_contents)
        to_sort = split_dict(main_char)

        # start the sort
        to_sort.sort(reverse=True, key=on_sort)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{main_word} word(s) found in this document.\n")
        
        for letter in to_sort:
            print(f"The letter '{letter["letter"]}' was found '{letter["num"]}' times.")

def word_count(input_str):
    wc_list = input_str.split()
    return ( len(wc_list))
        
def char_count(input_str):
    working_str = input_str.lower()
    char_list = list(working_str)
    count_dict = {}

    for char in char_list:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

def split_dict(input_dict):
    list_dict = []
    for letter in input_dict:
        mini_dict = {}
        mini_dict["letter"] = letter
        mini_dict["num"] = input_dict[letter]
        list_dict.append(mini_dict)
    return list_dict

def on_sort(dict):
    return dict["num"]

main("./books/frankenstein.txt")
