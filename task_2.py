inp = input("enter add or subtract or multiply or divide:")
result_for_add = 0
result_for_subtract = 0
result_for_multiply = 1
result_for_divide = 1
string = "10", "5"
for num in string:
    intgr = int(num)
    if inp == "add":
        result_for_add += intgr
        print(result_for_add)
    elif inp == "subtract":
        result_for_subtract -= intgr
        print(result_for_subtract)
    elif inp == "multiply":
        result_for_multiply *= intgr
        print(result_for_multiply)
    elif inp == "divide":
        result_for_divide /= intgr
        print(result_for_divide)
    else:
        print("it isn't maths")

