class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list()
        for i in range(1, n + 1):
            special = None
            if not i % 3:
                special = 'Fizz'
            if not i % 5:
                if not special:
                    special = 'Buzz'
                else:
                    special += 'Buzz'
            if not special:
                res.append(str(i))
            else:
                res.append(special)
        return res
