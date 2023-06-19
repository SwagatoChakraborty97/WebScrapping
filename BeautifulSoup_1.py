import requests
response = requests.get("https://www.google.com")
# print(response.status_code)
# print(response.text)

from bs4 import BeautifulSoup

# Syntax 
# BeautifulSoup(/*html file*/,/*predefined parser name*/)
data = BeautifulSoup(response.text,'html.parser')
print(data)
print()
print(type(data))
print()
print(data.prettify())    # prettify data
# Syntax 
# data./*tagname*/ to get desired data within tag
# NOTE - Using this syntax we get only the 1st occurence of multiple occurences(if present)
print()
print(data.title) # To get a tag
print(data.title.string) # To get string present in b/w the tags. WOrks only if only 1 child present under the tag
print(data.title.attrs) # Returns dict
print()
print(data.p)
print(data.p.string)
print(data.p.attrs) # Returns dict
print(data.p['style'])
print()
print(data.h2)  # if tag not present it return None
print()

# Another Syntax to find any tag from webpage
# Returns only 1st occurence 
# data.find('/*tagname*/')
print(data.find('title'))      # To find anything from webpage
# To find all occurences of specific tag use findall()
print()
print(data.find_all('a'))       # Returns all occurences of tag in form of a list
print()
print(data.find_all(['p','h3'])) # Returns all occurence of tag mentioned in list
print()
print(data.find_all(True))      # Return all tag in webpage
print()
print(data.find_all(id = "gbar"))      # Find by id
print()
print(data.find_all(class_ = 'ds'))      # Find by id

print()
print(data.get_text())  # To get all text in webpage  
print()

iterator = data.head.children   # returns an iterator to get all children under a tag
for i in iterator:
    print(i)

iterator = data.head.descendants   # returns an iterator to get all descendants under a tag
for i in iterator:
    print(i)
    