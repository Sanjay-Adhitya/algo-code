def reverse_int(int_):
    value = 0
    final = 1
    if int_ < 0:
        int_ = int_ * -1  
        final = -1  
    while int_ > 9:
        value = (value*10) + int_ % 10
        int_ = int_//10
    return ((value*10) + int_)*final

print(reverse_int(-123))