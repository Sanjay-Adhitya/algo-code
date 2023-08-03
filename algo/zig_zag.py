def zig_zag(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    print(a)
    while(st < ed):
        print(f"st - {st} {a[st]} ed - {ed} {a[ed]}")
        a[st], a[ed] = a[ed], a[st]
        print(a)
        st = st + 1
        ed = ed - 1
    
    return a

print(zig_zag([1,2,3,4,5,6,7,8,9],9))



