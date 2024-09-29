#implementing a Stack class using Python deque collection
from collections import deque

#The reason behind creating a seprate class instead of using deque directly is to define methods
# like peek(), is_empty() etc, which we expicitly do not have in deque

class Stack:
    def __init__(self) -> None:
        # calling our stack container
        self.container = deque()
    
    def push(self, data):
        self.container.append(data) #add element into the end to the deque
        return
    
    def pop(self):
        return self.container.pop() # remove and return the top element
    
    def peek(self):
        return self.container[-1] # Return the topmost element without removing
    
    def size(self):
        return len(self.container) #Return the length of the stack
    
    def is_empty(self):
        return len(self.container) == 0 #if length is 0 then stack is empty
    
    