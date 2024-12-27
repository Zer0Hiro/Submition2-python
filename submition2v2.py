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
    return int_lst

def unify(lstA,lstB):
    union_lst = lstA
    same = intersect(lstA,lstB)
    for i in range(len(lstB)):
        flag = 0
        for x in range(len(same)):
            if same[x] == lstB[i]:
               flag = 1
        if flag != 1:
            union_lst.append(lstB[i])
    return union_lst

def difference(lstA,lstB):
    dif = []
    for i in range(len(lstA)):
        flag = 0
        for x in range(len(lstB)):
            if lstA[i] == lstB[x]:
                flag = 1
        if flag != 1:
            dif.append(lstA[i])
    return dif

def sym_diff(lstA,lstB):
    Alist = difference(lstA, lstB)
    Blist = difference(lstB, lstA)
    result = unify(Alist, Blist)
    return result

def main():      
    a = [23,56,4,67]
    b = [12,45,4]
    c = []
    n = 3
    if belong(c,n) == True:
        print("%d belongs to A or to B"%n)
    else:
        print("%d doesn't belong either to A or B"%n)
    print(sym_diff(c,b))
main()    
