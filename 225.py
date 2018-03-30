class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        help = list()
        while True:
            val = self.queue.pop(0)
            if not len(self.queue):
                break
            else:
                help.append(val)
        while len(help):
            self.queue.append(help.pop(0))
        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        help = list()
        while True:
            val = self.queue.pop(0)
            if not len(self.queue):
                help.append(val)
                break
            else:
                help.append(val)
        while len(help):
            self.queue.append(help.pop(0))
        return val

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.queue)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()