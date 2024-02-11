def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

       # Swap the found minimum element with the first element of the unsorted part
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


# Example:
abc = ['b', 'd', 'e', 'a', 'c']

# Print the original unsorted list
print("Original List:", abc)

# Perform Selection Sort
selection_sort(abc)

# Print the sorted list
print("Sorted List:", abc)

#-----------------------------------------------------------------------------------------------------------------------#

def merge(arr, left, right):
    i = j = k = 0

    # Compare elements from left and right halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Check if any elements are left in either left or right half
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index

        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)





# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)

merge_sort(arr)
print("Sorted Array:", arr)

#---------------------------------------------------------------------#



# def a():
#     a()

# a()


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(500))