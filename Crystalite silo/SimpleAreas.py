import math

def simple_areas(*args):
    area = list(args)

    if len(area) == 1:
        return math.pi*math.pow((area[0]/2),2)
    elif len(area) == 2:
        return area[0]*area[1]
    elif len(area) == 3:
        r = (area[0] + area[1] + area[2] ) / 2
        return math.sqrt(r*(r-area[0])*(r-area[1])*(r-area[2]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")
