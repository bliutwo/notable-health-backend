from typing import List, Dict
import re


def get_input_from_file_as_list_of_lines(filename: str) -> List[str]:
    l = []
    with open(filename) as f:
        for line in f:
            l.append(line)
    return l


def get_input_from_file_as_single_string(filename: str) -> str:
    s = ""
    with open(filename) as f:
        for line in f:
            s += line
    return s


def word_count_dictionary(text: str) -> Dict[str, int]:
    words = text.split()
    d = {}
    for w in words:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return d


def main():
    f1 = "lorem_ipsum.txt"
    f2 = "regexr_example.txt"
    s = get_input_from_file_as_single_string(f1)
    t = get_input_from_file_as_single_string(f2)

    print(word_count_dictionary(s))

    # Example of built-in .replace()
    print(s.replace('the', 'THEEEEE'))

    # Example of built-in re.sub()
    pattern = "([A-Z])\w+"
    replace = "CAPITAL WORD"
    t = re.sub(pattern, replace, t)
    print(t)


if __name__ == "__main__":
    main()
