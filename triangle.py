def classify_triangle(a, b, c):
    if a == b and a == c:
        return 'The triangle is equilateral'
    elif a == b or a == c or b == c:
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            return 'The right triangle is isosceles'
        return 'The triangle is isosceles'
    else:
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            return 'The right triangle is scalene'
        return 'The triangle is scalene'
    
print(classify_triangle(3, 4, 5))