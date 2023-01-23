#Area calc
#Variables
height = 0 
width = 0
area = 0

#function for calculating the area
def area_calc ():
    height = int(input("Please enter the height of the square: "));
    width = int(input("Please enter the width of the square: "));
    area = (height * width);
    return area;

#calling the function
area = area_calc();

#Print area
print("The area of the square is:", area);