#question5
class stat1:
    def __init__(self, *numb):   #initialize variables
        self.data = []
        self.read_data(numb)
        self.min1 = 99E999
        self.max1 = -99E999
        self.aver = 99E999

    def read_data(self, numb):   #reads and stores set of numbers
        for i in numb:
            self.data.append(i)

    def sum_data(self):      #adds set of data values
        self.sumd = sum(self.data)

    def range(self):   #sets the min and max values for data set
        self.min1 = 99E9999
        self.max1 = -99E999
        for i in self.data:
            if i > self.max1:
                self.max1 = i
            if i < self.min1:
                self.min1 = i
        #print(self.min1, "-", self.max1)

    def get_range(self):  #returns the min and max values
        if self.min1 == 99E999:
            print("Range called")
            self.range()
        return self.min1, self.max1

    def clear_d(self):   #clears the data set
        del self.data[:]

    def add_dat(self, n1):   #adds a single value to the data set
        self.data.append(n1)

    def average(self):  #generates the average
        self.sum_data()
        ndat = len(self.data)
        self.aver = self.sumd/ndat

    def get_average(self):  #returns the average
        if self.aver == 99E999:
            self.average()
        return self.aver

    def num_data(self):  #returns number of items in set
        return len(self.data)

    def get_data(self): #returns data set
        return self.data

    def printobj(self, obj1 = None):  #prints object
        if obj1 != None:
            print(obj1.get_data())
        else:
            print(self.data)
            
            
        
P = stat1(1,2,-3,4)
print(P.num_data())
P.average()
min1,max1 = P.get_range()
print(min1,max1)
P.clear_d()
P.add_dat(9)
P.add_dat(8)
P2 = stat1(1,2,-3,4)
P2.range()
min1,max1 = P2.get_range()
print(min1,max1)
P2.printobj(P)

