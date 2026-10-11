prices = [7,1,5,3,6,4]

smallest = prices[0]
max_profit = 0

for i in range(1, len(prices)):
    if prices[i] < smallest:
        smallest = prices[i]
    else:
        profit = prices[i]-smallest
        if profit > max_profit:
            max_profit = profit
print(max_profit)


      

