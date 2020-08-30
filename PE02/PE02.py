# In this exercise, you are expected to calculate the perimeter and the area of a triangle.
# You are required to read contents in the file named ‘input_pe02.txt’. 
# It will contain four lines. The first one is a Boolean variable, 
# and the rest of the lines correspond to three cartesian coordinates. 
# A sample file may contain the following values.

# True
# 1, 2
# 3, -2
# 2, -0.5

# If the Boolean variable is True, 
# you need to calculate the perimeter of a triangle formed by three subsequent coordinates. 
# If the value is False, you need to calculate the area of the triangle. 
# If the coordinate does not form a triangle, make sure you generate an error message.

# In this example, the Boolean variable is True. 
# Therefore, you need to generate the perimeter of a triangle formed by three coordinates – 
# (1,2), (3, -2), and (2, -0.5). The perimeter value in this case becomes 8.967 units (no rounding required). 
# In this case, your code needs to generate the following output:

# Perimeter of the triangle: 8.967

# On the other hand, if the Boolean variable is False, the sample answer becomes 0.5. 
# In this case, the following output needs to be generated.

# Area of the triangle: 0.5

# To calculate the distance, use the Euclidean distance between two coordinates. 
# For example, the distance between (x1, y1) and (x2, y2) should be ((x1-x2)**2 + (y1-y2)**2)**0.5.

# Also, you can use the following formula to calculate the area of a triangle formed by three distinct coordinates 
# (x1, y1), (x2, y2), and (x3, y3).

# Area = |x1*y2 + x2*y3 + x3*y1 – x1*y3 – x2*y1 – x3*y2| / 2

# Here, | | in the area formula is an absolute value function. 
# That is, |x| = x for any non-negative number x and |x| = -x for a negative number x. 
# For example, |3| = 3 and |-3| = 3.



#function to calculate the area of the triangle
def area(x1,y1,x2,y2,x3,y3):
    result = abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)/ 2 #abs function to avoid negative values
    return result

#function to calculate the sides and parimeter of the triangle
def perimeter(x1,y1,x2,y2,x3,y3):
    side1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
    side2 = ((x2-x3)**2 + (y2-y3)**2)**0.5
    side3 = ((x3-x1)**2 + (y3-y1)**2)**0.5
    result = side1 + side2 + side3
    return result

#open and read line by line of the "input_pe02.txt" file 
with open("input_pe02.txt", "r") as file:
  for line in file:
    stripped_line = line.strip()
    #if the boolean value is False, then extract each number from next lines and assign to each coordinates x1,y1,x2,y2,x3,y3 one by one
    if "False" in stripped_line: 
        line = file.readline()
        x1,y1 = line.split(",")
        line = file.readline()
        x2,y2 = line.split(",")
        line = file.readline()
        x3,y3 = line.split(",")
        #pass the values of the coordinates to function "area" and print the result on console
        print(area(float(x1),float(y1),float(x2),float(y2),float(x3),float(y3)))
    else: 
    #if the boolean value is not False, 
    # then still extract each number from next lines and assign to each coordinates x1,y1,x2,y2,x3,y3 one by one
        line = file.readline()
        x1,y1 = line.split(",")
        line = file.readline()
        x2,y2 = line.split(",")
        line = file.readline()
        x3,y3 = line.split(",")
        #pass the values of the coordinates to function "perimeter" and print the result on console
        print(perimeter(float(x1),float(y1),float(x2),float(y2),float(x3),float(y3)))