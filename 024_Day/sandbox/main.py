with open('test.txt') as file:
    print(file.read())


with open('test.txt',mode='a') as file:
    file.write("\nHere is some new text :)")