def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print( char_count(file_contents) )

def word_count(input_str):
    wc_list = input_str.split()
    return ( len(wc_list))
        
def char_count(input_str):
    working_str = input_str.lower()
    char_list = list(working_str)
    count_dict = {}

    for char in char_list:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

main()
