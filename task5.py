class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        out = []
        for i in words:
            s = set(i.lower())
            if s <= row1 or s <= row2 or s <= row3:
                out.append(i)
        return out