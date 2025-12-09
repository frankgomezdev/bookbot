import sys
from stats import count_words, count_chars, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_file_path = sys.argv[1]
    words = get_book_text(book_file_path)
    char_counts = count_chars(words)
    char_list = []
    for char, counts in char_counts.items():
        new_dict = {"char": char, "num": counts}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    count_words(words)
    print("--------- Character Count -------")
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()