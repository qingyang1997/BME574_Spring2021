def interface():
    print("")

    while (True):
        print("\nOptions:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter an option:")
        if (choice == "9"):
            return
        elif (choice == "1"):
            HDL_driver()

def get_input():
    data = input("Enter the HDL Level:")
    return int(data)

def analyze_data(data):
    if (data >= 60):
        return "Normal"
    elif (data >= 40):
        return "Borderline Low"
    else:
        return "Low"

def output_res(data, res):
    print("The HDL entered was {}" .format(data))
    print(res)
    
def HDL_driver():
    # Get input data
    data = get_input()

    # Analyze data
    res = analyze_data(data)
    
    # Output data
    output_res(data,res)

interface()
