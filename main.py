import random
import timeit
import tracemalloc

# Quick Sort Algorithm
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        divider = arr[len(arr) // 2] 
        smaller_than_divider = [element for element in arr if element < divider]
        equal_to_divider = [element for element in arr if element == divider]
        greater_than_divider = [element for element in arr if element > divider]
        return quickSort(smaller_than_divider) + equal_to_divider + quickSort(greater_than_divider)

# Merge Sort Algorithm
def mergeSort(array):
    if len(array) <= 1:
        return array

    middle_index = len(array) // 2
    left_half = mergeSort(array[:middle_index])
    right_half = mergeSort(array[middle_index:])
    
    # Merging the two halves
    merged_array = []
    left_index = right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_array.append(left_half[left_index])
            left_index += 1
        else:
            merged_array.append(right_half[right_index])
            right_index += 1
    
    merged_array.extend(left_half[left_index:])
    merged_array.extend(right_half[right_index:])
    
    return merged_array

# Function to generate datasets
def generateDatasets(n):
    sortedData = list(range(n))
    reverseSortedData = list(range(n, 0, -1))
    randomData = [random.randint(0, n) for _ in range(n)]
    return sortedData, reverseSortedData, randomData

# Function to measure execution time
def measureTime(func, data):
    start_time = timeit.default_timer()
    func(data.copy()) 
    end_time = timeit.default_timer()
    return end_time - start_time

# Function to measure memory usage
def measureMemory(func, data):
    tracemalloc.start()
    func(data.copy())
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

# Function to run and compare Quick Sort and Merge Sort on various datasets
def compareAlgorithms(n):
    sortedData, reverseSortedData, randomData = generateDatasets(n)
    
    datasets = [("SORTED DATA", sortedData), ("REVERSE SORTED DATA", reverseSortedData), ("RANDOM DATA", randomData)]
    algorithms = [("QUICK SORT", quickSort), ("MERGE SORT", mergeSort)]
    
    print(f"\n--- PERFORMANCE COMPARISON FOR N = {n} ---")
    
    for name, data in datasets:
        print(f"\nDATASET TYPE :: {name}")
        for algo_name, algo in algorithms:
            time_taken = measureTime(algo, data)
            current_mem, peak_mem = measureMemory(algo, data)
            print(f"{algo_name} | EXECUTION TIME :: {time_taken:.6f} SECONDS | MEMORY USAGES :: {peak_mem / 1024:.2f} KB")

# Run the comparison for different dataset sizes
if __name__ == "__main__":
    compareAlgorithms(1000) 
    compareAlgorithms(5000) 
    compareAlgorithms(10000)