def main(coins):
    change = 0
    for i in coins:
        if i <= change+1:
            change+=i
        else:
            return change+1
        
        
print(main([1,1,2,3,5,7,22]))