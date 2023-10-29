"""Import pyplot from matplotlib to create the plots that we need to show"""
import matplotlib.pyplot as plt
"""Import random to Generate the 5000 and 10000 random numbers"""
import random
"""Import timeit to measure the amount of time it takes to sort the numbers"""
import timeit
"""Import sys set the maximum recursion limit to 10000,
    quick sort was causing problems as the number grows"""
import sys

def main():
    sys.setrecursionlimit(10000)

"""This function would be used to generate the numbers"""
def generate_random_numbers(n):
    """Generate n random numbers."""
    return [random.randint(1, 10000) for _ in range(n)]

"""This function would be used to sort the numbers in insertion sort"""
# Source https://www.geeksforgeeks.org/insertion-sort/
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

"""This function would be used to sort the numbers in quick sort"""
# Source https://www.geeksforgeeks.org/quick-sort/
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

"""This function would be used to sort the numbers in merge sort"""
# Source https://www.geeksforgeeks.org/merge-sort/
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


"""This is the helper function for the merge sort algorithm"""
def merge(left, right):
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

"""This function inverts an array"""
def invert_array(array):
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
    insertion_sort_timeElapsed = []
    quick_sort_timeElapsed = []
    merge_sort_timeElapsed = []
    
    # Generate the random number list and the ascending number list
    for length in lengths:
        array = generate_random_numbers(length)
        random_number_list.append(array)
        ascending_number_list.append(merge_sort(array))
    
    # Generate the descending number list
    for array in ascending_number_list:
        descending_number_list.append(invert_array(array))
        
    # Measure the time it take to finish sorting for each sorting algorithm for random lists
    for array in random_number_list:
        start_time = timeit.default_timer()
        insertion_sort(array)
        end_time = timeit.default_timer()
        insertion_sort_timeElapsed.append((end_time - start_time) * 1000 )
        start_time = timeit.default_timer()
        quick_sort(array)
        end_time = timeit.default_timer()
        quick_sort_timeElapsed.append((end_time - start_time) * 1000)
        start_time = timeit.default_timer()
        merge_sort(array)
        end_time = timeit.default_timer()
        merge_sort_timeElapsed.append((end_time - start_time) * 100000)
    
    # Plot the random list time elapsed
    plt.figure(1)
    plt.title('Comparison of Sorting Algorithms Time Elapse with Different Length of Random Lists')
    plt.plot(lengths, insertion_sort_timeElapsed, label='Insertion Sort (ms)', marker='o', markersize=10)
    plt.plot(lengths, quick_sort_timeElapsed, label='Quick Sort (ms)', marker='o', markersize=10)
    plt.plot(lengths, merge_sort_timeElapsed, label='Merge Sort (100ms)', marker='o', markersize=10)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.legend()
    
    # Clean the lists
    insertion_sort_timeElapsed = []
    quick_sort_timeElapsed = []
    merge_sort_timeElapsed = []
    
    # Measure the time it take to finish sorting for each sorting algorithm for ascending lists
    for array in ascending_number_list:
        start_time = timeit.default_timer()
        insertion_sort(array)
        end_time = timeit.default_timer()
        insertion_sort_timeElapsed.append((end_time - start_time) * 1000000)
        start_time = timeit.default_timer()
        quick_sort(array)
        end_time = timeit.default_timer()
        quick_sort_timeElapsed.append((end_time - start_time) * 1000)
        start_time = timeit.default_timer()
        merge_sort(array)
        end_time = timeit.default_timer()
        merge_sort_timeElapsed.append((end_time - start_time) * 100000)

    # Plot the ascending list time elapsed
    plt.figure(2)
    plt.title('Comparison of Sorting Algorithms Time Elapse with Different Length of Ascending Lists')
    plt.plot(lengths, insertion_sort_timeElapsed, label='Insertion Sort (µs)', marker='o', markersize=10)
    plt.plot(lengths, quick_sort_timeElapsed, label='Quick Sort (ms)', marker='o', markersize=10)
    plt.plot(lengths, merge_sort_timeElapsed, label='Merge Sort (100ms)', marker='o', markersize=10)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.legend()
    
    # Clean the lists
    insertion_sort_timeElapsed = []
    quick_sort_timeElapsed = []
    merge_sort_timeElapsed = []
    
    # Measure the time it take to finish sorting for each sorting algorithm for descending lists
    for array in descending_number_list:
        start_time = timeit.default_timer()
        insertion_sort(array)
        end_time = timeit.default_timer()
        insertion_sort_timeElapsed.append((end_time - start_time) * 1000)
        start_time = timeit.default_timer()
        quick_sort(array)
        end_time = timeit.default_timer()
        quick_sort_timeElapsed.append((end_time - start_time) * 1000)
        start_time = timeit.default_timer()
        merge_sort(array)
        end_time = timeit.default_timer()
        merge_sort_timeElapsed.append((end_time - start_time) * 100000)
        
    # Plot the descending list time elapsed
    plt.figure(3)
    plt.title('Comparison of Sorting Algorithms Time Elapse with Different Length of Descending Lists')
    plt.plot(lengths, insertion_sort_timeElapsed, label='Insertion Sort (ms)', marker='o', markersize=10)
    plt.plot(lengths, quick_sort_timeElapsed, label='Quick Sort (ms)', marker='o', markersize=10)
    plt.plot(lengths, merge_sort_timeElapsed, label='Merge Sort (100ms)', marker='o', markersize=10)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.legend()

    # Show the plots
    plt.show()