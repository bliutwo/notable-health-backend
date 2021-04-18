from typing import List
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


def main():
    filename = "regexr_example.txt"
    t = get_input_from_file_as_single_string(filename)

    # Example of built-in .replace()
    # print(t.replace('the', 'THEEEEE'))

    # Example of built-in re.sub()
    pattern = "([A-Z])\w+"
    replace = "CAPITAL WORD"
    t = re.sub(pattern, replace, t)
    print(t)


if __name__ == "__main__":
    main()
