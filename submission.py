from typing import List, Dict
import re


numbers_to_integers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def get_input_from_file_as_single_string(filename: str) -> str:
    s = ""
    with open(filename) as f:
        for line in f:
            s += line
    return s

def determine_first_number(text: str) -> int:
    pattern = "[Nn]umber ([a-z]+)"
    match = re.search(pattern, text)
    number = match.group(1)
    return numbers_to_integers[number]

def capitalize_first_letter(text: str) -> str:
    if text:
        c = text[0]
        if c.islower():
            c = c.upper()
            text = c + text[1:]
    return text

def transform(text: str) -> str:
    start = determine_first_number(text)
    pattern = "[Nn]umber [a-z]+"
    replace = "INSERTION_PLACE"
    output = re.sub(pattern, replace, text)
    l = output.split("INSERTION_PLACE")
    ans = ""
    for i, s in enumerate(l):
        if i == 0:
            ans += s
        else:
            ans += '\n'
            ans += str(start)
            ans += '. '
            # Remove extra whitespace on left side of string
            s = s.lstrip()
            ans += capitalize_first_letter(s)
            start += 1
    return ans


def write_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


def main():
    input_filename = "input.txt"
    input = get_input_from_file_as_single_string(input_filename)

    output = transform(input)
    print(output)

    output_filename = "output.txt"
    write_to_file(output, output_filename)


if __name__ == "__main__":
    main()
