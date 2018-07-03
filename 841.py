class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        travel = [False for _ in range(n)]
        entered = set()
        to_enter = [0]
        while len(to_enter):
            room_idx = to_enter.pop(0)
            travel[room_idx] = True
            for key in rooms[room_idx]:
                if not travel[key]:
                    to_enter.append(key)
        if all(travel):
            return True
        return False