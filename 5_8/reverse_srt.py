def rev_srt(s):
    # l = 0
    # r = len(s)-1
    s1 = ''
    # while l<r:
    #     temp = s[l]
    #     s[l] = s[r]
    #     s[r] = temp
    #     l+=1
    #     r-=1
    # return s
    for i in range(len(s)-1,-1,-1):
        s1 += s[i]
    return s1
print(rev_srt("qwert"))