def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if int_list is None:
        raise ValueError('Not an integer')  # Raises a Value error if the list is empty
    elif len(int_list) == 0:  # Returns None if list length is equal to zero
        return None
    else:
        m_list = int_list[0]
        if len(int_list) == 1:  # Returns the first value of the list if there is only one item
            return int_list[0]
        else:
            for x in int_list:  # Iterates through the list and sets the current max whenever x is greater
                if x > m_list:
                    m_list = x
        return m_list  # Returns the max value


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError('Empty list')  # Raises a Value error if the list is empty
    elif len(int_list) == 0:  # Returns None if empty list
        return []
    elif len(int_list) == 1:  # Returns the first value of the list if there is only one item
        return int_list  # Returns the value in the list
    else:
        rev_list = reverse_rec(int_list[1:])  # Sets rev_list to the sliced int_list
        rev_list.append(int_list[0])  # Adds the first value of the list to the reversed list
        return rev_list


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mid = (high + low) // 2
    if int_list is None:
        raise ValueError('Empty list')  # Raises a Value error if the list is empty
    elif len(int_list) == 1:
        if int_list[0] == target:
            return 0
        else:
            return None
    elif len(int_list) == 0:  # Returns None if empty list
        return None
    elif int_list[mid] == target:  # Returns the mid as the index
        return mid
    elif high <= low and int_list[mid] != target:  # Returns None if the high and low are equal target isn't in list
        return None
    elif int_list[mid] > target:  # Does recursive call on the low and one less than the mid point
        return bin_search(target, low, max(mid - 1, 0), int_list)
    elif int_list[mid] < target:  # Does recursive call on the midpoint plus one and high
        return bin_search(target, mid + 1, high, int_list)
