"""
Write a Server Log Message

You'll be provided with example data for a user, the time of their visit and 
the site they accessed. You should use the variables provided and the 
techniques you've learned to print a log message like this one (with the 
username, url, and timestamp replaced with values from the appropriate 
variables):
John.McAfee accessed the site https://canvas.vub.be/courses/234097 at 12:53.
"""

username = "Elizabeth.Smith"
timestamp = "09:11"
url = "https://canvas.vub.be/courses/189241"

# TODO: print a log message using the variables above.

print(username + " accessed the site " + url + " at " + timestamp)