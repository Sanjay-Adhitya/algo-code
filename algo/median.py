import time


def findMedian(arr):
    # Write your code here
    
    sorted_data = quick_sort(arr)
    print(sorted_data)
    return sorted_data[round(len(sorted_data)/2)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [i for i in arr if i < pivot]    
    right = [i for i in arr if i > pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
    

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds.")
        return result
    return wrapper

check_obj = time_it(findMedian)
check_obj([9, 2, 5, 1, 7, 4, 8, 6, 3])