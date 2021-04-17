from typing import List

def get_input_from_file(filename: str) -> List[str]:
    l = []
    with open(filename) as f:
        for line in f:
            l.append(line)
    return l

def main():
    print("Hello world!")
    filename = "patients.csv"
    print(get_input_from_file(filename))

if __name__ == "__main__":
    main()
