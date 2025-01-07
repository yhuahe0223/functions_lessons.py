# Return Practice #1
# Create a function called power that takes two numeric values as arguments. It must return the number that results from solving a power, using the first number as the base, and the second as the exponent

def power(x,y):
    z = x**y
    return z 






# Return Practice #2
# Create a function called usd_to_eur that takes a numeric value (an amount in US dollars) as its only parameter, and returns the equivalent amount in euros as a result. For the purposes of this example, we will take the conversion 1 USD = 0.90 EUR.
def usd_to_eur(x):
    z  = x*0.9
    return z 
# Create a variable called dollars and store any amount in it. Then, pass it to your function and evaluate its result.
dollars  = 30
print(usd_to_eur(dollars))
# Hint: to perform the conversion, the function internally must multiply this value in dollars by 0.90 to obtain the equivalent amount in euros.




# Return Practice #3
# Create a function called reverse_word that takes the characters of a given word as an argument, reverses the order of their characters, and returns them that way and in uppercase.
def reverse_word(word):
    z = word[::-1]
    return z.upper()
# For example, if we pass it the word "Python", it should return: "NOHTYP"
print(reverse_word('Python'))
# Also, you must create a variable called word, which contains any string, to pass it as an argument to the created function.

# Hint: inside the created function, you should use string methods already seen.