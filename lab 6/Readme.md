# exercise6
exercises for Students
Implement a method to find the middle element of the linked list.
Create a method to detect if the linked list has a cycle.
Implement a method to remove duplicates from an unsorted linked list.
Add a method to merge two sorted linked lists into a single sorted linked list.

# What you have implemented?
i have implemented a singly linked list:
Each node holds two parts: the data and a pointer (reference) to the next node.
The last node's next pointer is None, marking the end of the list.
Insert allows adding new nodes at specified positions.
Delete removes nodes by value.
Search finds the position of nodes by their values.
Reverse changes the order of the nodes in the list.




# exercise7
Exercises for Students
Implement a method to find the maximum value in the BST.
Add a method to count the total number of nodes in the BST.
Implement a level-order traversal (breadth-first search) for the BST.
Create a method to find the height of the BST.
Implement a method to check if the tree is a valid BST

what did you implement?
What you have implemented?
i have implemented a binary search Tree (BST) with operations like insertion, deletion, search, and traversal.
# Insertion:
Inserts elements while maintaining the BST property.
Uses a helper function _insert that places the new node in the correct position recursively.


# Deletion:
Handles three cases:
Node with no children: simply remove it.
Node with one child: replace the node with its child.

# Search:
Recursively searches for the specified value.
Returns True if the node is found; False otherwise.

# Traversal Methods:
In-order (Left, Root, Right): Visits nodes in ascending order.
Pre-order (Root, Left, Right): Useful for creating a copy of the tree.