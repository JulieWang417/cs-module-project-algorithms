'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import collections
def sliding_window_max(nums, k):
    # Your code here

    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return nums
    queue = collections.deque()
    res = []
    for num in nums:
        if len(queue) < k:
            queue.append(num)
        else:
            res.append(max(queue))
            queue.popleft()
            queue.append(num)
    res.append(max(queue))
    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
