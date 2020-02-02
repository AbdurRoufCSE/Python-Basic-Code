class student:
    name=""
    roll=""
    cgpa=""
    def set_value(self, name, roll, cgpa):
        self.name=name
        self.roll=roll
        self.cgpa=cgpa

    def disply(self):
        print(f"Name:{self.name} Roll:{self.roll} CGPA:{self.cgpa}")
rouf=student()
rouf.set_value("Abdur Rouf",101,3.97)
rouf.disply()

betall=student()
betall.set_value("Betall",102,3.95)
betall.disply()