class Stack():

    def __init__(self, length) -> None:
        
        self.table = [None]*length
        self.top = length 
        self.bottom = 0
        self.current = 0

    def push(self, element):
        if not self.is_full():
            index = self.current 
            while self.table[index] is not None:
                index += 1
            self.table[index] = element
            self.current += 1
            return True
        else:
            return -1

    def pop(self):
        if not self.is_empty():
            element =  self.table[self.current -1]
            self.table[self.current - 1] = None
            self.current -= 1
            return element
        return -1
    
    def size(self):
        return self.current
    
    def is_empty(self):
        if self.current != self.bottom:
            return False
        return True
    
    def is_full(self):
        if self.current != self.top:
            return False
        return True
                
