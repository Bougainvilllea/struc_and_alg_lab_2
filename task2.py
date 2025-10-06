def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    

print(tribonacci(0))  
print(tribonacci(1))  
print(tribonacci(2))  
print(tribonacci(3)) 
print(tribonacci(4)) 
print(tribonacci(5)) 