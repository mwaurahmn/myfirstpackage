def top_n(items, n):
    """
    Return the top n items in an array, in desc order.

    Args:
        items (array): list or array-like object
        n (int): number of items to return

    Return:
        array: top n items, in desc order

    Example:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    sorted_items = sorted(items, reverse=True) # Sort the items in descending order
    return sorted_items[:n] # Return top n elements