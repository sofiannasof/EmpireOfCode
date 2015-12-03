def count_units(number):
    return str('{0:b}'.format(number)).count('1')

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_units(4) == 1
    assert count_units(15) == 4
    assert count_units(1) == 1
    assert count_units(1022) == 9

    print("Use 'Check' to earn sweet rewards!")
