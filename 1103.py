class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        base = num_people * (num_people + 1) / 2
        num_people_square = num_people * num_people
        k = 0
        tmp_candies = candies
        while True:
            needed = base if k == 0 else base + k * num_people_square
            if tmp_candies - needed >= 0:
                k += 1
                tmp_candies -= needed
            else:
                break
        result = list()
        if k > 0:
            for idx in range(num_people):
                result.append((k)*(idx+1)+num_people*k*(k-1)/2)
            candies -= k * base + k * (k - 1) / 2 * num_people * num_people
        else:
            result = [0 for _ in range(num_people)]
        idx = 0
        while candies > 0:
            needed = k * num_people + (idx + 1)
            if candies < needed:
                result[idx] += candies
                candies=0
            else:
                result[idx] += needed
                candies-=needed
            idx += 1
        result = list(map(int, result))
        return result