practical 4
exercise 
Modify the linear search function to return all indices where the target appears, not just the first one.
Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
Create a function that counts the number of comparisons made in each search algorithm.
Implement a jump search algorithm and compare its performance with linear and binary search.

What you have implemented?
in this lab 4 i have implemented Linear Search:

The linear_search function iterates through each element of the list.
If the target element is found, it returns the index of that element.
If the loop completes without finding the target, it returns -1.
Linear search has a time complexity of O(n), where n is the number of elements in the list.
Binary Search:

The binary_search function requires the input list to be sorted.
It initializes two pointers, left and right, to represent the current search interval.
Binary search has a time complexity of O(log n), making it much more efficient for large sorted lists. However, it requires the list to be sorted beforehand.




practical 5
exercise 
Implement a function that uses a stack to evaluate postfix expressions.
Create a function that uses two stacks to implement a queue.
Use a queue to implement a basic task scheduler that processes tasks in the order they were added.
Implement a function that uses a stack to convert infix expressions to postfix.

what you have implemented?
in this lab 5 i have implemented:
Function Definition: We define a function evaluate_postfix that takes a string expression as input.
Stack Initialization: We initialize an empty list stack to store numbers temporarily.
Tokenization: We split the input string into individual tokens using the split() method.
Enqueue Method: The enqueue method appends the item to the stack_enqueue, which is used for adding elements to the queue.
Dequeue Method: The dequeue method:
Checks if stack_dequeue is empty. If it is, it transfers all elements from stack_enqueue to stack_dequeue (this reverses their order).
If stack_dequeue is still empty after the transfer, it raises an exception indicating that the queue is empty.