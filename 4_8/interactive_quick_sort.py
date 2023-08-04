from stack import Stack

def partition(array,left,right):
    pivot = array[right]
    i = left - 1
    

def inter_quick_sort(array):
    stack_1 = Stack(len(array))
    
    stack_1.push([0,len(array) -1])
    while stack_1.is_empty():
        range_to_sort = stack_1.pop()
        left, right = range_to_sort
        if left < right:
            pass

inter_quick_sort([1,4,2,0,8])