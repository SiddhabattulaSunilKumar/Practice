student_height = input("Input a list of student height ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
#Python functions
MaxHeight = max(student_height)
print(MaxHeight)

#Without using python function
ReturnMaxHeight = 0
MaxHeightOutput = 0
for Mxheight in student_height:
  if Mxheight>ReturnMaxHeight:
    MaxHeightOutput = Mxheight
  else:
    MaxHeightOutput = ReturnMaxHeight
  ReturnMaxHeight = Mxheight
print(f"Max height is {MaxHeightOutput}")
