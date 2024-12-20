def max_paints(prices, money):
    # Sort the prices in ascending order
    prices.sort()
    
    # Initialize counters
    total_cost = 0
    count = 0
    
    # Iterate over the sorted prices
    for price in prices:
        if total_cost + price <= money:
            total_cost += price
            count += 1
        else:
            break
    
    return count

# Example usage
prices = [2, 3, 5, 1]
money = 7
result = max_paints(prices, money)
print(result)  # Output: 3
