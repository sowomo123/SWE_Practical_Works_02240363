#step 1
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

#step2 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list


test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

#step 3
import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")


large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

#step4
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

#step 5
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()

#excerise1

def linear_search_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i) 
    return indices if indices else -2 

test_list = [2, 1, 5, 1, 6, 9, 2, 6, 5, 3, 8]
result = linear_search_all_indices(test_list, 6)
print(f"Linear Search {result}")

#excerise 2 
def find_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left 


sorted_list = [1, 3, 5, 7, 9]
target_value = 6
insertion_point = find_insertion_point(sorted_list, target_value)
print(f"Insertion point for {target_value} is index {insertion_point}")

#excersise 3 

def linear_search_with_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1  
        if arr[i] == target:
            return i, comparisons  
    return -1, comparisons 


test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result, comparisons = linear_search_with_count(test_list, 6)
print(f"Linear Search: Index of 6 is {result}, Comparisons: {comparisons}")


#binary searchwith comoparision
def binary_search_with_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1  
        if arr[mid] == target:
            return mid, comparisons 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        comparisons += 1  
    return -1, comparisons  
sorted_list = sorted(test_list)
result, comparisons = binary_search_with_count(sorted_list, 6)
print(f"Binary Search: Index of 6 is {result}, Comparisons: {comparisons}")




#exercise 4
import math

def jump_search(arr, target):
    length = len(arr)
    step = int(math.sqrt(length))  
    prev = 0

   
    while arr[min(step, length) - 1] < target:
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1  
    for i in range(prev, min(step, length)):
        if arr[i] == target:
            return i  
    return -1  


import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search_with_count(arr, target)[0]
    linear_time = time.time() - start_time

    # Binary Search (requires sorted array)
    sorted_arr = sorted(arr)
    start_time = time.time()
    binary_result = binary_search_with_count(sorted_arr, target)[0]
    binary_time = time.time() - start_time

    # Jump Search (requires sorted array)
    start_time = time.time()
    jump_result = jump_search(sorted_arr, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Time: {jump_time:.6f} seconds")

large_list = list(range(2000))
target_value = 9999
compare_search_algorithms(large_list, target_value)



