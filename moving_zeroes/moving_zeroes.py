'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    result = []
    count = 0
    for i in arr:
        if i == 0:
            result.append(i)
        else:
            result.insert(0, i)
            count += 1
    return result



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")