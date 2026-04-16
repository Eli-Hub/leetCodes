from typing import List


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]: # type: ignore
    result = []

    for word in words:
        lookup = dict()
        query = ''
        for i in range(len(word)):
            if word[i] not in lookup:
                lookup[word[i]] = pattern[i]
            query += lookup[word[i]]

        if len(set(lookup.values())) == len(lookup) and query == pattern:
            result.append(word)

    return result




words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"


print(findAndReplacePattern(words, pattern)) # type: ignore
