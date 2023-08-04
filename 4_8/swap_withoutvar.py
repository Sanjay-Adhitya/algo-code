def swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b

def swap_char(a,b):
    a,b = ord(a),ord(b)
    a = a + b
    b = a - b
    a = a - b
    return chr(a),chr(b)
