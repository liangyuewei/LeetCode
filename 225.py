import queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q2 = queue.Queue()
        q2.put(x)
        while not self.q1.empty():
            q2.put(self.q1.get())
        self.q1 = q2

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.get()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        topElement = self.pop()
        self.push(topElement)
        return topElement

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()