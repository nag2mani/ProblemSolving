from itertools import combinations, permutations

arr = [1, 2, 3]

# print(list(combinations(arr, 0)))
# print(list(combinations(arr, 1)))
# print(list(combinations(arr, 2)))
# print(list(combinations(arr, 3)))
# print(list(combinations(arr, 4)))
# print(list(permutations(arr, 2)))
# print(list(permutations(arr, 3)))

# def subarrays(arr):
#     subarrs = []
#     for i in range(len(arr) + 1):
#         for combo in combinations(arr, i):
#             subarrs.append(list(combo))
#     return subarrs
# print(subarrays(arr))

def subarrays(arr):
    subarrs = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n+1):
            subarrs.append(arr[i:j])
    return subarrs
print(subarrays(arr))

# def subarrays_recursive(arr):
#     if len(arr) == 0:
#         return [[]]
#     else:
#         subarrs = subarrays_recursive(arr[:-1])
#         return subarrs + [subarr + [arr[-1]] for subarr in subarrs]
# print(subarrays_recursive(arr))



