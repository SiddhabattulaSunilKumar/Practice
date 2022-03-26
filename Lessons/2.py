# print("hello"[4])

# noOfChar = len(input("what is your name..? : "))
# print(type(noOfChar))
# noOfChar_new = str(noOfChar)
# print("your name char = "+noOfChar_new+" Character")

# this exercise to print of one give numbr (example input 36 - output 3+6 = 9)

# YourInputNumber = input("Enter two digit number : ")
# YIN1 = int(YourInputNumber[0])
# YIN2 = int(YourInputNumber[1])
# YIN3 = YIN1 + YIN2
# print("Your output is : "+str(YIN3))

#**********BMI Calculator************
# YourHeight = float(input("Enter your Height in meter : "))
# YourWeight = float(input("Enter your Wight in KG : "))
# BMI=YourWeight/(YourHeight**2)
# print(int(BMI))
# print("%.0f" % BMI)

#*******No of Years, Months, Weeks, Days left in your life******
# YourAge = int(input("Please enter your age : "))
# YearsLeft = 90-YourAge
# MonthsLeft = YearsLeft*12
# WeeksLeft = YearsLeft * 52
# DaysLeft = YearsLeft*365
# print(f"Years Left : {YearsLeft}, Months Left : {MonthsLeft}, Weeks left : {WeeksLeft}, Days Left : {DaysLeft} ")

#**********Tip Calculator with round 2 decimal places**********
totalBill = float(input("Enter Total bill : "))
NoOfPeopel = int(input("Enter no of people bill need to convert : "))
TipPaid = int(input("Enter the tip you want to pay : "))
TotalTipPaid = 1+(TipPaid/100)
TotalAmountPaidByEach = (totalBill/NoOfPeopel)*TotalTipPaid
print(f"Total Amount need to pay by each : {round(TotalAmountPaidByEach,2)}")