# Task 1

########################################################################
# Function to calculate Area and Check the area is square or not .
def calculate_area(length , width):
    if length == width :
        return "This is a square!"
    area =  length * width
    return 'The Area = ' + str(area)


# main function to call the calculate_area function 
def main():
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))
    print(calculate_area(length , width))


main()