"""
List manipulation functions for common operations.
"""

from typing import List, Any, Union


def find_duplicates(lst: List[Any]) -> List[Any]:
    """
    Find duplicate elements in a list.
    
    Args:
        lst (List[Any]): The list to check for duplicates
        
    Returns:
        List[Any]: List of duplicate elements
        
    Example:
        >>> find_duplicates([1, 2, 3, 2, 4, 3])
        [2, 3]
    """
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    Remove duplicates from list while preserving order.
    
    Args:
        lst (List[Any]): The list to process
        
    Returns:
        List[Any]: List with duplicates removed
        
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4, 3])
        [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flatten a nested list into a single list.
    
    Args:
        nested_list (List[List[Any]]): The nested list to flatten
        
    Returns:
        List[Any]: Flattened list
        
    Example:
        >>> flatten_list([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
    """
    result = []
    for sublist in nested_list:
        result.extend(sublist)
    return result


def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        lst (List[Any]): The list to chunk
        chunk_size (int): Size of each chunk
        
    Returns:
        List[List[Any]]: List of chunks
        
    Example:
        >>> chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def merge_sorted_lists(list1: List[Union[int, float]], list2: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1 (List[Union[int, float]]): First sorted list
        list2 (List[Union[int, float]]): Second sorted list
        
    Returns:
        List[Union[int, float]]: Merged sorted list
        
    Example:
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result


def find_max_subarray_sum(lst: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the maximum sum of a contiguous subarray (Kadane's algorithm).
    
    Args:
        lst (List[Union[int, float]]): List of numbers
        
    Returns:
        Union[int, float]: Maximum subarray sum
        
    Example:
        >>> find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
    """
    if not lst:
        return 0
    
    max_sum = current_sum = lst[0]
    
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def rotate_list(lst: List[Any], k: int) -> List[Any]:
    """
    Rotate list to the right by k positions.
    
    Args:
        lst (List[Any]): The list to rotate
        k (int): Number of positions to rotate
        
    Returns:
        List[Any]: Rotated list
        
    Example:
        >>> rotate_list([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
    """
    if not lst or k == 0:
        return lst.copy()
    
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]


def list_intersection(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Find intersection of two lists (common elements).
    
    Args:
        list1 (List[Any]): First list
        list2 (List[Any]): Second list
        
    Returns:
        List[Any]: List of common elements
        
    Example:
        >>> list_intersection([1, 2, 3, 4], [3, 4, 5, 6])
        [3, 4]
    """
    return list(set(list1) & set(list2))
