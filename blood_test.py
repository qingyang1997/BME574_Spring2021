def interface():
    print("")

    while (True):
        print("\nOptions:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter an option:")
        if (choice == "9"):
            return
        elif (choice == "1"):
            HDL_driver()
        elif (choice == "2"):
            LDL_driver()

def get_HDL_input():
    data = input("Enter the HDL Level:")
    return int(data)

def analyze_HDL_data(data):
    if (data >= 60):
        return "Normal"
    elif (data >= 40):
        return "Borderline Low"
    else:
        return "Low"

def output_HDL_res(data, res):
    print("The HDL entered was {}" .format(data))
    print(res)

def get_LDL_input():
    data = input("Enter the LDL Level:")
    return int(data)

def analyze_LDL_data(data):
    if (data < 130):
        return "Normal"
    elif (data <= 159):
        return "Borderline High"
    elif (data <= 189):
        return "High"
    else:
        return "Very High"

def output_LDL_res(data, res):
    print("The LDL entered was {}" .format(data))
    print(res)

def HDL_driver():
    # Get input data
    data = get_HDL_input()

    # Analyze data
    res = analyze_HDL_data(data)
    
    # Output data
    output_HDL_res(data,res)

def LDL_driver():
    # Get input data                                                           
    data = get_LDL_input()

    # Analyze data
    res = analyze_LDL_data(data)
    
    # Output data
    output_LDL_res(data,res)
    
interface()
