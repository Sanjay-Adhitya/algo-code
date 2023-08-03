def timeConversion(s):
    """
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.

    Note: 
    - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

    condition 1 :
        12 and am = 12 - 12
        not 12 and am = print(with out am) 
        12 and pm = 12
        not 12 and pm = print(+12 with out pm) 
    """
    ext = s[-2:]
    fir = s[:2]
    if ext == "AM":
        if fir == "12":
            return "00"+s[:-2][2:]
        else:
            return s[:-2]
    if ext == "PM":
        if fir == "12":
            return "12"+s[:-2][2:]
        else:
            return str(int(s[:2])+12)+s[:-2][2:]

print(timeConversion("12:01:00AM"))