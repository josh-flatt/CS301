def search_sorted_list(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1
    return binary_search(sorted_list, item, low, high)


def binary_search(sorted_list, item, low, high):
    mid = (low + high) // 2
    if sorted_list[mid] == item:
        return True
    if low >= high:
        return False
    if sorted_list[mid] > item:
        return binary_search(sorted_list, item, low, mid)
    if sorted_list[mid] < item:
        return binary_search(sorted_list, item, mid + 1, high)
