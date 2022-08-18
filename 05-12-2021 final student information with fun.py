stud = []

c = 'y'

def Add():
    ch = 'y'
    while ch == 'y' :
        print("-------------------------------------")
        r = int(input("Enter the Roll number     : "))
        n = input("Enter the Name            : ")
        p = input("Enter the Percentage      : ")
        print("-------------------------------------")
        ch  = input("do you want to add more records 'y' / YES 'n' / NO : ")
        stud_data = [r ,n ,p]
        stud.append(stud_data)

def Search():
    flag = 0
    roll = int(input("Enter the Roll number to be searched : "))
    for i in range (len(stud)) :
        if stud[i][0]==roll :
            print("Roll number : ", stud[i][0])
            print("Name : ", stud[i][1])
            print("Percentage : ", stud[i][2])
            print("-------------------------------------")
            flag = 1
    if flag == 0 :
        print("Not Found !")

def Update():
    s = len(stud)
    up = 'y'
    while up == 'y' :
        
        print(stud)
        print()
        
        roll = int(input("Search the Roll Number to be updated : "))
        flag = 0
        
        print("********** Detail are here ********** ")
        for i in range (s) :
            if stud[i][0] == roll :
                print("Roll number : ", stud[i][0])
                print("Name : ", stud[i][1])
                print("Percentage : ", stud[i][2])
                print("-------------------------------------")
                flag = 1
                print("1.Roll number  2.Name  3.Percentage ")
                search = int(input("Enter the choice :  ")      )
                if search == 1 :
                    if stud[i][0] == roll:
                        
                        print("rollno: " , stud[i][0])
                        print("Name:   " , stud[i][1])
                        print("Per:    " , stud[i][2])
                        print()                           
                        Nroll = int(input("Enter the new rollno:  "))
                        stud[i][0] = Nroll
                        print("rollno: " , stud[i][0])
                        print("Name:   " , stud[i][1])
                        print("Per:    " , stud[i][2])
                        print("****record is updated*******")
                        print()
                        break
                    
                elif search == 2 :
                    
                    Nname = input("Enter the New Name :  ")
                    stud[i][1] = Nname
                    print("********** Details are here *********")
                    print("rollno: " , stud[i][0])
                    print("Name:   " , stud[i][1])
                    print("Per:    " , stud[i][2])
                    print("****record is updated*******")
                    print()
                    break
                
                elif search == 3:
                    
                    Nper = int(input("Enter the New percentage :  "))
                    stud[i][2] = Nper
                    print("********** Details are here *********")
                    print("rollno: " , stud[i][0])
                    print("Name:   " , stud[i][1])
                    print("Per:    " , stud[i][2])
                    print("****record is updated*******")
                    print()
                    break
                
                else:
                    print("Not found the option!")
                
        up = input("Do you want to continue:  'y'  /  'n'  ")
                       
        if flag == 0:
            print("Record not found please don't retry :  ")
            break

def Delete():
    Droll = int(input("Enter the Roll Number to delete the record : "))
    flag = 0
    
    for i in range (len(stud)) :
        if stud[i][0] == Droll :
            print("rollno: " , stud[i][0])
            print("Name:   " , stud[i][1])
            print("Per:    " , stud[i][2])
            flag = 1
            
            d = "y"
            d = input("Enter 'y' to delete the record || 'n' to cancle the deletation : ")
            
            if d == "y" :
                stud.pop(i)
                print("Record has been deleted ")
            break
def Display():
    a = int(input("Select the choice  1. All Records 2. Individual Records : "))
    if a == 1 :            
        for i in range (len(stud)) :            
            print("-------------------------------------")
            print("Roll number : ", stud[i][0])
            print("Name : ", stud[i][1])
            print("Percentage : ", stud[i][2])
            print("-------------------------------------")
    elif a == 2 :
        flag = 0
        roll = int(input("Enter the Roll number to be searched : "))
        for i in range (len(stud)) :
            if stud[i][0]==roll :
                print("Roll number : ", stud[i][0])
                print("Name : ", stud[i][1])
                print("Percentage : ", stud[i][2])
                print("-------------------------------------")
                flag = 1
        if flag == 0 :
            print("Not Found !")
    

while c == 'y' :
    print("-----------------------------------------")
    print("Enter the choice give below : ")
    print("1. Add Record ")
    print("2. Search  Record")
    print("3. Update Record ")
    print("4. Delete Record")
    print("5. Display Record ")
    print("------------------------------------------")

    choice = int(input("Enter the choice : "))
    if choice == 1 :
        Add()
    elif choice == 2 :
        Search()
    elif choice == 3 :
        Update()
    elif choice == 4 :
        Delete()
    elif choice == 5 :
        Display()
