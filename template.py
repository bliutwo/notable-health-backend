from typing import List

def get_input_from_file(filename: str) -> List[str]:
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
    print("Hello world!")
    filename = "patients.csv"
    print(get_input_from_file(filename))
    print(get_input_from_file_as_single_string(filename))

if __name__ == "__main__":
    main()
