# 2.2  Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the i(th) day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
def max_profit(prices: list[int]):
    output = -99999999999999999
    for i in range(0, len(prices)-1):
        for q in range(i, len(prices)):
            if prices[i] == 0:
                conpare = prices[q]
                if conpare > output:
                    output = conpare
            else:
                if prices[q] - prices[i] > output:
                    output = prices[q] - prices[i]
    return output


print(max_profit([22,23,14,34,17,41,29,49,37,15,19,44,39,3,21,14,6,17,41,10,11,16,14]))