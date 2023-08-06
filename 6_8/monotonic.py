def mono_array(nums):

    l = 0
    tone = {}
    while l<len(nums) -1:
        if nums[l] < nums[l+1]:
            tone['increase'] = True
        elif nums[l] > nums[l+1]:
            tone['decrease'] = True
        else:
            pass
        if len(tone.keys()) > 1: return False
        l+=1
    return True
print(mono_array([1,2,2,3]))