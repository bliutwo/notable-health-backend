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
    # pattern = r"([A-Z])\w+"
    orig = t[:]
    # re.sub(pattern, "CAPITAL WORD", t)
    print(t)
    re.sub(r"the", "CAPITAL WORD", t)
    print(t)
    assert(orig != t)


if __name__ == "__main__":
    main()
