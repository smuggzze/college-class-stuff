class IntStack:  # class for creating a stack using an array of integers
    def __init__(self, max_stack_size):
        self.max_stack_size = max_stack_size
        self.int_array = max_stack_size * [None]
        self.next_free_location = 0
        self.input = input("give an integer for the stack pls: ")


    def stack(self):
        int(self.input)

    def push(self):
        # push the item, return True if works, False if didn't

        # check if room, if not False

        # insert item at items[next_free_location]

        # update next_free_location

def main():
    stack = IntStack()
    run = True

    while run:
        stack.stack()

