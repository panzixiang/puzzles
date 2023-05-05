from typing import List

from english_words import get_english_words_set
import re


web2lowerset = get_english_words_set(['web2'], lower=True)

def search(regex: str) -> List[str]:
    outlist: List = []
    for word in web2lowerset:
        if re.search(regex, word, re.IGNORECASE):
            outlist.append(word)
    return outlist


def main():
    while True:
        var = input("Please enter something: ")
        print(search(var))


if __name__ == "__main__":
    main()