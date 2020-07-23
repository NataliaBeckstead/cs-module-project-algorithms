'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque

def sliding_window_max(nums, k):
    # result = [0] * (len(nums) - k + 1)
    # for i in range(0, len(nums) - k + 1):
    #     max_num = nums[i]
    #     for j in range(i, i + k):
    #         if max_num < nums[j]:
    #             max_num = nums[j]
    #     result[i] = max_num
    # return result
    result = []
    q = deque()

    for i in range(len(nums)):
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
        if i - q[0] >= k:
            q.popleft()
        if i >= k - 1:
            result.append(nums[q[0]])

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
