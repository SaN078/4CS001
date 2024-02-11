def ordered_find(c, sorted_list):
    start = 0
    end = len(sorted_list) - 1

    while True:
        mid = (start + end) // 2

        if c == sorted_list[mid]:
            return mid
        elif c < sorted_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

        if start > end:
            return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = ordered_find(target_element, sorted_list)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")

