
from random import randint
for x in range(1,6):
   guessNumber=int(input("Enter your guess number between 1 to 5: "))
   randomNumber= randint(1,5)

   if randomNumber==guessNumber:
      print("You have won")
   else:
      print("You have lost")
