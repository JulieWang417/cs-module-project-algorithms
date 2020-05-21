'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

x=0
x ^= 5
print("x is:",x)

def single_number(arr):
    # Your code here

    single = arr[0]
    # Do XOR of all elements and return
    for i in range(1,len(arr)):
        single ^= arr[i]  # exclusive OR， XOR
        # single = single ^ arr[i], if single is same as arr[i], return 0, otherwise return 1
        # 0 ^ b = b
        # print(single)
    return single

"""
def singleNumber(nums): 
  
    # applying the formula : Required no = 2*(sum_of_array_without_duplicates) - (sum_of_array)
    return 2 * sum(set(nums)) - sum(nums) 
  
"""

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")