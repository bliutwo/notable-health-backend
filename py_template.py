from typing import List


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


def find_and_replace_regex(text: str, reg_expr_str: str) -> str:
    """
    Write a function `find_and_replace_regex()` that takes two arguments:

    - a string text *t*
    - a regular expression string *r*

    For every instance of text that matches the regular expression *r*, put two asterisks on each side of it.

    Output: *t* with modifications as specified
    """
    return ""

def main():
    print("Hello world!")
    filename = "lorem_ipsum.txt"
    t = get_input_from_file_as_single_string(filename)

    # Example of built-in .replace()
    print(t.replace('ipsum', 'asdfghhljsdklfjkafjoiewajsajkbja'))




if __name__ == "__main__":
    main()
