def ceaser_chiper(s, k):

    # Update alphabet_lower_dict to start digits from 0
    alphabet_lower_dict = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
        "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15,
        "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25
    }

    # Update alphabet_upper_dict to start digits from 0
    alphabet_upper_dict = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
        "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
        "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
        "Y": 24, "Z": 25
    }

    # Keys from the alphabet_lower_dict as a list
    alphabet_lower_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Keys from the alphabet_upper_dict as a list
    alphabet_upper_keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    final_str = ""
    
    for i in s:
    
        if i in alphabet_lower_dict.keys():
            index = alphabet_lower_dict[i]
            index = index + k
            if index <= 25:
                final_str += alphabet_lower_keys[index]
            else:
                final_str += alphabet_lower_keys[index%26]
            
        elif i in alphabet_upper_dict.keys():
            index = alphabet_upper_dict[i]
            index = index + k
            if index <= 25:
                final_str += alphabet_upper_keys[index]
            else:
                final_str += alphabet_upper_keys[index%26]
        else:
            final_str += i

    return final_str

print(ceaser_chiper("www.abc.xy", 87))