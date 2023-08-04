class StringManager():

    def charCounter(self, string, s):

        c = 0
        for i in string:
            if i == s:
                c += 1
        return c
    
    def char_1st_non_repeated(self, string):
        repetor = {}
        
        for i in string:
            if repetor.get(i) == None:
                repetor[i] = 1
            else:
                repetor[i] += 1

        for i in repetor.keys():
            if repetor[i] <= 1:
                return i

    def atoi(self, i_s):

        res = 0
        sign = 1

        if i_s[0] == '-' : 
            i_s=i_s[1:]
            sign = -1
        
        for i in range(len(i_s)):
            if i_s[i] == ' ':
                i+=1
                continue
            va = ord(i_s[i]) - ord('0')
            res = res * 10 + va
        return sign * res
        
obj_str = StringManager()

# print(
#     obj_str.charCounter("StringS","S")
# )

# print(
#     obj_str.char_1st_non_repeated('sssttring')
# )

# print(
#     obj_str.atoi("-  1  2   3")
# )

