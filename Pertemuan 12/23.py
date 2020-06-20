tuple = {}
tuple[(5,3)] = 8
tuple[(1,2,7)] = 10
tuple[(1,2)] = 12
_sum = 0
for k in tuple:
    _sum += tuple[k]
print(len(tuple) + _sum)