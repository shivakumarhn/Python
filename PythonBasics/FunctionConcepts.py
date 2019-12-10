def test():
    print("Hello world")


test()


def abc(a):
    print(a + 10)


abc(10)


def getCountryName(name="india"):
    print(name)


getCountryName()
getCountryName("UK")
getCountryName(100)


# pass list into function
def getNames(lst):
    for x in lst:
        print(x)


print("---------------")

name = ["java", "python", ".Net", "C#"]
getNames(name)


# Function with return
def add(a, b):
    c = a + b
    return c


s1 = add(5, 9)
print(s1)

print("---------------")


def getCapitalName(countryName):
    if countryName == "India":
        return "New delhi"
    elif countryName == "USA":
        return "Washington DC"


print(getCapitalName("India"))
print(getCapitalName("USA"))


def launchBrowser(browserName):
    if browserName == "chrome":
        print("launch google chrome")
    elif browserName == "firefox":
        print("launch firefox")
    else:
        print("browser not defined")


launchBrowser("chrome")


print("---------------")


# Recursion function
# a function calling itself

# WAP to get factorial of given number
# fact(4) = 4*3*2*1 = 24
# fact(4) = 5*4*3*2*1 = 120

def fact(num):
    if num > 1:
        num = num * fact(num - 1)
    return num


print(fact(4))
print(fact(5))


def login(username, password):
    print("login with %s and %s " % (username, password))


print("---------------")

login("mandya219@gmail.com", "test@123")
