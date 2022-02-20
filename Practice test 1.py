#Practice 1, Q1

class sum_dataC:
    def __init__(self, harry = []):
        self.harry = harry

    def sum_data(self):
        sum1 = 0
        for i in self.harry:
            sum1 += i
        return sum1

class double_Val:
    def __init__(self, innes = []):
        self.innes = innes

    def loop(self):
        j = 0
        for i in innes:
            self.innes[j] = self.innes[j]**2
            j += 1
        return


class final(sum_dataC, double_Val):
    def __init__(self, harry, innes):
        double_Val.__init__(self, innes)
        sum_dataC.__init__(self, harry)
        
    def get_harry(self):
        return self.harry


    def get_innes(self):
        return self.innes

class final_extended(final):
    def __init__(self, sum_dataC, double_Val):
        super().__init__(sum_dataC, double_Val)

    def get_var(self):
        return self.harry

    def set_var(self):
        print(self.innes)
        while True:
            value = int(input("Input value between -5 and 10"))
            if value >= -1 and value <=10:
                self.innes.append(value)
                break
        

harry = [1, 12, 24, 33]
innes = [6, 3, 8, 7]
X = final(harry, innes)
print(X.sum_data()) 
X.loop()
print(X.get_harry())
print(X.get_innes())

z = final_extended(harry, innes)
print(z.sum_data())
z.set_var()
print(z.get_var())

    
