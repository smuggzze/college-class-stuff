class CircularQueue:
    def __init__(self,):
        self.max_size = 10
        self.array = self.max_size * [None]
        self.next_free_location = 0
        self.queue_front = 0

    def enqueue(self, item):
        self.array[self.next_free_location] = item
        self.next_free_location += 1
        self.next_free_location = self.next_free_location % self.max_size

    def dequeue(self):
        print(self.array.pop(self.queue_front))
        self.queue_front += 1
        self.queue_front = self.queue_front % self.max_size


queue = CircularQueue()
queue.enqueue(1)
print(queue.array)
