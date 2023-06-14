class MinStack(object):

    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        self.arr = self.arr[:-1]

    def top(self):
        return self.arr[-1]

    def getMin(self):
        return min(self.arr)

st = MinStack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.pop()
print(st.getMin())
print(st.top())
