class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(people):
            return list()
        res = list()
        people.sort(key=lambda x: x[0], reverse=True)
        highest = people[0][0]

        while len(people):
            if people[0][0] == highest:
                res.append(people.pop(0))
            else:
                break
        res.sort(key=lambda x: x[1])

        if not len(people):
            return res

        base = 0
        h_value = people[0][0]
        for idx in range(len(people)):
            if people[idx][0] != h_value:
                people[base:idx] = sorted(people[base:idx], key=lambda x: x[1])
                h_value = people[idx][0]
                base = idx
        people[base:] = sorted(people[base:], key=lambda x: x[1])

        for _ in range(len(people)):
            guy = people.pop(0)
            k_value = guy[1]
            res.insert(k_value, guy)

        return res
