'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    #ZeroDivisionError: division by zero
    """
    n = len(arr)
    prod = 1
    for i in range(n):
        prod *= arr[i]
    for i in range(n):
        arr[i] = prod/arr[i]

    return arr
"""

    # Initialize a variable to store the  
    # total product of the array elements 
    n = len(arr)
    temp = 1
    """
    for example arr =[3,5,4,2]
    """
    # Allocate memory for the product array  
    prod = [1 for i in range(n)] 
  
    # Initialize the product array as 1  
  
    # In this loop, temp variable contains product of 
    # elements on left side excluding arr[i]  
    for i in range(n): 
        prod[i] = temp 
        temp *= arr[i] 
    """
    here, prod = [1,3,3*5,3*5*4]
    """
    # Initialize temp to 1 for product on right side  
    temp = 1
  
    # In this loop, temp variable contains product of 
    # elements on right side excluding arr[i]  
    for i in range(n - 1, -1, -1): 
        prod[i] *= temp 
        temp *= arr[i] 
    """
    here, temp = [2*4*5,2*4,2,1]
    """
    """
    last, let prod = prod * temp, prod = [2*4*5,3*2*4,3*5*2,3*5*4]
    """
    return prod
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
