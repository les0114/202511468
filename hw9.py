
class point:
    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y

    def show(self):
        print(f'({self.x}, {self.y})')
        
    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)


class rectangle:
    def __init__(self, x1, y1, x2, y2):
        
        self.lt = point(x1, y1)  
        self.rb = point(x2, y2)  

    def show(self):

        print(f'좌측 상단 꼭지점: ({self.lt.x}, {self.lt.y})')
        print(f'우측 하단 꼭지점: ({self.rb.x}, {self.rb.y})')

    def getwidth(self):

        return self.rb.x - self.lt.x

    def getheight(self):

        return self.rb.y - self.lt.y

    def getarea(self):
        
        return self.getwidth() * self.getheight()

    def getperimeter(self):
        
        return 2 * (self.getwidth() + self.getheight())




if __name__ == '__main__':
    
    r1 = rectangle(5, 5, 20, 10)


    
    a = r1.getarea()
    p = r1.getperimeter()

    
    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')
