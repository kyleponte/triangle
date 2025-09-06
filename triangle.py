def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
    
    sides = sorted([a, b, c])
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if a == b and a == c:
        return 'Equilateral'
    elif a == b or a == c or b == c:
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            return 'Right Isoceles'
        else:
            return 'Isosceles'
    else:
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            return 'Right Scalene'
        else:
            return 'Scalene'