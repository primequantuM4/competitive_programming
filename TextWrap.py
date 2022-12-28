import textwrap

def wrap(string, max_width):
    lines = ""
    for letter in string:
        lines += letter
        if len(lines) == max_width:
            print(lines)
            lines = ""
    if len(lines) != 0:
        print(lines)
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
