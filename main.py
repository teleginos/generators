from itertools import combinations


def all_variants(text):
    length = len(text)
    for elem in range(length):
        for j in range(elem + 1, length + 1):
            yield text[elem:j]


if __name__ == '__main__':
    a = all_variants('abc')
    for i in a:
        print(i)
