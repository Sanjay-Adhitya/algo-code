def is_palindrome(num):

    rev_num = reverse_num(num)

    return num == rev_num

def reverse_num(num):
    value = 0
    final = 1
    if num < 0:
        num= num * -1
        final = -1
    while num < 9:
        value = (value*10 )+ num%10
        num = num//10
    return ((value*10 )+ num)*final

print(is_palindrome(-29293933939292))