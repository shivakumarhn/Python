def login(username, password):
    print(username, password)


login("shiva", "test123")
login(username="test123", password="shiva")


# *args
def getMarks(*arg):
    for x in arg:
        print(x)


getMarks(10, 20, 30, 40)
getMarks("A", "B+", "C", "D+")


# keyword args:
# **args

def getStudentMarks(**args):
    for key, value in args.items():
        print("%s == %s" % (key, value))


getStudentMarks(Tom=100, John=40, Ram=82, Ann=59)
getStudentMarks(kay="apple", SellerName="Steve")

# Lambda functions: Anonymous function
# A function with no name

cube = lambda x: x * x * x
print(cube(4))

total = lambda marks: marks + 300
print(total(300))

