student_height = input("Input a list of student height ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
# Not using any functions from python
TotalHieght = 0
Count =0
for CountOfStdHeight in student_height:
  TotalHieght += CountOfStdHeight 
  Count +=1
print(TotalHieght)
print(Count)
AverageHeight = TotalHieght/Count
print(f"Average Height is {round(AverageHeight)}")

#Using Python Functions
TotalNoStudent = len(student_height)
TotalHeightOfSTudents = sum(student_height)
print(TotalNoStudent)
print(TotalHeightOfSTudents)