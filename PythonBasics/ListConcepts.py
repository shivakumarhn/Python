score = [10,20,6,90,60]

print(score)
print(score[0])
print(score[4])
print(score[-1])
print(score[-5])

'#new/shallow copy of list'
print(score[:])

print(score + [13,93,54])
print(score + ["A","N","z"])

number =[1,2,3,4,5]
number[2] = 90
print(number)

'#append'
number.append(100)
print(number)

number.append(7**3)
print(number)

name = ['a','b','c','d','e','f']
print(name)
name[2:5]=['C','D','E']
print(name)
name[2:5] = []
print(name)

name[:] = []
print(name)
name.append([1,2,3])
print(name)

test = [20,30,40,50]
print(len(test))

a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[1])

print(x[0][1])
print(x[1][2])







