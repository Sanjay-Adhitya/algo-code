class MergeSort():

    def merge_sort(self,arr):
        if len(arr) <= 1:   return arr
        mid = len(arr) // 2
        sorted_r_arr = self.merge_sort(arr[:mid])        
        sorted_l_arr = self.merge_sort(arr[mid:])

        return self.compare_merge(sorted_r_arr,sorted_l_arr)

    def compare_merge(self, r_arr,l_arr):

        i_r,i_l,merged = 0,0,[]

        while i_r < len(r_arr) -1 and i_l < len(l_arr):
            if r_arr[i_r] < l_arr[i_l]:
                merged.append(r_arr[i_r])
                i_r+=1
            else:
                merged.append(l_arr[i_l])
                i_l+=1

        merged += l_arr[i_l:]
        merged += r_arr[i_r:]
        return merged

arr = MergeSort().merge_sort([2,8,3,4,1,4,0])
print(arr)