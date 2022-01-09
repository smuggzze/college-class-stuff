class CircularQueue:
    def __init__(self, ):
        self.max_size = 10
        self.array = self.max_size * [None]
        self.next_free_location = 0
        self.queue_front = 0

    def enqueue(self, item):

        if self.array[self.next_free_location] is not None:  # if the next location is full, don't add the item
            return False  # return False if enqueue didnt work

        else:
            self.array[self.next_free_location] = item  # add the chosen item to the next free location in array
            self.next_free_location += 1  # increment next free location
            self.next_free_location = self.next_free_location % self.max_size  # next free location will always return
            # to the start. 10 % 10 = 0
            print(self.array)  # create a visual display of the array for the user to interface with
            return True  # return True if it worked

    def dequeue(self):

        if self.array[self.queue_front] is None:  # resets the start of the queue to the original start and same with
            # the next_free_location. This is to improve readability of the Queue in console
            self.next_free_location = 0
            self.queue_front = 0
            return False  # returns False if queue is empty

        else:
            dequeued_item = (self.array[self.queue_front])
            self.array[self.queue_front] = None  # keeps the array at set size
            self.queue_front += 1  # increment the front of the queue. keeping it circular
            self.queue_front = self.queue_front % self.max_size  # makes it so that the queue will always return to
            # the start, 10 % 10 = 0
            print(self.array)
            return dequeued_item  # return the dequeued item if it worked.

queue = CircularQueue()
