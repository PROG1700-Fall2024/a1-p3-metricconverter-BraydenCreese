#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.


"""
Had lost of trouble with the math here and gave it my best shot, I understand the programming but I suck at math

"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # setting our starting vars to 0 for clean numbers
    tons =      0
    stone =     0
    pounds =   0
    ounces =    0

    # getting user input for all values as a float (Ex: 1.1). Also setting up error handling to stop user from not using numbers as inputs
    while True:
        try:
            tons = float(input("Enter the number of tons: "))
            break
        except ValueError:
            print("Invlid input. Please enter a valid number for 'number of tons'.")

    while True:
        try:
            stone = float(input("Enter the number of stone: "))
            break
        except ValueError:
            print("Invlid input. Please enter a valid number for 'number of stone'.")


    while True:
        try:
            pounds = float(input("Enter the number of pounds: "))
            break
        except ValueError:
            print("Invlid input. Please enter a valid number for 'number of pounds'.")

    while True:
        try:
            ounces = float(input("Enter the number of ounces: "))
            break
        except ValueError:
            print("Invlid input. Please enter a valid number for 'number of ounces'.")

    # calcs for metric tons
    totalOunces = 35840 * tons + 224 * stone + 16 * pounds + ounces  # Convert all vars to total ounces
    totalKilos = totalOunces / 35.274  # Convert total ounces to total kilograms
    metricTons = int(totalKilos / 1000)  # Calculate metric tons (set to int as this is better as whole number)

    # print results out to user
    print(f"The metric weight is {metricTons} metric tons, {totalKilos:.2f} kilos, and {totalOunces:.2f} grams.")

    # YOUR CODE ENDS HERE

main()