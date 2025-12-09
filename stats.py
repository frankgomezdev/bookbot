def count_words(file_contents):
    word_list = file_contents.split()
    num_words = len(word_list)
    print (f'Found {num_words} total words')

def count_chars(file_contents):
    char_count = {}
    lowered_text = file_contents.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]