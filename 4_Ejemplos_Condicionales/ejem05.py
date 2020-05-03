# operadores logicos y relacionales
a = True
b = False
print("a = " + repr(a))
print("b = " + repr(b))
print("a and b = " + repr(a and b))
print("a or b = " + repr(a or b))
print("not a = " + repr(not a))
print("a or (6 > 10) = " + repr(a or (6 > 10)))
print("((4 <= 4) or false) and (!a) = " + repr(((4 <= 4) or false) and (not a)))
