"""Triangle classifier: returns a string label given three side lengths."""
def classify_triangle(a, b, c):
    """Return a label such as 'Equilateral', 'Isosceles', 'Right Scalene', or 'Not a triangle'."""
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'

    sides = sorted([a, b, c])
    a = sides[0]
    b = sides[1]
    c = sides[2]
    tolerance = 1e-9

    if a == b and a == c:
        return 'Equilateral'
    if a == b or a == c or b == c:
        if abs((pow(a, 2) + pow(b, 2) - pow(c, 2)) - 0) <= tolerance:
            return 'Right Isosceles'
        return 'Isosceles'
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        return 'Right Scalene'
    return 'Scalene'
