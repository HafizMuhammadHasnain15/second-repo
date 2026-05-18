# whilres operator
print(name:=input("enter your name"))

# simple input 
name=input("enter your name : ")
print(name)

while True:
    enter=input("if intersted to start again print enter otherwise print no ")
    number1=int(input("enter the first value : "))
    number2=int(input("enter the second  value : "))
    print(f"the addition of {number1} + {number2} is  {number1+number2}")
    print(f"the subtraction of {number1} - {number2} is  {number1-number2}")
    print(f"the multiplication of {number1} * {number2} is  {number1*number2}")
    if enter=="no":
        break
