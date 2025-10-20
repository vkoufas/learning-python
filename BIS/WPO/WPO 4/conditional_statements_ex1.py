"""
Which Prize

Write an if statement that lets a competitor know which of these prizes they 
won based on the number of points they scored, which is stored in the integer 
variable points.

Points      Prize
1 - 50      no prize
51 - 150    candle
151 - 180   bath towel
181 - 200   bottle of wine

All of the lower and upper bounds here are inclusive, and points can only take
on positive integer values up to 200.

In your if statement, assign the result variable to a string holding the 
appropriate message based on the value of points. 
If they've won a prize, the message should state 
"Congratulations! You won a [prize name]!" with the prize name. 
If there's no prize, the message should state "Oh dear, no prize this time."
"""

points = 174

if points <=50:
    result = "Oh dear, no prize this time."
elif points <=150:
    result = "Congratulations! You won a candle!"
elif points <= 180:
    result = "Congratulations! You won a bath towel!"
elif points <=200:
    result = "Congratulations! You won a bottle of wine!"
else:
    result = "Oh dear, no prize this time."

print(result)