def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        wc_list = file_contents.split()
        print( len(wc_list) )

main()
