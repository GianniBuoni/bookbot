def count_words(text: str) -> int:
    wc_list = text.split()
    return (len(wc_list))

def count_char(text: str) -> list[dict[str, int]]:
    chars = list(text.lower())

    # initial count
    char_count = {}
    for char in chars:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # map char_count into a list of dictionaries
    char_count = list(map(
        lambda x: {"char": x, "count": char_count[x] },
        char_count
    ))

    # sort the final count list
    return sorted(
        char_count,
        reverse = True,
        key = lambda x: x["count"]
    )
