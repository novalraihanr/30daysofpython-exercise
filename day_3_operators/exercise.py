# my_age = 22
# my_height = 169.0
# complex_number = 2 + 2j
#
# base = input("Enter base: ")
# height = input("Enter height: ")
# area_triangle = 0.5 * int(base) * int(height)
# print("The area of the triangle is ", area_triangle)
#
# side_a = input("Enter side a: ")
# side_b = input("Enter side b: ")
# side_c = input("Enter side c: ")
# perimeter = side_a + side_b + side_c
# print("The perimeter of the triangle is ", perimeter)
#
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# area = length * width
# perimeter = 2 * (length + width)
# print("Rectangle area: ", area)
# print("Rectangle perimeter: ", perimeter)
#
# radius = float(input("Enter radius: "))
# area = 3.14 * radius ** 2
# circumference = 2 * 3.14 * radius
# print("Area of circle: ", area)
# print("Circumference of circle: ", circumference)
#
# slope1 = 2
# x = 0
# y = 0
# x_intercept = 0 + 2 / 2
# y_intercept = 2 * 0 - 2
# print("The Slope is ", slope1)
# print("The X Intercepet is ", x_intercept)
# print("The Y Intercept is ", y_intercept)
#
# x1 = 2
# y1 = 2
# x2 = 6
# y2 = 10
# slope2 = (y2 - y1) / (x2 - x1)
# euclidean_distance = ((2 - 2) ** 2 + (6 - 10) ** 2) ** 0.5
# print("Slope is ", slope2)
# print("Euclidean Distance is ", euclidean_distance)
#
# compare_slope = slope1 == slope2
# print("Slope 1 and Slope 2 is ", compare_slope)
#
# x_value = (-6 + (6 ** 2 - 4 * 1 * 9) ** 0.5) / ( 2 * 1 )
# print("The x value for y = 0 is ", x_value)
#
length_python = len("python")
length_dragon = len("dragon")
print("Is python and dragon the same length? ", length_dragon == length_python)

is_on = "on" in "python" and "on" in "dragon"
print("is on in python and dragon? ", is_on)

is_jargon = "jargon" in "I hope this course is not full of jargon"
print("is jargon in I hope this course is not full of jargon?", is_jargon)

is_on_not = "on" not in "python" and "on" not in "dragon"
print("is on not in python and dragon?")

float_length_python = float(length_dragon)
string_length_python = str(float_length_python)
print("float of the length of python is ", float_length_python)
print("string of the length of python is ", string_length_python)

num = 2
even_or_not = num % 2 == 0
print("Is the num even or not? ", even_or_not)

check = 7 // 3 == int(2.7)
print("Is 7 floor divided by 3 the same as int converted 2.7? ", check)

check2 = type('10') == type(10)
print("is the type of '10' the same as the type of 10? ", check2)

check3 = int(float('9.8')) == 10
print("Is int('9.8') os the same as 10? ", check3)

hours = input("Enter hours: ")
rate_per_hour = input("Enter rate per hour: ")
weekly_earning = int( hours ) * int(rate_per_hour)
print("Your weekly earning is ", weekly_earning)

years_you_lived = input("Enter number of years you have lived: ")
years_to_second = int(years_you_lived) * 31556952
print("You have lived for ", years_to_second, " seconds")

a = 1
b = 2
c = 3
d = 4
e = 5

print(a, " ", a ** 0, " ", a ** 1, " ", a ** 2, " ", a ** 3)
print(b, " ", b ** 0, " ", b ** 1, " ", b ** 2, " ", b ** 3)
print(c, " ", c ** 0, " ", c ** 1, " ", c ** 2, " ", c ** 3)
print(d, " ", d ** 0, " ", d ** 1, " ", d ** 2, " ", d ** 3)
print(e, " ", e ** 0, " ", e ** 1, " ", e ** 2, " ", e ** 3)


