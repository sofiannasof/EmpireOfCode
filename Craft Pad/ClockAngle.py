def clock_angle(time):
    hours, min = time.split(":");
    nhours = int(hours)
    nmin = int(min)
    angle = 0
    
    if nhours > 12:
        nhours = nhours - 12
    
    nhours = nhours*30 + ((nmin/60)*30)
    nmin = (nmin)/60*360
    angle = abs(nmin - nhours) 

    if angle >  180:
        angle = 360 - angle
    
    if angle == 0.0:
        return 0

    ssangle = str(format(angle, '.1f'))

    if '.' in ssangle:
        return float(ssangle)
    else:
        return int(ssangle)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
