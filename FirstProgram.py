class Car:
    color = "Black"

    def __init__(self, color):
        self.color = color

    def start(self):
        print("Starting")
    
    def stop(self):
        print("Stopping")


class Tarzan(Car):
    nickName = "Tarzaan"

    def __init__(self, color):
        super().__init__(color)

    def showColor(self):
        print(self.color)
    


merc = Tarzan("Red")

merc.showColor()