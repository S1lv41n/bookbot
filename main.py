from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    filepath = sys.argv[1]
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    word_counter = get_num_words (filepath)
    print ("----------- Word Count ----------")
    print (f"Found {word_counter} total words")
    char_counter, dict_list = get_num_char (filepath)
    print ("--------- Character Count -------")
    char_counter_sorted = dict_list.sort(reverse=True, key=lambda d: d["num"])
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print ("============= END ===============")


main()