#syntax
print("Hellow World")

if 5>2:
    print("YES")

#Comments
    #This is a comment
    """This is a comment
    Written in
    more than just one line"""

#variables
    #1
carname = 'Volvo'
    #2
x = 50
    #3
x = 5
y = 10
print(x + y)
    #4
x = 5
y = 10
z = x + y
print(z)
    #5
x, y, z = "Orange", "Banana", "Cherry"
    #6
x = y = z = "Orange"
    #7
def myfunc():
    global x
    x = 'fantastic'


#data types
    #1
x = 5
print(type(x)) #int
    #2
x = "Hello World"
print(type(x)) # str
    #3
x = 20.5
print(type(x)) #float
    #4
x = ["apple", "banana", "cherry"]
print(type(x)) #list
    #5
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
    #6
x = {"name" : "John", "age" : 36}
print(type(x)) #dict
    #7
x = True
print(type(x)) #bool
