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
   
    


    
