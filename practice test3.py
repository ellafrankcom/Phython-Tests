#revision for test
class Data1:
    def __init__(self, list1):
        self.list1 = list1

    def createNewL(self, list1 = None):
        del(self.list1) #delete object's list1
        if list1 == None:
            datainput = input("Enter a set of values all on one line each seperated by a space: ")
            self.list1 = [] #create new list
            for i in datainput.split(): #create new list using user input, seperated by split
                self.list1.append(float(i))
        else:
            self.list1 = list1
        print(self.list1)
        

    def appendV(self, list1 = None):
        if list1 == None:
            datainput = input("Enter a set of values all on one line each seperated by a space: ")
            for i in datainput.split(): #create new list using user input, seperated by split
                self.list1.append(float(i))
        else:
            self.list1 += list1
        print(self.list1)

    def get_dat(self):
        return self.list1


class sum1(Data1):
    def __init__(self, list1):
        Data1.__init__(self, list1)

    def printdata(self): #will loop through elements of self.list1
        for i in self.list1:
            print(i)

    def sum_data(self):
        return sum(self.list1)
    
"""
#For Testing
x1 = [1,2,3]
a = Data1(x1)
y = [6, 7, 8]
a.createNewL()
a.createNewL(y)
a.appendV()
a.appendV([7, 99, 100])

z = [2,4,6]
b = sum1(z)
print(b.get_dat())
b.printdata()
print("Sum of list elements object b = {}".format(b.sum_data()))
"""

N1 = []
for i in range(10):
    N1.append(i)
x = sum1(N1)
print("Sum of list elements object x = {}".format(x.sum_data()))

k = [1, 8, 9, 10]
x.appendV(k)
x.printdata()

x.appendV()
x.printdata()

Z = [2.4, 6, 8]
x.createNewL(Z)
x.printdata()

m = [99, 88, 77]
x2 = sum1(m)
x2.appendV(x.get_dat())
x2.printdata()
