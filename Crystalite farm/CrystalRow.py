def check_line(line):
    listline = list(line)
    even = []
    odd = []
    
    for i in range(0,len(listline)):
        if i%2 == 0:
            even.append(listline[i])
        else:
            odd.append(listline[i])


    if len(unique(even))==1: 
            if  len(unique(odd))==1:
                if unique(even) != unique(odd):
                    return True

    
    return False

def unique(data):
    datalist = list(data)
    uniqued = list(set(datalist))

    return uniqued
    

            

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_line(["X", "Z", "X"]) == True
    assert check_line(["X", "Z", "X", "X"]) == False
    assert check_line(["X", "Z"]) == True
    assert check_line(["Z", "X"]) == True
    assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
