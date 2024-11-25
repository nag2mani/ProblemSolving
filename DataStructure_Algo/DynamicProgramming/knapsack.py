#Using recursion.
def knapSack(bag_weight, weight_list, value_list, n): 
    """
    W is weight of bag.
    weight_list is list of weight.
    value_list is list of each weight.
    n is length of list.
    """
    # Base Case 
    if n == 0 or bag_weight == 0: 
        return 0
    
    #if nth term is greater then capacity of bag then we can't take it.
    if (weight_list[n-1] > bag_weight): 
        return knapSack(bag_weight, weight_list, value_list, n-1) 

    #maximum of two cases Take or not Take.
    else: 
        return max(value_list[n-1] + knapSack(bag_weight - weight_list[n-1], weight_list, value_list, n-1), knapSack(bag_weight, weight_list, value_list, n-1))

# print(knapSack(50,[10, 20, 30], [60, 100, 120], 3))






#Using Dp (Bottom up approach)
def knapSack_dp(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


val = [60, 100, 120, 500] 
wt = [10, 20, 30, 30] 
W = 50
n = len(val) 
print(knapSack_dp(W, wt, val, n))


