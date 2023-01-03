def swap_case(s):
    res = []
    for letter in s:
        if letter.isupper():
            res.append(letter.lower())
        else:
            res.append(letter.upper()) 
    return "".join(res)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
