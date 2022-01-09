class IntStack:  # class for creating a stack using an array of integers
    def __init__(self, max_stack_size):
        self.max_stack_size = max_stack_size
        self.int_array = max_stack_size * [None]
        self.next_free_location = 0
        self.stack_top = 0

    def push(self, item):
        if self.next_free_location >= self.max_stack_size:
            return False  # return False if it didn't work

        else:
            self.int_array[self.next_free_location] = item  # add the chosen item to the next free location in array
            self.next_free_location += 1  # increment next free location
            self.stack_top = self.next_free_location - 1  # top of the stack is always going to be one less than the
            # next_free_location
            if self.next_free_location >= self.max_stack_size:  # next_free_location can't exceed max_stack_size
                self.next_free_location = self.max_stack_size
            print(self.int_array)
            return True  # return True if it worked

    def pop(self):
        if self.int_array[self.stack_top] is None:
            return False  # return False, because you can't pop nothing
        else:
            popped_int = self.int_array[self.stack_top]
            self.int_array[self.stack_top] = None  # return the state of the popped_int to None
            self.stack_top -= 1  # top of the stack is going to decrease
            self.next_free_location -= 1  # next free location is also going to decrease
            print(self.int_array)  # give a visualisation of the stack for the user to interface with
            return popped_int  # return the originally popped integer

    def peek(self):  # shows the top item of the stack without removing it.
        return self.int_array[self.stack_top]


stack = IntStack(10)
