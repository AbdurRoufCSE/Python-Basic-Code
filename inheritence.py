class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")
class Samsung(Phone):#inherited Phone class that's why Phone is parent class/super class/Base class
       def photo(self):
        print("You can take photo")


s=Samsung()
s.call()
s.message()
s.photo()
print(issubclass(Samsung,Phone))