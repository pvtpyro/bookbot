from stats import get_num_words, get_char_count, pretty_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]
    contents = get_book_text(path)
    num_words = len(get_num_words(contents))
    num_each_char = get_char_count(contents)
    report = pretty_dict(num_each_char)

    

    print(f"Found {num_words} total words")
    for i in report:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')

main()