class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i + " , self.img , "j", sep = "")

    def __add__(self, object):
        return Complex(self.real + object.real, self.img + object.img)
    
    def __sub__(self, object):
        return Complex(self.real - object.real, self.img - object.img)

num1 = Complex(1, 5)
num2 = Complex(3, 7)

num3 = num1 + num2

num3.showNumber()

num3 = num1 - num2

num3.showNumber()