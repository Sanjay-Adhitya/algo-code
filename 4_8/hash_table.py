class Hash_Table_cus():

    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size
    
    def insert(self, key) -> bool:
        index = self.hash_keys(key) # this is most important logic
        while self.table[index] is not None:
            index = (index + 1) % self.size 
        self.table[index] = key
    
    def hash_keys(self, keys) -> int:
        return keys % self.size
    
    def contains(self, key):
        index = self.hash_keys(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == initial_index:
                break
        return False

    def get_data(self):
        return self.table

array = [5,66,8,7,6,9]
unique_set = Hash_Table_cus(len(array))
print(unique_set.get_data())

for i in array:
    unique_set.insert(i)

print(unique_set.contains(60))