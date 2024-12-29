def belong(ls, num):
    return num in ls

def is_subject(ls_a, ls_b):
    for x in ls_a: 
        if x not in ls_b:
            return False
    return True    
        
def are_equal(ls_a, ls_b):
    return is_subject(ls_a, ls_b) and is_subject(ls_b, ls_a)

#If number is in A and B shows which number is it
def intersect(lstA,lstB):
    int_lst = []
    for i in range(len(lstA)):
        for x in range(len(lstB)):
            if lstA[i] == lstB[x]:
                #Only if number in A equal to number in B
                int_lst.append(lstB[x])
    return int_lst

#Gets both lists together and if numbers repeats shows it only ones
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

#Basically A-B but if number: doesnt exist in B == save | exists in B != save
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

#Unify both differences same as unify but more numbers will be removed to show them only ones
def sym_diff(lstA,lstB):
    Alist = difference(lstA, lstB)
    Blist = difference(lstB, lstA)
    result = unify(Alist, Blist)
    return result

#Creates a list of a group
def build_set(n):
    lst = []
    count = 0
    print("Enter %d natural numbers between 1 to 100, with no repetitions:"%n)
    while count != n:
        a = int(input())
        flag = False
        if 0 < a <= 100:
            for i in lst:
                if i == a:
                    flag = True
            if flag == False:
                count += 1
                lst.append(a)
            else:
              print("Wrong input")  
        else:
            print("Wrong input")
    return lst

def build_universal():
    universal = []
    for i in range(1,101):
        universal.append(i)
    return universal

def is_empty(lst):
    return len(lst) == 0

#Need are - equal!!!
# def is_universal(lst,universal):

def main():
    lists = ["A","B"]
    for i in range(len(lists)):
        name = lists[i]
        size = int(input("Enter the size of set %s\n"%name))
        lists[i] = build_set(size)
        print("%s set is"%name, lists[i])
        print()
    natural = int(input("Enter a natural number: "))
    
    does = False
    for x in range(len(lists)):
        if belong(lists[x],natural) == True:
            does = True   
    if does == False:
        print("%d doesn't belong either to A or B"%natural)
    else:
        print("%d belongs to A or to B"%natural)
    
    inter = intersect(lists[0], lists[1])
    if is_empty(inter) == True:
        print("The intersection of A and B is empty")
    else:
        print("The intersection of A and B is", inter)
    
    
main()
    
