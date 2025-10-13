"""
Which is denser, Rio or San Francisco?

Try comparison operators in this quiz! This code calculates the population densities of Rio de Janeiro and San Francisco.

Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.
"""

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

print("San Francisco Population Density: ", san_francisco_pop_density)
print("Rio Population Density: ", rio_de_janeiro_pop_density)

print("Is the population of San Francisco more dense than that of Rio de Janeiro?")
print("Answer is: ") # How do I put the answer in the same line?

if san_francisco_pop_density > rio_de_janeiro_pop_density:
    print(True)
else:
    print(False)

