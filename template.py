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

def find_and_replace(text: str, query: str, replace: str) -> str:
    return ""

def find_and_replace_regex(text: str, reg_expr_str: str) -> str:
    return ""

def main():
    print("Hello world!")
    filename = "lorem_ipsum.txt"
    print(get_input_from_file_as_list_of_lines(filename))
    print(get_input_from_file_as_single_string(filename))

if __name__ == "__main__":
    main()
