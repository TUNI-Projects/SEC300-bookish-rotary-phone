"""
Write a program that reads a file and filters all characters
except letter’s, numbers, commas and hyphen.
Print the result on the screen

file generated using https://commentpicker.com/string-generator.php
1094 lines in total
with lowercase, uppercase, numbers and special characters letters (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
"""


def filter_char(ch):
    if ord(ch) >= 48 and ord(ch) <= 57:
        # number
        return ch
    elif ord(ch) >= 97 and ord(ch) <= 122:
        # lowercase letter
        return ch
    elif ord(ch) >= 65 and ord(ch) <= 90:
        # uppercase letter
        return ch
    elif ord(ch) >= 44 and ord(ch) <= 45:
        # commas and hyphen
        return ch


def main():
    # read the whole file
    filtered_content = []
    with open('lipsum.txt') as file:
        for line in file:
            content = filter(filter_char, [*line])
            filtered_content += [*content]

    for c in filtered_content:
        print(c, end=" ")
    print("")


if __name__ == "__main__":
    main()
