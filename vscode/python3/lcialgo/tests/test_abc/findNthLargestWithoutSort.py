import heapq

def find_nth_largest(nums, n):
    # Handle edge case: If the list has fewer than n elements
    if len(nums) < n:
        return None
    
    # Step 1: Use a min-heap to keep track of the n largest elements
    min_heap = []
    
    # Step 2: Iterate through the list
    for num in nums:
        # Step 3: Push the current number into the heap
        if len(min_heap) < n:
            heapq.heappush(min_heap, num)
        else:
            # If the heap has n elements, only push the new number if it is larger
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
    
    # Step 4: Return the smallest element in the heap, which is the nth largest number
    return min_heap[0]

# Example usage:
nums = [12, 35, 1, 10, 34, 1]
n = 2
print(f"{n}-th largest number: {find_nth_largest(nums, n)}")

def find_nth_smallest(nums, n):
    # Handle edge case: If the list has fewer than n elements
    if len(nums) < n:
        return None
    
    # Step 1: Use a max-heap (simulated by negating numbers) to keep track of the n smallest elements
    max_heap = []
    
    # Step 2: Iterate through the list
    for num in nums:
        # Step 3: Push the negated current number into the heap
        if len(max_heap) < n:
            heapq.heappush(max_heap, -num)  # Negate the number to simulate max-heap
        else:
            # If the heap has n elements, only push the new number if it is smaller
            if num < -max_heap[0]:  # Compare with negated largest element
                heapq.heapreplace(max_heap, -num)
    
    # Step 4: Return the root of the heap (negated again), which is the nth smallest number
    return -max_heap[0]

# Example usage:
nums = [12, 35, 2, 10, 34, 1]
n = 2
print(f"{n}-th smallest number: {find_nth_smallest(nums, n)}")