class Queue:
    def __init__(self):
        self.elements = []

    def queue(self, item):
        self.elements.insert(0, item)

    def dequeue(self):
        return self.elements.pop()


queue = Queue()
queue.queue(7)
queue.queue(9)
queue.queue(11)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
