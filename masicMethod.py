class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color


    def disply(self):
        print(f"Name = {self.name}, Color = {self.color}")
bike1 = Bike("Rouf","Blue")
bike2 = Bike("Rouf","Blue")

print(bike1 == bike2 )

