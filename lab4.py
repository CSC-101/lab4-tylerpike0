import data

# Write your functions for each part in the space below.

# Part 1

# takes in a list of lists of ints, and then returns a list made of the first element of each of the inputed lists
def first_element(lists : list[list[int]]) ->list[int]:
    returnList = []
    for listI in lists:
        returnList.append(listI[0])
    return returnList



# Part 2
from data import Point

# takes in a list of points, and then returns a list of the x-coordinates
def x_coordinates(points: list[Point]) -> list[float]:
    x_coordinates = []
    for point in points:
        x_coordinates.append(point.x)
    return x_coordinates

# Part 3

# Takes in a list of points and returns a list of those points that are in upper right quadrant
def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    points_in_positive_quadrant = []
    for point in points:
        if point.x > 0 and point.y > 0:
            points_in_positive_quadrant.append(point)
    return points_in_positive_quadrant

# Part 4

# takes in two points and returns the float distance between them
def distance (point1 : Point, point2: Point) -> float:
    x_distance = point1.x - point2.x
    y_distance = point1.y - point2.y
    squared_distance = x_distance * x_distance + y_distance * y_distance
    return pow(squared_distance, 0.5)

# Part 5

# takes in two points and returns the manhattan distance between them
def manhattan_distance(point1 : Point, point2: Point) -> float:
    x_distance = point1.x - point2.x
    y_distance = point1.y - point2.y
    return abs(x_distance) + abs(y_distance)

# Part 6

# takes in a list of points, and returns a list of floats that correspond ot the distance that each point is form the origin (0,0)
def distance_all(points: list[Point]) -> list[float]:
    distances = []
    for point in points:
        distances.append(distance(Point(0,0),point))

    return distances

