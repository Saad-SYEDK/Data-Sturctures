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
        return len(self.container) == 0 #if length is 0 then stack is empty.
    
#Questions:
    
#Q1. Write a function that can reverse a string usign the stack class.
def reverse_string(str):
    # Intuition: we can push each char of the string into stack.
    # Once the string is over, we pop each char and append into variable
    
    stack = Stack() # initialize stack
    for char in str:
            stack.push(char)
    
    #initialize a variable to store our answer
    ans = ""
    
    #pop each element in the stack and append into our answer
    while not stack.is_empty():
        ans += stack.pop()
    
    return ans

#Q2. Write a fuction that  checks if parenthesis in the string are balanced or not.
# Possible parenthesis are "{}',"()" or "[]".
def is_balanced(str):
    #Intuition : Whenever we find an opening parenthesis we will push it onto stack
    # when we find a closing parenthesis we pop from our stack and compare, if they do not match
    # it means the string is not balanced, after itrating the strign if the stack is not 
    # not empty then also the string is not balanced
    
    stack = Stack()
    
    for char in str:
        
        # if opening bracket - push into stack
        if char == '{' or char == '(' or char == '[':
            stack.push(char)
        
        # if closing bracket - pop and compare
        if char == '}':
            if stack.pop() != '{':
                return False
        elif char == ')':
            if stack.pop() != '(':
                return False
        elif char ==']':
            if stack.pop() != '[':
                return False
    if stack.is_empty():
        return True
    else:
        return False

# Checking
print(is_balanced("[a+b]*(x+2y)@@@*{gg+kk}"))
    
    