class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for path in paths:
            splited = path.split(" ")
            head = splited[0] + "/"
            files = list()
            contents = list()
            for file in splited[1:]:
                splited_content = file.split("(")
                files.append(head + splited_content[0])
                contents.append(splited_content[1][:-1])
            for idx in range(len(files)):
                d[contents[idx]].append(files[idx])
        res = list()
        for key, val in d.items():
            if len(val) > 1:
                res.append(val)
        return res
