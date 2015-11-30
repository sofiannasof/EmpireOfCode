def count_inversion(sequence):
    numbers = list(sequence)
    count = 0
    
    nums = list(numbers)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
                count=count+1


    return count;


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
