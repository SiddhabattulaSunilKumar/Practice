print("Row column cross")
Row1 = ["⚀","⚀","⚀"]
Row2 = ["⚀","⚀","⚀"]
Row3 = ["⚀","⚀","⚀"]
print(f"{Row1}\n{Row2}\n{Row3}")
Your_Input = input("Please enter the row and column you want to move (Row,Column) : ")
Combined_Row = [Row1,Row2,Row3]
Split_Input = Your_Input.split(",")
Combined_Row[int(Split_Input[1])-1][int(Split_Input[0])-1]="X"
Combined_Row_Output = f"{Combined_Row[0]}\n{Combined_Row[1]}\n{Combined_Row[2]}"
#Combined_Row[1,1] = "X"
