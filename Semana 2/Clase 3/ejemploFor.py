
# listaCombinada = ["Daniel",234,-30,True,"Hola",["soy un elemento dentro de otra lista"]]
names = ["Daniel","Jose","Miguel","Ana","Carolina"]
for element in names:
    print(element)


# listOfNumbers = [10, 50, -5, 20, -30.4]

# for number in listOfNumbers:
#     if number > 15:
#         print(number)


list3 = ["hola","hoy",345,89]
print(list3[3])

for index,element in enumerate(list3):
    print(index, element)


matrix = [[1,2,3],[3,4,5],[6,7,8]]

for row in matrix:
    print(row)
    for element in row:
        print(element)
