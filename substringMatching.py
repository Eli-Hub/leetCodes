class Solution:
      def hasMatch(self, s: str, p: str) -> bool:
        a, b = p.split('*')
        l, r = s.find(a), s.rfind(b)
        # return l + len(a) - l < r and l != -1
        return l != -1 and l + len(a) - 1 < r