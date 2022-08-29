
import re


example_sep = 'https://www.google.com, https://www.facebook.com'

cleanString = re.sub(',',' ', example_sep )

new_list = cleanString.split()

for i in new_list:
    print(i)