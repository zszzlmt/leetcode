"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):

    def __traval__(self, dic, id):
        res = dic[id].importance
        for child_id in dic[id].subordinates:
            res += self.__traval__(dic, child_id)
        return res

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {item.id: item for item in employees}
        return self.__traval__(dic, id)
