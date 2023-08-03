def towerBreakers(n, m):
    # Write your code here
    if m == 1: 
        return 2
    else:
        if n % 2 == 1:
            return 1
        else:
            return 2

print(towerBreakers(
    729771, 591431
))