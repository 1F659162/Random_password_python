import random
while True  :
    Max = int(input("Enter max number : "))
    total = ''
    Sum = 0

    if total == '' :
        for i in range (1 , Max+1 , 1):
            rand_int = str(random.randint(0,9))
            rand_a_z = random.choice('abcdefghijklmnopqrstuvwxyz')
            rand_A_Z = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            
            total += random.choice([rand_int , rand_a_z])
    print("random >> " , total)
    print("\nEnter c tocontinue.")
    print("Enter e to exit.")
    CR = input("Enter : ")
    if(CR == 'c') :
        print()
        continue
    else :
        break
