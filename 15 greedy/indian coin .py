def indianCoin(coins, amount):
    
    # Sort the coins in descending order to start with the largest denomination
    coins = sorted(coins, reverse=True)
    res = []
    count = 0
    
    # Iterate over each coin in the sorted list
    for coin in coins:
        # Check if the current coin can be used
        if amount >= coin:
            # Use the current coin as many times as possible
            while amount >= coin:
                amount -= coin  # Subtract the coin value from the amount
                count += 1  # Increment the coin count
                res.append(coin)  # Add the coin to the result list
    
    print(f'Number of coins: {count}')
    print(f'Coins are: {res}')

coins = [2000, 500, 100, 50, 20, 10, 5, 2, 1]
amount = 590

indianCoin(coins, amount)
