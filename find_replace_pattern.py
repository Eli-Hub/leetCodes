from typing import List

# def constructRectangle(area: int) -> List[int]:
#     w = int(area ** 0.5)
#     while area % w != 0:
#         w -= 1
#     return [area // w, w]


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]: # type: ignore
    result = []

    for word in words:
        lookup =dict()
        query = ''
        print(f"words[word]: {word}")
        for i in range(len(word)):
            if word[i] not in lookup:
                lookup[word[i]] = pattern[i]
            query += lookup[word[i]]
            # print(lookup, query)

        if len(set(lookup.values())) == len(lookup) and query == pattern:
            result.append(word)
            print(lookup)





words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"


print(findAndReplacePattern(words, pattern)) # type: ignore
