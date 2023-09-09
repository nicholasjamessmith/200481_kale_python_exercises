"""
# 1. Using the print method, print "Hello World"
print("Hello World")
# 2. Create variables for the data type below. 
# Data Types:
# Int
intvar = 2
# Float
floatvar = 2.2
# String
stringvar = "This is a string"
# Boolean 
booleanvar = False
# Boolean (The other boolean value)
booleanvarother = True
# Lists ( 4 items in list min.)
listvar = [0, 1, 2, 3]
# Dictionaries  ( 4 key/value pairs min.)
"""
dictionaryvar = {
  "a": 1,
  "b": 2,
  "c": 3,
  "d": 4,
}
"""
# 3. For each of the variables, use the print method for each variable. To print each varible
print(intvar)
print(floatvar)
print(stringvar)
print(booleanvar)
print(listvar)
print(dictionaryvar)

# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
print(f"int: {intvar}, string {stringvar}")
"""
# 5. Comment out all print statements up to this point

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
for x in range (5):
  print("David Rocks")
# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 
def print_string():
  print("Alex Rocks")
print_string()

# 8. Declare a function that takes in 2 parameters.
def func_params(first, second): 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
  print(first + " and " + second + " Rocks")
# Now call that function using "Kyle" and "Winston" as the arguments

func_params("Kyle", "Winston")

# invoke that function 4 more times
func_params("Geologists", "Bands")
func_params("Awesome", "Stuff")
func_params("Vacation", "Time")
func_params("Other", "Thing")

# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
listvar = [0, 1, 2, 3]
# print(listvar[3])
# b. Now print the index at 100. Does this error? comment it out
# print(listvar[100]) / IndexError: list index out of range
# e. Now print the index at -1 index. Observe what it prints. Then comment it out
# print(listvar[-1]) # prints -3 (as if the list were a circle and it was rotating back 1)
# f. Now print the index at -100.  Does this error? comment it out
# print(listvar[-100]) # IndexError: list index out of range

# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2. 
for x in listvar:
 print(x)
# The staring number MUST be a negative number. The ending number MUST be postive number
listvar.insert(0, -1)
print(listvar)

# Looking to get each item printed once in order and then a second time in order
listvar.append(-2)
print(listvar)
listvar.sort()
print(listvar)

# 11. Write a WHILE LOOP in python that does the same thing as 10. 
"""
i = 1
while i <= len(listvar):
  print(i)
  i += 1
"""
counter = 0
while(counter < 1):
  print(listvar)
  counter += 1
# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.
 #######

# Hint: type this into google "loop python"

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
for x in dictionaryvar.values():
  print(x)
# Print each key
for x in dictionaryvar:
  print(x)

# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"
for x in dictionaryvar.values():
  print(x)