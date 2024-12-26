def belong(ls, num):
    num in ls
    False
    num not in ls
    return True
def is_subject(ls_a, ls_b):
    ls_a in ls_b
    return True
    ls_a not in ls_b
    return False
def are_equal(ls_a, ls_b):
    ls_a in ls_b and ls_b in ls_a
    return True
    ls_a not in ls_a or ls_b not in ls_a
    return False
    


def main():
            
    a = [12345]
    b = [123456789]
    c = [12345]
    n = 6
    print(belong(a, n))
    print(is_subject(a, b))
    print(are_equal(a, c))
main()    
