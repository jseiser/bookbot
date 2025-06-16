from curses.ascii import isalpha
from stats import char_count, get_num_words, sorted_dict
import sys


def get_book_text(file_path: str) -> None:
    with open(file_path) as f:
        contents: str = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    num_words: int = get_num_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    x = char_count(contents)
    for l in sorted_dict(x):
        if isalpha(l["char"]):
            print(f"{l['char']}: {l['num']}")
    print("============= END ===============")


def main():
    get_book_text(sys.argv[1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main()
