def belong(ls, num):
    return num in ls

def is_subject(ls_a, ls_b):
    return ls_a in ls_b

def are_equal(ls_a, ls_b):   
    return (ls_a in ls_b) and (ls_b in ls_a)


def main():
            
    a = [1,2,3,4,5]
    b = [1,2,3,4,5,6,7,8,9]
    c = [1,2,3,4,5]
    n = 3
    print(belong(a, n))
    print(is_subject(a, b))
    print(are_equal(a, c))
main()    
