def most_difference(*args):
    numbers = list(args)
    if not numbers:
        temp = 0
    else:
        max = numbers[0]
        min = numbers[0]
        
        print(max)
        print(min)
    
        for i in range(0,len(numbers)):
            if numbers[i] > max:
                max = numbers[i]
        
        for i in range(0,len(numbers)):
            if numbers[i] < min:
                min = numbers [i]
        
        temp = max-min
    
    return temp


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(most_difference(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(most_difference(5, 5), 0, 3), "5-5=0"
    assert almost_equal(most_difference(10.2, 2.2, 0.00001, 1.1, 0.5), 10.199, 3), "10.2-(0.00001)=10.19999"
    assert almost_equal(most_difference(), 0, 3), "Empty"

    print("All set? Click 'Check' to review your code and earn rewards!")
