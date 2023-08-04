from datetime import datetime
class BucketSort():

    def divide_by_10s(self, *args):
        min = args[0]
        max = args[0]
        bucketList = []
        for i in args:
            if min > i:
                min = i
            if max < i:
                max = i
        for i in range(min-1, max, 10):
            temp = []
            for j in args:
                if j < i+10 and j > i:
                    temp.append(j)
            if len(temp) > 0:
                bucketList.append(temp)
        return bucketList
    
    def merge_sort(self, array):        
        if len(array) <= 1:return array
        mid = len(array)//2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])
        return self.compare_merge(left_half, right_half) 
    
    def compare_merge(self,  left_half, right_half):
        i_l = 0
        i_r = 0
        merged = []
        while i_l >= 1 and i_r >= 1:
            if left_half[i_l] > right_half[i_r]:
                merged.append(left_half[i_l])
                i_l += 1
            else:
                merged.append(right_half[i_r])
                i_r += 1
        merged += left_half[i_l:]
        merged += right_half[i_r:]
        return merged
    
    def __init__(self, array): 
        divided = self.divide_by_10s(array)
        out = []
        # out = [self.merge_sort(i) for i in divided]
        # for i in divided:
        #     out.extend(self.merge_sort(i))
        [out.extend(x) for x in list(map(self.merge_sort,divided))]
        print(out)

# BucketSort([2,3,74,18,6,5])


arr = [1,2,3,4,5,6,7,8]
arr_ = [2,3,74,18,6,5]

def sqre(*args):
    print(args[0]*args[1]) 

# print(list(map(sqre,arr,arr_)))



def log_datetime(func):
    '''Log the date and time of a function'''
    def wrapper(*args, **kwargs):
        print(
            f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        return func(*args, **kwargs)
    return wrapper

@log_datetime
def one(*args):
    def two(*args):
        print(args)
    return two(args)

one([1,2,3,4])