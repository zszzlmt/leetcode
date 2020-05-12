class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        return sum([1 if guess[idx] == answer[idx] else 0 for idx in range(len(guess))])