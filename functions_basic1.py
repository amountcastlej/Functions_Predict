#1
# I predict the outcome to be 5
def a():
    return 5
print(a())
# Answer is 5

#2
# I predict the outcome to be 10
def a():
    return 5
print(a()+a())
# Answer is 10

#3
# I predict the outcome to be 5
def a():
    return 5
    return 10
print(a())
# Answer is 5

#4
# I predict the outcome to be 5
def a():
    return 5
    print(10)
print(a())
# Answer is 5

#5
# I predict the outcome to be 5
def a():
    print(5)
x = a()
print(x)
# Answer is 5 & None

#6
# I predict the result to give an error
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# Error occurred 

#7
# I predict the result to be 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Answer is 25

#8
# I predict the result to be 100 & 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Answer is 100 & 10

#9
# I predict the result to be 7, 14, 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Answer is 7, 14, 21

#10
# I predict the result to be 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Answer is 8

#11
# I predict the result to be 500, 500, 300, 300
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# Answer is 500, 500, 300, 500

#12
# I predict the result to be 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# Answer is 500, 500, 300, 500

#13
# I predict the result to be 500, 500, 300, 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# Answer is 500, 500, 300, 300

#14
# I predicted the result to be 1, 3, 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#Answer is 1, 3, 2

#15
# I predicted the result to be 1, 3, 5, 10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# Answer is 1, 3, 5, 10