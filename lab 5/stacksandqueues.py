#part 1
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(4)
stack.push(7)
stack.push(8)
print(stack.pop())  
print(stack.peek())  
print(stack.size())  

#part 2

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(4)
queue.enqueue(7)
queue.enqueue(8)
print(queue.dequeue())  
print(queue.front())  
print(queue.size())  

#part 3
#problem 1
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


print(is_balanced("((()))"))  
print(is_balanced("(()"))  

#problem 2
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

print(reverse_string("hi my name is sonam wangmo!"))  

#problem 3
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()


names = ["karma", "tshering", "norbu", "pema", "euden", "pema"]
print(hot_potato(names, 7))  

#exercise 1

def evaluate_postfix(expression):
    stack = []#empty stack to hold number
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        else: 
            right_operand = stack.pop()
            left_operand = stack.pop()
            
            if token == '+':
                stack.append(left_operand + right_operand)
            elif token == '-':
                stack.append(left_operand - right_operand)
            elif token == '*':
                stack.append(left_operand * right_operand)
            elif token == '/':
            
                stack.append(int(left_operand / right_operand))
    
    
    return stack.pop()

expression = "2 4 + 2 * 9 /" 
result = evaluate_postfix(expression)
print("Result:", result)  

#exercise 2 

class QueueUsingStacks:
    def __init__(self):
      
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        
      
        if not self.stack_dequeue:
            raise IndexError("dequeue from empty queue")
        
    
        return self.stack_dequeue.pop()

    def is_empty(self):
        
        return not self.stack_enqueue and not self.stack_dequeue

    def peek(self):
        
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        
        if not self.stack_dequeue:
            raise IndexError("peek from empty queue")
        
        
        return self.stack_dequeue[-1]


queue = QueueUsingStacks()
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)

print(queue.dequeue())  
print(queue.peek())     
print(queue.dequeue())  
print(queue.is_empty()) 
print(queue.dequeue())  
print(queue.is_empty()) 

#exercise 3

import queue
import time

class TaskScheduler:
    def __init__(self):
        
        self.task_queue = queue.Queue()

    def add_task(self, task, *args):
        self.task_queue.put((task, args))

    def process_tasks(self):
        while not self.task_queue.empty():
        
            task, args = self.task_queue.get()
            print(f"Processing task: {task.__name__} with arguments: {args}")
            task(*args)  
            self.task_queue.task_done()  

def print_message(message):
    print(message)

def add_numbers(a, b):
    print(f"Sum: {a + b}")

scheduler = TaskScheduler()


scheduler.add_task(print_message, "Hello, World! My name is sonam wangmo")
scheduler.add_task(add_numbers, 20, 10)

scheduler.process_tasks()

#exerxise 4

def infix_to_postfix(expression):

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    
    stack = []
    output = []


    tokens = expression.split()
    
    for token in tokens:
        if token.isalnum():  
            output.append(token)
        elif token in precedence:  
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  


    while stack:
        output.append(stack.pop())

    return ' '.join(output)

expression = "s + o  * n - a - m"
postfix_expression = infix_to_postfix(expression)
print("Postfix Expression:", postfix_expression)  