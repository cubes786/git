def kadaneMin(arr):
    # Step 1: Initialize
    current_sum = arr[0]
    min_sum = arr[0]
    
    # Step 2: Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Step 3: Update current_sum
        current_sum = min(arr[i], current_sum + arr[i])
        
        # Step 4: Update min_sum
        min_sum = min(min_sum, current_sum)
    
    return min_sum

def min_cost(prices):
    # Initialize variables
    min_sum = float('inf')  # Set to infinity initially
    current_sum = 0

    # Iterate through the prices array
    for price in prices:
        current_sum += price  # Add the current price to the subarray sum
        
        # Update the minimum sum if current_sum is smaller
        min_sum = min(min_sum, current_sum)
        
        # If the current sum becomes positive, reset it
        if current_sum > 0:
            current_sum = 0
    
    return min_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -3, 4]
print(f"The maximum sum of a contiguous subarray is: {kadaneMin(arr)}")
print(f"2 The maximum sum of a contiguous subarray is: {min_cost(arr)}")
