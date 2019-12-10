x = int(input("please enter the value of x"))

if x < 0:
    print("x is negative number")
elif x > 0:
    print("x is positive number")
elif x == 0:
    print("x is equals to zero")
else:
    print("Not defined")

if True:
    print("PASS")
else:  # dead code
    print("FAIL")

a = 100
b = 200
c = 300

if a > b and a > c:
    print("a is largest number")
elif b > c:
    print("b is largest number")
else:
    print("c is largest number")

total = int(input("enter the total value"))
if total < 100:
    total = total + 20
elif 100 <= total <= 500:
    total = total + 50
else:
    total = total + 100

print(total)
print("total=" + str(total))
print(f'{"total value is "}{total}')
