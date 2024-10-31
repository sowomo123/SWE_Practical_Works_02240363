#exercise 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #created a node to represent individual elements in linked list

class LinkedList:
    def __init__(self):
        self.head = None #created the linkedlist class with a constructor
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node#implementing the append method
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def find_middle(self):
        if not self.head:
            return None #implemening thr find middle method
        
        if not self.head.next:
            return self.head.data
        slow = self.head
        fast = self.head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#implementing main method
def main():
    ll_odd = LinkedList()
    for num in [1, 2, 3, 4, 5]:
        ll_odd.append(num)
    
    print("Odd-length list:")
    ll_odd.display()
    print("Middle element:", ll_odd.find_middle())
    
    print("\n")
    
    
    ll_even = LinkedList()
    for num in [1, 2, 3, 4, 5, 6]:
        ll_even.append(num)
    
    print("Even-length list:")
    ll_even.display()
    print("Middle element:", ll_even.find_middle())


main()

#exercise 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def detect_cycle(self):
        """
        Detect if the linked list contains a cycle
        
        Returns:
        - True if a cycle exists
        - False if no cycle is found
        """
        # If list is empty or has only one node
        if not self.head or not self.head.next:
            return False
        
        # Initialize slow and fast pointers
        slow = self.head
        fast = self.head
        
        # Move pointers until they meet or fast reaches the end
        while fast and fast.next:
            # Move slow pointer one step
            slow = slow.next
            # Move fast pointer two steps
            fast = fast.next.next
            
            # If slow and fast meet, there's a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end, no cycle
        return False
    
    def create_cycle(self, position):
        """
        Create a cycle in the linked list for testing
        
        Args:
        position: The node at which the last node connects back to 
                  (0-indexed from the head)
        """
        if not self.head:
            return
        
    
        cycle_node = self.head
        for _ in range(position):
            cycle_node = cycle_node.next
        
        current = self.head
        while current.next:
            current = current.next
        
        
        current.next = cycle_node
    
    def display(self, max_nodes=10):
        """Display the linked list (with a limit to prevent infinite loop)"""
        current = self.head
        count = 0
        visited = set()
        
        while current and count < max_nodes:
            if current in visited:
                print(f"{current.data} (cycle)", end=" -> ")
                break
            
            print(current.data, end=" -> ")
            visited.add(current)
            current = current.next
            count += 1
        
        print("None")

# Demonstration
def main():
    # Test case 1: No cycle
    print("Test Case 1: No Cycle")
    ll_no_cycle = LinkedList()
    for num in [1, 2, 3, 4, 5]:
        ll_no_cycle.append(num)
    
    ll_no_cycle.display()
    print("Has cycle:", ll_no_cycle.detect_cycle())
    
    print("\n")
    
    print("Test Case 2: Cycle at position 2")
    ll_with_cycle = LinkedList()
    for num in [1, 2, 3, 4, 5]:
        ll_with_cycle.append(num)
    
    ll_with_cycle.create_cycle(2)
    
    ll_with_cycle.display()
    print("Has cycle:", ll_with_cycle.detect_cycle())

#excersise 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def remove_duplicates_hash(self):
        """
        Remove duplicates using a hash set
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # If list is empty or has only one node
        if not self.head or not self.head.next:
            return
        
        # Set to keep track of unique values
        unique_values = set()
        
        # First node is always unique
        current = self.head
        unique_values.add(current.data)
        
        # Iterate through the list
        while current.next:
            # Check if next node's data is a duplicate
            if current.next.data in unique_values:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Add new unique value
                unique_values.add(current.next.data)
                current = current.next
    
    def remove_duplicates_in_place(self):
        """
        Remove duplicates without using extra space
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        # If list is empty or has only one node
        if not self.head:
            return
        
        # Outer loop to select current node
        current = self.head
        while current:
            # Inner loop to compare with subsequent nodes
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    # Remove duplicate
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            
            # Move to next unique node
            current = current.next
    
    def display(self):
        """Display the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Demonstration
def main():
    # Scenario 1: Remove duplicates using hash set
    print("Scenario 1: Remove Duplicates (Hash Method)")
    ll_hash = LinkedList()
    for num in [1, 2, 3, 2, 4, 1, 5, 3]:
        ll_hash.append(num)
    
    print("Original List:")
    ll_hash.display()
    
    ll_hash.remove_duplicates_hash()
    print("After removing duplicates:")
    ll_hash.display()
    
    print("\n")
    
    # Scenario 2: Remove duplicates in-place
    print("Scenario 2: Remove Duplicates (In-Place Method)")
    ll_in_place = LinkedList()
    for num in [1, 2, 3, 2, 4, 1, 5, 3]:
        ll_in_place.append(num)
    
    print("Original List:")
    ll_in_place.display()
    
    ll_in_place.remove_duplicates_in_place()
    print("After removing duplicates:")
    ll_in_place.display()

main()

#excersise 4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add a new node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def merge_sorted_lists(self, other_list):
        """
        Merge two sorted linked lists into a new sorted list
        
        Args:
        other_list (LinkedList): Another sorted linked list to merge
        
        Returns:
        LinkedList: A new merged sorted linked list
        """
        # Create a new list to store merged result
        merged_list = LinkedList()
        
        # Pointers for current nodes in both lists
        current1 = self.head
        current2 = other_list.head
        
        # Dummy node to simplify merging
        dummy = Node(0)
        current_merged = dummy
        
        # Compare and merge until one list is exhausted
        while current1 and current2:
            if current1.data <= current2.data:
                current_merged.next = Node(current1.data)
                current1 = current1.next
            else:
                current_merged.next = Node(current2.data)
                current2 = current2.next
            current_merged = current_merged.next
        
        # Add remaining nodes from first list, if any
        while current1:
            current_merged.next = Node(current1.data)
            current1 = current1.next
            current_merged = current_merged.next
        
        # Add remaining nodes from second list, if any
        while current2:
            current_merged.next = Node(current2.data)
            current2 = current2.next
            current_merged = current_merged.next
        
        # Set the head of the merged list
        merged_list.head = dummy.next
        return merged_list
    
    def merge_sorted_lists_in_place(self, other_list):
        """
        Merge two sorted linked lists in-place
        
        Args:
        other_list (LinkedList): Another sorted linked list to merge
        
        Returns:
        LinkedList: The merged sorted linked list
        """
        # If first list is empty, return the second list
        if not self.head:
            return other_list
        
        # If second list is empty, return the first list
        if not other_list.head:
            return self
        
        # Determine the head of the merged list
        if self.head.data <= other_list.head.data:
            merged_head = self.head
            current1 = self.head.next
            current2 = other_list.head
        else:
            merged_head = other_list.head
            current1 = self.head
            current2 = other_list.head.next
        
        # Keep track of the current node in the merged list
        current_merged = merged_head
        
        # Merge the lists
        while current1 and current2:
            if current1.data <= current2.data:
                current_merged.next = current1
                current1 = current1.next
            else:
                current_merged.next = current2
                current2 = current2.next
            current_merged = current_merged.next
        
        # Attach remaining nodes
        if current1:
            current_merged.next = current1
        if current2:
            current_merged.next = current2
        
        # Update the head of the first list
        self.head = merged_head
        return self
    
    def display(self):
        """Display the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Demonstration
def main():
    # Scenario 1: Merge with new list creation
    print("Scenario 1: Merge Sorted Lists (New List)")
    
    # First sorted list
    list1 = LinkedList()
    for num in [1, 3, 5, 7]:
        list1.append(num)
    
    # Second sorted list
    list2 = LinkedList()
    for num in [2, 4, 6, 8]:
        list2.append(num)
    
    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()
    
    # Merge lists
    merged_list = list1.merge_sorted_lists(list2)
    print("Merged List:")
    merged_list.display()
    
    print("\n")
    
    # Scenario 2: Merge in-place
    print("Scenario 2: Merge Sorted Lists (In-Place)")
    
    # First sorted list
    list3 = LinkedList()
    for num in [1, 3, 5, 7]:
        list3.append(num)
    
    # Second sorted list
    list4 = LinkedList()
    for num in [2, 4, 6, 8]:
        list4.append(num)
    
    print("List 3:")
    list3.display()
    print("List 4:")
    list4.display()
    
    # Merge lists in-place
    merged_list_in_place = list3.merge_sorted_lists_in_place(list4)
    print("Merged List (In-Place):")
    merged_list_in_place.display()


main()
