#checks if number belongs to list returns (T,F)
def belong(ls, num):
    return num in ls

#Checks if numbers are in of one list is a part of another one
def is_subject(ls_a, ls_b):
    for x in ls_a: 
        if x not in ls_b:
            return False
    return True    

#If both lists equal to each other        
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

#Gets both groups together and if numbers repeats shows it only ones
def unify(lstA,lstB):
    union_lst = []
    union_lst += lstA
    same = intersect(lstA,lstB)
    for z in range(len(lstB)):
        flag = 0
        for x in range(len(same)):
            if same[x] == lstB[z]:
               flag = 1
        if flag != 1:
            union_lst.append(lstB[z])
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
    #Checker for empty lists
    if n != 0:
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

#Universal group maker
def build_universal():
    universal = []
    for i in range(1,101):
        universal.append(i)
    return universal

#Checks if list empty
def is_empty(lst):
    return len(lst) == 0

#Checks if list equal to universal
def is_universal(lst,universal):
    return are_equal(lst, universal)

def main():
    #Creates lists
    groups = ["A","B"]
    for i in range(len(groups)):
        name = groups[i]
        size = int(input("Enter the size of set %s\n"%name))
        groups[i] = build_set(size)
        print("%s set is"%name, groups[i])
        print()   
    
    #If natural number is a part of one of the lists
    natural = int(input("Enter a natural number: "))
    does = False
    for x in range(len(groups)):
        if belong(groups[x],natural) == True:
            does = True   
    if does == False:
        print("%d doesn't belong either to A or B"%natural)
    else:
        print("%d belongs to A or to B"%natural)
    
    #Short version of Intersect, Union and Symmetric difference prints
    checkers = [intersect(groups[0], groups[1]),unify(groups[0], groups[1]),sym_diff(groups[0], groups[1])]
    names = ["intersection","union","symmetric difference"]
    for c in range(len(checkers)):
        if is_empty(checkers[c]) == True:
            print("The %s of A and B is empty"%names[c])
        else:
            print("The %s of A and B is:"%names[c], checkers[c])
    
    #If universal print
    universal = is_universal(checkers[1], build_universal())
    if universal == True:
        print("A union B is equal to universal set")
    else:
        print("A union B is not equal to universal set")
main()
