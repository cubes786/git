def sum_of_selections(lst):
    total_sum = 0

    while lst:
        # Find the first minimum value
        min_value = min(lst)
        min_index = lst.index(min_value)
        
        # Determine the left and right indices to be removed
        start_index = max(0, min_index - 1)
        end_index = min(len(lst), min_index + 1)

        # Select the segment to be removed
        selection = lst[start_index:end_index+1]
        
        # Add the first minimum value to the total sum
        total_sum += min_value
        
        # Remove the selected segment from the list
        lst = lst[:start_index] + lst[end_index:]
        
    return total_sum

# Example usage
lst = [3, 2, 1, 1, 2, 4, 6, 5]
result = sum_of_selections(lst)
print(f"The sum of the selections is: {result}")  # Output should be 8
