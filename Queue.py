# Queue is a Linear Data Structure
# It fallows FIFO (First In First Out)
# New elemet is addes at end and remove at that First only 
# Insert an element is called "enqueue"
# Deleting elemet is called "dequeue"
# Time Complexity O(1)

class Queue(object):

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.insert(0, data)
        return f"{data} added to queue"

    def dequeue(self):
        return f"{self.queue.pop()} deleted in queue"

    def queuesize(self):
        return(f"{len(self.queue)} size of queue")

if __name__ == "__main__":
    q = Queue()
    print(q.isEmpty())
    print(q.queue)
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.queue)
    print(q.dequeue())
    print(q.dequeue())
    print(q.queue)
    print(q.queuesize())
    print(q.isEmpty())