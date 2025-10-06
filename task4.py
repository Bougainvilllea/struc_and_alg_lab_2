from functools import lru_cache
import matplotlib.pyplot as plt
import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

@lru_cache(maxsize=None)
def lucas_fast(n):
    if n == 0: 
        return 2
    if n == 1: 
        return 1
    return lucas_fast(n-1) + lucas_fast(n-2)

@lru_cache(maxsize=None)
def fib_with_lucas(n):
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    i = n // 2
    j = n - i
    return (fib_with_lucas(i) * lucas_fast(j) + fib_with_lucas(j) * lucas_fast(i)) // 2

def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return end_time - start_time, result

def compare_methods():
    Ns = [0, 1, 2, 10, 15, 20, 25, 30, 35]
    times_std = []
    times_fast = []
    
    for n in Ns:
        time_std, result_std = measure_time(fibonacci, n)
        times_std.append(time_std)
        
        time_fast, result_fast = measure_time(fib_with_lucas, n)
        times_fast.append(time_fast)
        
        match = result_std == result_fast
        
        print(f"{n}\t{time_std:.6f}\t{time_fast:.6f}\t{match}")
    
    return Ns, times_std, times_fast

def plot_results(Ns, times_std, times_fast):
    plt.figure(figsize=(10, 6))
    plt.plot(Ns, times_std, label='Стандартная рекурсия', marker='o', linewidth=2)
    plt.plot(Ns, times_fast, label='fib_with_lucas', marker='x', linewidth=2)
    plt.yscale('log')  
    plt.xlabel('n')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени вычисления Fn')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    Ns, times_std, times_fast = compare_methods()
    plot_results(Ns, times_std, times_fast)