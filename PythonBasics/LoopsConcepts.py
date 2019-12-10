# while loop
count = 0
while count < 4:
    # print("Hello world")
    print(count)
    count = count + 1

print("-----------------")

num = 0
while num < 4:
    print("Hello python")
    num = num + 1
else:
    print("Bye python")

print("------------------")

# for loop
name = ["java", "python", ".net", "c#"]
for i in name:
    print(i)

print("-------------")

a = "I love india"
for i in a:
    print(i)

print("-------------")

lst = ["india", "mandya", "hagadur"]
for index in range(len(lst)):
    print(lst[index])

print("-------------")

# for loop with else
countryList = ["india", "US", "UK", "German"]
for index in range(len(countryList)):
    print(countryList[index])
else:
    print("countryList is over")

print("-------------")

cityList = ["Banglore", "NY", "Delhi", "Berlin"]
for index in range(2):
    print(cityList[index])
else:
    print("City list is over")

print("-------------")

# nested for loop
for i in range(1, 5):
    for j in range(i):
        print("*", end='')
    print()
