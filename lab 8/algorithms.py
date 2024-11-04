# step 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)

#step 2 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)

# step 3
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)

# step 4
import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)

# exercise 1 
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1  

arr = [10, 7, 8, 9, 1, 5, 6,2, 0, 12, 18, 19, 56, 0.2, 0.8, 67]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# exercise 2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                swapped = True
        if not swapped:
            break
arr = [10, 7, 8, 9, 1, 5, 6,2, 0, 12, 18, 19, 56, 0.2, 0.8, 67]
bubble_sort(arr)
print("Sorted array:", arr)

# exercise 3
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]

    i = 0 
    j = 0 
    k = left 
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1

    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1

    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1

def hybrid_merge_sort(arr, left, right, threshold):
    if left < right:
        if right - left <= threshold:
            insertion_sort(arr, left, right)
        else:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, threshold) 
            hybrid_merge_sort(arr, mid + 1, right, threshold)  
            merge(arr, left, mid, right)  

arr = [10, 7, 8, 9, 1, 5, 6,2, 0, 12, 18, 19, 56, 0.2, 0.8, 67]
threshold = 5 
hybrid_merge_sort(arr, 0, len(arr) - 1, threshold)
print("Sorted array is:", arr)


# exercise 4 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Insertion Sort with visualization
def insertion_sort(arr, ax):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            # Update the plot
            ax.clear()
            ax.bar(range(len(arr)), arr, color='green')
            ax.set_title('Insertion Sort')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            plt.pause(0.1)
        arr[j + 1] = key
        # Update the plot
        ax.clear()
        ax.bar(range(len(arr)), arr, color='yellow')
        ax.set_title('Insertion Sort')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(0.1)

# Merge function for Hybrid Merge Sort with visualization
def merge(arr, left, mid, right, ax):
    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]
    
    i = 0
    j = 0
    k = left

    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1
        # Update the plot
        ax.clear()
        ax.bar(range(len(arr)), arr, color='black')
        ax.set_title('Merging')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(0.1)

    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1
        # Update the plot
        ax.clear()
        ax.bar(range(len(arr)), arr, color='green')
        ax.set_title('Merging')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(0.1)

    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1
        # Update the plot
        ax.clear()
        ax.bar(range(len(arr)), arr, color='green')
        ax.set_title('Merging')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.pause(0.1)


def hybrid_merge_sort(arr, left, right, ax, threshold=5):
    if left < right:
        if right - left <= threshold:
            insertion_sort(arr[left:right + 1], ax)
        else:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, ax, threshold)
            hybrid_merge_sort(arr, mid + 1, right, ax, threshold)
            merge(arr, left, mid, right, ax)


def visualize_sorting():
    arr = np.random.randint(1, 100, 20)  
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title('Sorting Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.pause(1)

    hybrid_merge_sort(arr, 0, len(arr) - 1, ax)

    ax.clear()
    ax.bar(range(len(arr)), arr, color='red')
    ax.set_title('Sorted Array')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.pause(2)

    plt.show()

visualize_sorting()
