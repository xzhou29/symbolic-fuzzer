def is_divisible_by_3_5(num: int, num2: int):
    
    if num % 3 == 0:
        if num % 5 == 0:
            return True
        else:
            return False
    return False

def check_triangle(a: int, b: int, c: int):
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"



def check_triangle2(a: int, b: int, c: int):
    a = 7
    b = 2
    if not is_divisible_by_3_5(a, b):
        return "Failed"
    b = c
    if not is_divisible_by_3_5(b, c):
        return "Failed"
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"


def check_triangle3(a: int, b: int, c: int):
    a = 3
    if not is_divisible_by_3_5(a, c):
        return "Failed"
    a = 4
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"