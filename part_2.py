"""Import pyplot from matplotlib to create the plots that we need to show"""
import matplotlib.pyplot as plt
"""Import random to Generate the random numbers in different size"""
import random
"""Import sys set the maximum recursion limit to 10000,
    quick sort was causing problems as the number grows"""
import sys

"""This function sets the recursion limit to 10000"""
def main():
    sys.setrecursionlimit(10000)

"""This function would be used to generate the numbers"""
def generate_random_numbers(n):
    return [random.randint(1, 10000) for _ in range(n)]

"""This is the insertion sort algorithm from part 1, I added the count of operations"""
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        count += 1
        while j >= 0 and arr[j] > key:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return count

"""This is the quick sort algorithm from part 1, I added the count of operations"""
def quick_sort(arr):
    count = 0
    if len(arr) < 2:
        return count
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    count += len(arr) - 1
    count += quick_sort(less)
    count += quick_sort(greater)
    return count

"""This is the merge sort algorithm from part 1, I added the count of operations"""
def merge_sort(arr):
    count = 0
    if len(arr) < 2:
        return count
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    count += merge_sort(left)
    count += merge_sort(right)
    tempCounter, _ = merge(left, right)
    count += tempCounter
    return count

"""This is the helper function for the merge sort algorithm from part 1, I added the count of operations"""
def merge(left, right):
    count = 0
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        count += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return count, merged


"""This function would be used to sort the numbers in merge sort from part 1"""
def merge_sort_from_part_1(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge_from_part_1(merge_sort_from_part_1(left), merge_sort_from_part_1(right))

"""This is the helper function for the merge sort algorithm from part 1"""
def merge_from_part_1(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

"""This is function inverts an array from part 1"""
def invert_array_from_part_1(array):
    inverted_array = []
    for i in range(len(array) - 1, -1, -1):
        inverted_array.append(array[i])
    return inverted_array

"""This the main method to execute my research"""
if __name__ == "__main__":
    main()
    lengths = [10, 100, 1000, 3000, 5000, 7000, 9000, 10000]
    random_number_list = []
    ascending_number_list = []
    descending_number_list = []
    insertion_sort_counts = []
    quick_sort_counts = []
    merge_sort_counts = []
    
    #Generate the random number list and the ascending number list
    for length in lengths:
        array = generate_random_numbers(length)
        random_number_list.append(array)
        ascending_number_list.append(merge_sort_from_part_1(array))
    
    #Generate the descending number list
    for array in ascending_number_list:
        descending_number_list.append(invert_array_from_part_1(array))
        
    #Count the operations for each sorting algorithm for random lists
    for array in random_number_list:
        insertion_sort_counts.append(insertion_sort(array)/1000)
        quick_sort_counts.append(quick_sort(array)/1000)
        merge_sort_counts.append(merge_sort(array))    
    
    # Plot the random list count of operations
    plt.figure(1)
    plt.title('Sorting Algorithms Number of Operations vs Different Length of Random Lists')
    plt.plot(lengths, insertion_sort_counts, label='Insertion Sort (1000)', marker='o', markersize=10)
    plt.plot(lengths, quick_sort_counts, label='Quick Sort (1000)', marker='o', markersize=10)
    plt.plot(lengths, merge_sort_counts, label='Merge Sort ', marker='o', markersize=10)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.legend()
    
    # Clean the lists
    insertion_sort_counts = []
    quick_sort_counts = []
    merge_sort_counts = []
    
    # Count the operations for each sorting algorithm for ascending lists
    for array in ascending_number_list:
        insertion_sort_counts.append(insertion_sort(array))
        quick_sort_counts.append(quick_sort(array)/1000)
        merge_sort_counts.append(merge_sort(array))    

    # Plot the ascending list count of operations
    plt.figure(2)
    plt.title('Sorting Algorithms Number of Operations vs Different Length of Ascending Lists')
    plt.plot(lengths, insertion_sort_counts, label='Insertion Sort', marker='o', markersize=10)
    plt.plot(lengths, quick_sort_counts, label='Quick Sort (1000)', marker='o', markersize=10)
    plt.plot(lengths, merge_sort_counts, label='Merge Sort', marker='o', markersize=10)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.legend()
    
    # Clean the lists
    insertion_sort_counts = []
    quick_sort_counts = []
    merge_sort_counts = []
    
    # Count the operations for each sorting algorithm for descending lists
    for array in descending_number_list:
        insertion_sort_counts.append(insertion_sort(array)/1000)
        quick_sort_counts.append(quick_sort(array)/1000)
        merge_sort_counts.append(merge_sort(array))   

    # Plot the descending list count of operations
    plt.figure(3)
    plt.title('Sorting Algorithms Number of Operations vs Different Length of Descending Lists')
    plt.plot(lengths, insertion_sort_counts, label='Insertion Sort (1000)', marker='o', markersize=10)
    plt.plot(lengths, quick_sort_counts, label='Quick Sort (1000)', marker='o', markersize=10)
    plt.plot(lengths, merge_sort_counts, label='Merge Sort', marker='o', markersize=10)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.legend()

    # Show the plots
    plt.show()