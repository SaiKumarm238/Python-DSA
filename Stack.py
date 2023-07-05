# Stack is a Linear Data Structure
# It fallows LIFO (Last In First Out)
# New elemet is addes at end and remove at that end only 
# Insert an element is called "PUSH"
# Deleting elemet is called "POP"
# Time Complexity O(1)

class Stack(object):
    #constructor
    def __init__(self):
        self.stack = []
        self.numoditems = 0

    #checking empty 
    def isEqual(self):
        return self.stack == []

    #pushing elemets
    def push(self, data):
        self.stack.insert(self.numoditems,data)
        self.numoditems+= 1 #increment index
        return f"{data} pushed to stack"

    #deleting elemet 
    def pop(self):
        self.numoditems-=1
        data = self.stack.pop(self.numoditems)
        return f"{data} pop to stack"

    #length of stack
    def stacksize(self):
        return len(self.stack)

if __name__ == "__main__":
    s = Stack()
    print(s.isEqual())
    print(s.stack)
    print(s.push(2))
    print(s.push(3))
    print(s.push(4))
    print(s.isEqual())
    print(s.stack)
    print(s.pop())
    print(s.pop())
    print(s.stack)
    print(s.stacksize())