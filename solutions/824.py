class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        tail = 'a'
        ma = 'ma'
        for idx in range(len(words)):
            if words[idx][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                words[idx] += ma
            else:
                words[idx] = words[idx][1:] + words[idx][0] + ma
            words[idx] += tail
            tail += 'a'
        return ' '.join(words)
