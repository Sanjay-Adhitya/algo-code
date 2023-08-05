def dna_sequence(string):

    subs = {}
    
    for i in range(0, len(string)):
        if subs.get(string[i:i+10]):
            subs[string[i:i+10]] += 1   
        else:
            subs[string[i:i+10]] = 1

    for i in subs.keys():
        if subs[i] >= 2:
            yield i
    
    
print(list(dna_sequence("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))