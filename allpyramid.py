print("Which type of pyramid do you want to print \n1 - Center Pyramid\n2 - Left Pyramid\n3 - Right Pyramid")
user = int(input(">>"))
if user == 1:
    rows = int(input("Enter the number of rows : "))
    k = 2* rows - 2
    for i in range(0,rows):
        for j in range(0,k):
            print(end=" ")
        k = k -2
        for j in range(0,i+1):
            print("  * ",end="")
        print("")
        
elif user == 2:
    rows = int(input("Enter the number of rows : "))
    for i in range(0,rows+1):
        print("* "*int(i))
        
elif user == 3:
    rows = int(input("Enter the number of rows : "))
    k = 2* rows - 2
    for i in range(0,rows):
        for j in range(0,k):
            print(end=" ")
        k = k -2
        for j in range(0,i+1):
            print("* ",end="")
        print("")
else:
    print("Please enter valid number")