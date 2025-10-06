import random
import time
import matplotlib.pyplot as plt


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, data):
    start_time = time.perf_counter()
    sort_func(data.copy())
    end_time = time.perf_counter()
    return end_time - start_time

sizes = list(range(100, 1001, 100))
selection_times_random = []
quick_times_random = []
selection_times_sorted = []
quick_times_sorted = []
selection_times_reverse = []
quick_times_reverse = []

for size in sizes:
    random_data = [random.randint(1, 1000) for _ in range(size)]
    selection_times_random.append(measure_time(selection_sort, random_data))
    quick_times_random.append(measure_time(quick_sort, random_data))
    
    sorted_data = list(range(size))
    selection_times_sorted.append(measure_time(selection_sort, sorted_data))
    quick_times_sorted.append(measure_time(quick_sort, sorted_data))
    
    reverse_data = list(range(size, 0, -1))
    selection_times_reverse.append(measure_time(selection_sort, reverse_data))
    quick_times_reverse.append(measure_time(quick_sort, reverse_data))

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(sizes, selection_times_random, label='Selection Sort', marker='o')
plt.plot(sizes, quick_times_random, label='Quick Sort', marker='s')
plt.xlabel('Размер массива')
plt.ylabel('Время (секунды)')
plt.title('Случайные данные')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(sizes, selection_times_sorted, label='Selection Sort', marker='o')
plt.plot(sizes, quick_times_sorted, label='Quick Sort', marker='s')
plt.xlabel('Размер массива')
plt.ylabel('Время (секунды)')
plt.title('Отсортированный массив')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(sizes, selection_times_reverse, label='Selection Sort', marker='o')
plt.plot(sizes, quick_times_reverse, label='Quick Sort', marker='s')
plt.xlabel('Размер массива')
plt.ylabel('Время (секунды)')
plt.title('Обратно отсортированный массив')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()