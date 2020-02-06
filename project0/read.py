file = open("fruits.txt", "r")
content = file.readlines()
file.close()
for i in content:
     print(len(i.strip()))

numbers = [1, 2, 3]
file = open("numbers.txt", "w")
for i in numbers:
    file.write(str(i) + "\n")
file.close()
