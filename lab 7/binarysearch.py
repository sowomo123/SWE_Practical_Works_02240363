#exercise 1
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left:
                self._insert(current.left, data)
            else:
                current.left = Node(data)
        else:
            if current.right:
                self._insert(current.right, data)
            else:
                current.right = Node(data)


    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    # Create a BST and insert nodes
bst = BST()
bst.insert(50)
bst.insert(28)
bst.insert(35)
bst.insert(15)
bst.insert(85)

# Find the maximum value
print("Maximum value in the BST:", bst.find_max())  

#exersise 2
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert a new node into the BST"""
        if not self.root:
            self.root = TreeNode(data)
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = TreeNode(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(data)
                    break
                current = current.right
    
    def count_nodes_recursive(self):
        def count_recursive(node):
            if not node:
                return 0
            
            return 1 + count_recursive(node.left) + count_recursive(node.right)
        
        # Start counting from the root
        return count_recursive(self.root)
    
    def count_nodes_iterative_stack(self):
        # If tree is empty
        if not self.root:
            return 0
        
        # Initialize stack and node count
        stack = [self.root]
        node_count = 0
        
        # Depth-first traversal
        while stack:
            # Pop a node
            node = stack.pop()
            
            # Increment node count
            node_count += 1
            
            # Push right child first (if exists)
            if node.right:
                stack.append(node.right)
            
            # Push left child (if exists)
            if node.left:
                stack.append(node.left)
        
        return node_count
    
    def count_nodes_iterative_queue(self):
        # If tree is empty
        if not self.root:
            return 0
        
        # Initialize queue and node count
        queue = [self.root]
        node_count = 0
        
        # Breadth-first traversal
        while queue:
            # Get the first node
            node = queue.pop(0)
            
            # Increment node count
            node_count += 1
            
            # Add left child to queue (if exists)
            if node.left:
                queue.append(node.left)
            
            # Add right child to queue (if exists)
            if node.right:
                queue.append(node.right)
        
        return node_count

# Demonstration
def main():
    # Create a Binary Search Tree
    bst = BinarySearchTree()
    nodes = [50, 30, 70, 20, 40, 60, 80]
    
    # Insert nodes
    for node in nodes:
        bst.insert(node)
    
    print("Binary Search Tree Node Counting:")
    print("Total Nodes (Recursive):", bst.count_nodes_recursive())
    print("Total Nodes (Stack-based):", bst.count_nodes_iterative_stack())
    print("Total Nodes (Queue-based):", bst.count_nodes_iterative_queue())

main()

#eccersise 3
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert a new node into the BST"""
        if not self.root:
            self.root = TreeNode(data)
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = TreeNode(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(data)
                    break
                current = current.right
    
    def level_order_traversal(self):
        """
        Perform level-order traversal
        
        Returns:
        list: Nodes in level-order
        """
        # If tree is empty
        if not self.root:
            return []
        
        # Initialize queue and result list
        queue = deque([self.root])
        result = []
        
        while queue:
            # Get the current node
            node = queue.popleft()
            
            # Add node's data to result
            result.append(node.data)
            
            # Enqueue left child
            if node.left:
                queue.append(node.left)
            
            # Enqueue right child
            if node.right:
                queue.append(node.right)
        
        return result
    
    def level_order_traversal_with_levels(self):
        """
        Perform level-order traversal with level information
        
        Returns:
        list: Nodes grouped by levels
        """
        # If tree is empty
        if not self.root:
            return []
        
        # Initialize queue and result list
        queue = deque([(self.root, 0)])
        result = []
        
        while queue:
            # Get the current node and its level
            node, level = queue.popleft()
            
            # Extend result list if needed
            if level == len(result):
                result.append([])
            
            # Add node's data to appropriate level
            result[level].append(node.data)
            
            # Enqueue left child
            if node.left:
                queue.append((node.left, level + 1))
            
            # Enqueue right child
            if node.right:
                queue.append((node.right, level + 1))
        
        return result
    
    def level_order_zigzag_traversal(self):
        """
        Perform zigzag level-order traversal
        
        Returns:
        list: Nodes in zigzag pattern
        """
        # If tree is empty
        if not self.root:
            return []
        
        # Initialize queue and result list
        queue = deque([self.root])
        result = []
        left_to_right = True
        
        while queue:
            # Get the number of nodes at current level
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                # Get the current node
                node = queue.popleft()
                
                # Add to current level
                current_level.append(node.data)
                
                # Enqueue children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse level if needed
            if not left_to_right:
                current_level.reverse()
            
            # Add level to result
            result.append(current_level)
            
            # Flip direction
            left_to_right = not left_to_right
        
        return result
    
    def print_tree_visualization(self):
        """
        Print a visual representation of the tree
        """
        def get_tree_height(node):
            if not node:
                return 0
            return 1 + max(get_tree_height(node.left), get_tree_height(node.right))
        
        def print_node(node, space, height):
            if not node:
                return
            
            space += height
            
            # Print right subtree first
            print_node(node.right, space, height)
            
            # Print current node
            print()
            for _ in range(height, space):
                print(end=" ")
            print(node.data)
            
            # Print left subtree
            print_node(node.left, space, height)
        
        # Get tree height and print
        tree_height = get_tree_height(self.root)
        print_node(self.root, 0, tree_height)

# Demonstration
def main():
    # Create a Binary Search Tree
    bst = BinarySearchTree()
    nodes = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    
    # Insert nodes
    for node in nodes:
        bst.insert(node)
    
    # Print tree visualization
    print("Tree Visualization:")
    bst.print_tree_visualization()
    
    # Demonstrate different traversal methods
    print("\nLevel-Order Traversal (Flat):")
    print(bst.level_order_traversal())
    
    print("\nLevel-Order Traversal (With Levels):")
    for level, nodes in enumerate(bst.level_order_traversal_with_levels()):
        print(f"Level {level}: {nodes}")
    
    print("\nZigzag Level-Order Traversal:")
    for level, nodes in enumerate(bst.level_order_zigzag_traversal()):
        print(f"Level {level}: {nodes}")


main()

#exercise 4
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert a new node into the BST"""
        if not self.root:
            self.root = TreeNode(data)
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = TreeNode(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(data)
                    break
                current = current.right
    
    def height_recursive(self):
        """
        Find the height of the tree using recursive approach
        
        Returns:
        int: Height of the tree (-1 for empty tree)
        """
        def height_helper(node):
            # Base case: if node is None, height is -1
            if not node:
                return -1
            
            # Recursively find height of left and right subtrees
            left_height = height_helper(node.left)
            right_height = height_helper(node.right)
            
            # Return the maximum height + 1 (for current node)
            return max(left_height, right_height) + 1
        
        # Start from the root
        return height_helper(self.root)
    
    def height_iterative_dfs(self):
        """
        Find the height of the tree using iterative DFS (stack-based)
        
        Returns:
        int: Height of the tree (-1 for empty tree)
        """
        # If tree is empty
        if not self.root:
            return -1
        
        # Initialize stack with (node, depth) tuples
        stack = [(self.root, 0)]
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            
            # Update max depth
            max_depth = max(max_depth, current_depth)
            
            # Push right child to stack
            if node.right:
                stack.append((node.right, current_depth + 1))
            
            # Push left child to stack
            if node.left:
                stack.append((node.left, current_depth + 1))
        
        return max_depth
    
    def height_iterative_bfs(self):
        """
        Find the height of the tree using iterative BFS (queue-based)
        
        Returns:
        int: Height of the tree (-1 for empty tree)
        """
        # If tree is empty
        if not self.root:
            return -1
        
        # Initialize queue with root
        queue = [(self.root, 0)]
        max_depth = 0
        
        while queue:
            node, current_depth = queue.pop(0)
            
            # Update max depth
            max_depth = max(max_depth, current_depth)
            
            # Enqueue left child
            if node.left:
                queue.append((node.left, current_depth + 1))
            
            # Enqueue right child
            if node.right:
                queue.append((node.right, current_depth + 1))
        
        return max_depth
    
    def is_balanced(self):
        """
        Check if the tree is height-balanced
        
        Returns:
        bool: True if the tree is balanced, False otherwise
        """
        def check_balance(node):
            """
            Helper function to check balance
            Returns:
            tuple: (is_balanced, height)
            """
            # Base case: empty node is balanced
            if not node:
                return True, -1
            
            # Check left subtree
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            
            # Check right subtree
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            
            # Check if current node is balanced
            is_balanced = abs(left_height - right_height) <= 1
            
            # Return balance status and height
            return is_balanced, max(left_height, right_height) + 1
        
        # Check overall tree balance
        return check_balance(self.root)[0]

# Demonstration
def main():
    # Create multiple Binary Search Trees
    test_cases = [
        # Completely unbalanced (right-skewed)
        ([10, 20, 30, 40, 50], "Right-Skewed Tree"),
        
        # Completely unbalanced (left-skewed)
        ([50, 40, 30, 20, 10], "Left-Skewed Tree"),
        
        # Balanced tree
        ([30, 20, 40, 10, 25, 35, 45], "Balanced Tree"),
        
        # Another balanced tree
        ([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85], "Complex Balanced Tree")
    ]
    
    for nodes, tree_type in test_cases:
        # Create BST
        bst = BinarySearchTree()
        
        # Insert nodes
        for node in nodes:
            bst.insert(node)
        
        # Print tree information
        print(f"\n{tree_type}:")
        print("Height (Recursive):", bst.height_recursive())
        print("Height (DFS Iterative):", bst.height_iterative_dfs())
        print("Height (BFS Iterative):", bst.height_iterative_bfs())
        print("Is Balanced:", bst.is_balanced())

# Run the demonstration
main()
#exercise5
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left:
                self._insert(current.left, data)
            else:
                current.left = Node(data)
        else:
            if current.right:
                self._insert(current.right, data)
            else:
                current.right = Node(data)

    # Method to check if the tree is a valid BST
    def is_valid_bst(self):
        return self._is_valid_bst_helper(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_helper(self, node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self._is_valid_bst_helper(node.left, min_val, node.data) and
                self._is_valid_bst_helper(node.right, node.data, max_val))


