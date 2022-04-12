import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

Your_Input=input("Enter Your Choise Rock for 0,Paper for 1,Scissor for 2 : ")
Random_Num = random.randint(0,2)
if(Random_Num==0):
  ComputerOutput= Rock
elif(Random_Num==1):
  ComputerOutput= Paper
elif(Random_Num==2):
  ComputerOutput= Scissor

print(f"Your Choise is {Your_Input}")
if(Your_Input==0):
  print(Rock)
elif(Your_Input==1):
  print(Paper)
elif(Your_Input==2):
  print(Scissor)


print(f"Computer Choise is ")
print(ComputerOutput)