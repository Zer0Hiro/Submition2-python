def belong(ls, num):
    return num in ls

def is_subject(ls_a, ls_b):
    return ls_a in ls_b

def are_equal(ls_a, ls_b):   
    return (ls_a in ls_b) and (ls_b in ls_a)

def intersect(lstA,lstB):
    int_lst = []
    for i in range(len(lstA)):
        for x in range(len(lstB)):
            if lstA[i] == lstB[x]:
                int_lst.append(lstB[x])
    print(int_lst)
    return int_lst

def main():      
    a = [1,2,3,4,5]
    b = [5,6,7,8,9]
    c = [1,2,3,4,5]
    n = 3
    intersect(a,b)
main()    
