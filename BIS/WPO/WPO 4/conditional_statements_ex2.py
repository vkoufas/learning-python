"""
Fill in the conditionals below to inform the user about how
their guess compares to the answer.
"""

answer = 35
guess = int(input("Guess: "))

if guess < answer:
    result = "Oops! Your guess was too low."
elif guess > answer:
    result = "Oops! Your guess was too high."
elif guess == answer:
    result = "Nice! Your guess matched the answer!"

print(result)