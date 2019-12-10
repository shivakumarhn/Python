name = "Alexander"
for i in name:
    print(i)
    if i == 'x':
        break

print("----------")

name = "Alexander"
for i in name:
    print(i)
    if i == 'x':
        continue

print("----------")

lang = ["java", "python", ".net", "c#"]
for l in range(len(lang)):
    print(lang[l])
    if lang[l] == "python":
        print("Found python!!!")
        break

print("----------")

lan = ["kannada", "hindi", "english", "spanish"]
flag = False
for l in range(len(lan)):
    print(lan[l])
    if lan[l] == "english":
        print("English is global lang")
        flag = True
        break

print("----------")

if flag:
    print("I want to master english")


