class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        base = ord('a')
        s = set()
        for w in words:
            transformed = str()
            for c in w:
                mos = table[ord(c) - base]
                transformed += mos
            s.add(transformed)
        return len(s)