def unitconverter():
    print("welcome to unit converter")
    print("1. convert length (m to kilometers),(kilometers to m)")
    print("2. convert weight(gr to kg ),(kg to gr)")
    print("3. convert temperature(C to F),(F to C)")
    choice = input("enter your choice (1/2/3): ").strip()
    if  choice == "1":
    unit_type = input("enter m to km or km to m: ").strip().lower()
    value = float(input("enter the value to convert: "))
    if unit_type == "m to km":
        print(f"{value} meters ={value /1000} kilometers")
    elif unit_type == "km to m":
        print(f"{value} kilometers ={value *1000} meters")
    else:
        print("invalid unit type for length conversion")
    elif choice == "2":
    unit_type = input("enter gr to kg or kg to gr: ").strip().lower()
    value = float(input("enter the value to convert: "))
    if unit_type == "gr to kg":
        print(f"{value} grams ={value /1000} kilograms")
    elif unit_type == "kg to gr":
        print(f"{value} kilograms ={value *1000} grams")
    else:
        print("invalid unit type for weight conversion")
    elif choice == "3":
    unit_type = input("enter C to F or F to C: ").strip().upper()
    value = float(input("enter the value to convert: "))
    if unit_type == "C to F":
        print(f"{value} Celsius ={(value *9/5) +32} Fahrenheit")
    elif unit_type == "F to C":
        print(f"{value} Fahrenheit ={(value -32) *5/9} Celsius")
    else:
        print("invalid unit type for temperature conversion")