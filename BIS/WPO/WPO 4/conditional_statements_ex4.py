"""
Correct or improve these conditional statements.
"""

#the staments below should print "The weather is cold!" if we store (i) either a string of text that is not empty or (ii) an integer that is not zero (0) in the variable is_cold.
#the way it is currently written, the statements will only print "The weather is cold!" if we store a Boolean value (or the integer "1") in is_cold
#thus, we need to correct this statement 
is_cold = "a"
if is_cold:
    print("The weather is cold!")

#the statements below should return "Wear boots!" if the variable weather stores (i) "snow" or (ii) "rain".
#the way it is currently written, the statements will print "Wear boots!" if (i) the variable weather stores "snow" or (ii) if the string of text "rain" converted to a Boolean value is True or False.
#thus, we need to correct this statement 
weather = "sun"
if weather == "snow" or weather== "rain":
    print("Wear boots!")