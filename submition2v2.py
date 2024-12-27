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
    print(union_lst)
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
    print(dif)
    return dif
    
def main():      
    a = [1,2,3,4,5]
    b = [4,3,8,9]
    c = [1,2,3,4,5]
    n = 3
    difference(a,b)
main()    
