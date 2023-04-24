import csv
import copy

#Hello, world
print("Hello, World")
print("Python has three numeric types: int, float, and complex")
#Tipos de dados
myValue = 1 
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

print("seu nome é {}!" .format(name))

#Listas e Tuplas
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]


for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    




myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))