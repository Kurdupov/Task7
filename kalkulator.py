def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y

print("1.Додавання")
print("2.Віднімання")
print("3.Множення")
print("4.Ділення")

dija = input("Виберіть дію(1/2/3/4): ")

num1 = float(input("Введіть перше число : "))
num2 = float(input("Ведіть друге число : "))

if dija == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif dija == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif dija == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif dija == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")