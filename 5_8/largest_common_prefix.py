def lar_com_pre(strings):

    min_length = min(len(s) for s in strings)

    for i in range(min_length):

        char = strings[0][i]
        
        for string in strings:
            if string[i] != char:
                return string[:i]
    
    return strings[0][:min_length]

print(lar_com_pre(
    [
        "ABCD",
        "ABAD",
        "ABED"
    ]
))