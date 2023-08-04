def remove_duplicate(array):
    uninques = {}
    for i in array:
        try: uninques[i]
        except: uninques[i] = True 
    return list(uninques.keys())
array = [8,8,8,9,30,'a']

print(remove_duplicate(array=array))