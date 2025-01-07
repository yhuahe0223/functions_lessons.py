# #functions are ways to wrap your code 
# #into reuseable units 

# #defin a function with def 
#     # only define the function once
#     #when I pass in a parameeter,
#     # I am passing in a placeholder 
#     #for future information 
# def say_hello(name,age,address):
#     print(f'Hello! {name}')
#     print(f'How are you? {name}')
#     print(f'{name} are {age} years old')
#     print(f'{name} live in {address}')

    

# #call the function
# #pass in information called an argument 
# say_hello('Alice',22,'1234 s cermark')
# say_hello('Paul',33,'1234 s cermark' )



# def determindtoGrad(name, credits, gpa, satScore):
#     if credits>= 120 and gpa >= 2.5 and satScore >=800:
#         print(f'{name} is eligiblility to graduate')
#     else:
#         print(f'{name} is not eligible to graduate ')
       


#return = statement used to end a function 
#         and send a result back to the caller 

def add(x,y):
    z = x + y
    return z 

def subtract(x,y):
    z = x - y 
    return z 

def multiply(x,y):
    z = x * 8
    return z 

def divide(x,y):
    z = x / y 
    return z

print(add(1,2))
print(subtract(3,2))
print(multiply(3,1))
print(divide(4,2))