class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        in_place_pointer = 1
        pre = chars[0]
        pos = 0
        while True:
            if pos == len(chars):
                break
            idx = pos
            flag_end = False
            flag_another = False
            while True:
                if idx == len(chars):
                    flag_end = True
                    break
                if chars[idx] != pre:
                    flag_another = True
                    break
                idx += 1
            if flag_end:
                if idx - pos != 1:
                    for c in list(str(idx - pos)):
                        chars[in_place_pointer] = c
                        in_place_pointer += 1
                break
            elif flag_another:
                if idx - pos != 1:
                    for c in list(str(idx - pos)):
                        chars[in_place_pointer] = c
                        in_place_pointer += 1
                pre = chars[idx]
                pos = idx
                chars[in_place_pointer] = chars[pos]
                in_place_pointer += 1
                continue
        for times in range(len(chars) - in_place_pointer):
            chars.pop()
        return in_place_pointer