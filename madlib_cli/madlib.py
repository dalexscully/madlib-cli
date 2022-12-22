import re


def greeting():
    print("Thank you for coming to Madlib: A informative game where you can use random words and place into your story.")


def read_template(read_file):
    with open(read_file) as file:
        try:
            return file.read().strip()
        except FileNotFoundError:
            return 'File not Found'


def parse_template(string):
    new_string = string

    parts = tuple(re.findall(r"\{(.*?)\}", new_string))
    string = re.sub(r"\{(.*?)\}", "{}", new_string)

    print(string, parts)
    return (string, parts)


def merge(str, tuple):
    return str.format(*tuple)


if __name__ == "__main__":
    path = 'assets/dark_and_stormy_night_template.txt'
    print(read_template(path))



# greeting()
#
# template = read_template('assets/dark_and_stormy_night_template.txt')
#
# string, parts = parse_template(template)
#
# new_parts = []
#
# for word in parts:
#     new_word = input(f"Enter a {word}. ")
#     new_parts.append(new_word)
#
# madlib = merge(string, new_parts)
#
# with open('../assets/new_file.txt', 'w') as file:
#     file.write(madlib)
#
#
# print(f'Your madlib is: {madlib}')
