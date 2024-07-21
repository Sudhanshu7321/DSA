def knapsack(weight, value, w):
    # Create a list of tuples containing (index, value, weight, value-to-weight ratio)
    ratio = []
    for i in range(len(weight)):
        rat = [i, value[i], weight[i], value[i] / weight[i]]
        ratio.append(rat)
    
    # Sort the list by the value-to-weight ratio in descending order
    sortRatio = sorted(ratio, key=lambda x: x[3], reverse=True)
    
    capacity = w
    res = 0
    
    # Iterate over the sorted items
    for i in range(len(weight)):
        if capacity >= sortRatio[i][2]:  # If the knapsack can carry the whole item
            res += sortRatio[i][1]  # Add the entire value of the item
            capacity -= sortRatio[i][2]  # Subtract the weight of the item from the capacity
        else:
            res += sortRatio[i][3] * capacity  # Add the fractional value
            break  # The knapsack is now full
    
    print(f'Result of knapsack: {res}')

# Test the function
weight = [10, 20, 30, 5]
value = [60, 100, 120, 150]
w = 50

knapsack(weight, value, w)
