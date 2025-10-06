def recursive_count(some_list, t):
    if not some_list:
        return 0
    if some_list[0] == t:
        return 1 + recursive_count(some_list[1:], t)
    else:
        return recursive_count(some_list[1:], t)
    
print(recursive_count([1, 2, 3, 2, 2], 2)) 
print(recursive_count([], 5))               
print(recursive_count(['a', 'b', 'a'], 'a')) 