class student:
    name=""
    roll=""
    gpa=""
    def __init__(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa
    def disply(self):
        print(f"Name:{self.name} Roll:{self.roll} GPA:{self.gpa}")

rouf=student("Abdur Rouf",101,5.00)
rouf.disply()

betall=student("Betall",102,4.59)
'''betall.name="Betall"
betall.roll=102
betall.gpa=4.95'''
betall.disply()