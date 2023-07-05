# Linked List is a Linear Data Structure
# Three types
    # simple Node --->  Data1  + pointer to Next Node(address of the Data2)  , Data2 +  next Node Address (None) 
    # Doubly Linked List Two Pointers --> address + data + address last one is None
    # circular Linked List --> last Node Address or pointer refferes to first Node Addres or Pointer 
        # add1 + data1 + add2 + add2 + data2 + add1 

class Node(object):

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data 

    def set_data(self, d):
        self.data = d 


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size 

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size+=1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())

                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True #data removed 

            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False #data not found 


obj = LinkedList()
obj.add(5)
obj.add(8)
obj.add(10)
print(f"Size of Node is {obj.get_size()}")
obj.add(15)
print(f"Size of Node is {obj.get_size()}")
obj.remove(8)
print(f"Size of Node is {obj.get_size()}")
obj.remove(8)
print(f"Size of Node is {obj.get_size()}")
