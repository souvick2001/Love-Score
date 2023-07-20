import random
name1 = input("Enter your name : ")
name2 = input("Enter your partner name : ")
LoveScore = random.randint(1, 100)
# print (f"Your love score is : {LoveScore}")
if LoveScore <50 :
  print (f"Your love score is : {LoveScore} 🥲")
else:
  print (f"Your love score is : {LoveScore} 🎉🎊" )
