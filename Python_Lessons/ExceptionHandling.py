value_1 = float(input("Please enter an integer:"))
value_2 = float(input("Please enter an integer:"))

try:
    float(value_1)//float(value_2)
except:
    print("Please Enter two non zero integers")
else:
    print(value_1//int(value_2))