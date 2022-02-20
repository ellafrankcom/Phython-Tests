#List comprehension
row = int(input("Please input the amount of rows "))
col = int(input("Please input the amount of columns "))
list1= [[0.0 for j in range(col)] for i in range(row)]

for i in range(row):
        for j in range(col):
            print(list1[i][j], end=" ")
        print()

for i in range(row):
        for j in range(col):
           list1[i][j] = float(input("[{}][{}] :: ".format(i,j)))
     
for i in range(row):
        for j in range(col):
            print("{:10.4f}".format(list1[i][j],end =" "))
        print()

