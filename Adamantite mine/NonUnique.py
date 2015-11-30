def non_unique(data):
    datalist = list(data)
    non_uniqued = list(data)

    for i in range(0,len(datalist)):
        if count(datalist[i],datalist) == 1:
            non_uniqued.remove(datalist[i])
    
    return non_uniqued
    
def count(num, data):
    count = 0
    if type(num) is str:
        for i in range(0,len(data)):
            if type(data[i]) is str:
                if num.lower() == data[i].lower():
                    count = count + 1        
    else:
        for i in range(0,len(data)):
            if num == data[i]:
                count = count + 1
    return count
            



if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

    # Rank 2
    assert non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                       'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                       'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A', 'P', 'A', 'j', 'p', 7], "Letters"

    print("All done? Earn rewards by using the 'Check' button!")
