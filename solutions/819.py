class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        from string import ascii_letters

        modified = str()
        for c in paragraph:
            if c == " " or c in ascii_letters:
                modified += c
        words = modified.lower().split(" ")
        cnt = Counter(words)

        for word in banned:
            if word in cnt:
                del cnt[word]
        cnt = cnt.most_common()
        return cnt[0][0]
        # times = None
        # res = list()
        # for idx in range(len(cnt)):
        #     if times is None:
        #         times = cnt[idx][-1]
        #         res.append(cnt[idx][0])
        #     elif times != cnt[idx][-1]:
        #         break
        #     else:
        #         res.append(cnt[idx][0])
        # return res
