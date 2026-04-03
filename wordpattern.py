class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(s)>=1 and len(s)<=300:
            if len(pattern) != len(words):
                return False
        MapCharToWord = {}
        MapWordToChar = {}
        for c, w in zip(pattern, words):
            if c in MapCharToWord and MapCharToWord[c] != w:
                return False
            if w in MapWordToChar and MapWordToChar[w] != c:
                return False
            MapCharToWord[c] = w
            MapWordToChar[w] = c

        return True