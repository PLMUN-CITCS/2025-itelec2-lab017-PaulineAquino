import math

def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

# Define the radius
radius_value = 5

# Call the function and store the result
area_result = circle_area(radius_value)

# Print the result formatted to two decimal places
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
