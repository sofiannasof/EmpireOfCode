OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    
    if x == y:
        if operation == "conjunction":
            if x == 0:
                return False
            else:
                return True
        elif operation == "disjunction":
            if x==0:
                return False
            else:
                return True
        elif operation == "implication":
            if x == 0:
                return True
            elif y ==1:
                return True
            else:
                return False
        elif operation == "exclusive":
            return False
        elif operation == "equivalence":
            return True
            
    if x != y:
        if operation == "conjunction":
            return False
        elif operation == "disjunction":
            return True
        elif operation == "implication":
            if x == 0:
                return True
            elif y == 0:
                return False
            else:
                return False
        elif operation == "exclusive":
            return True
        elif operation == "equivalence":
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

    print("All done? Earn rewards by using the 'Check' button!")
