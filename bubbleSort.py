class BubbleSort():
    
    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-1,0,-1):
                print(j)
                if arr[j] < arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1], arr[j]
        print(arr)

BubbleSort().bubble_sort([
    3,2,5,73,1
])