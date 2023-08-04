class CountingSort():

    def get_count_array(self,array):
        max_ = max(array)
        min_ = min(array)
        return [0 for i in range(min_,max_)]

    def count_array_audit(self,array):
        counting_array = self.get_count_array(array)
        for i in arr: counting_array[i - 50] += 1
        return counting_array
    
    

obj = CountingSort()
arr = [50,60,790,3,90]
counting_array = obj.get_count_array(arr)

