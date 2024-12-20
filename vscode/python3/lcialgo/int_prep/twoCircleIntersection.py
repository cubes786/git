import math

def circle_relationship(circle1, circle2):
    # Extract center points and radii
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    
    # Calculate the distance between the two centers
    distance_centers = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Determine the relationship based on the distance and radii
    if distance_centers > r1 + r2:
        return "The circles do not intersect"
    elif distance_centers == r1 + r2:
        return "The circles touch at exactly one point (externally tangent)"
    elif distance_centers < abs(r1 - r2):
        return "One circle is completely inside the other"
    elif distance_centers == abs(r1 - r2):
        return "The circles touch at exactly one point (internally tangent)"
    else:
        return "The circles overlap partially"
    
# Example usage
circle1 = (0, 0, 5)  # Center (0, 0), Radius 5
circle2 = (8, 0, 3)  # Center (8, 0), Radius 3

result = circle_relationship(circle1, circle2)
print(result)
