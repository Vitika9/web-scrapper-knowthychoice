import requests
import json
from bs4 import BeautifulSoup

# Making a GET request to the main URL
request = requests.get('https://knowthychoice.in/blog/')

# Parsing the HTML
soup = BeautifulSoup(request.content, 'html.parser')

# Finding all blog post contents
blog_post_contents = soup.find_all('div', class_ = 'blog-post-content')

# Creating a dictionary to store data
data = dict({})

# Iterating blog_post_content to fetch and store it's data
for blog_post_content in blog_post_contents:
    # Getting anchor element which contains heading and url of blog page
    anchor = blog_post_content.find('a')
    heading = anchor.text
    url = anchor.get('href')

    # Using the new url to create new BeautifulSoup object
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    # Getting all lists of the blog page
    lists = soup.find_all('ul')

    concepts_covered_list = []

    # Iterating the concepts covered list which is at index 5 and storing the list item text in our concepts_covered_list
    for list_item in lists[5]:
        if list_item.text == '\n':
            continue
        concepts_covered_list.append(list_item.text)

    # Adding new element in our data dictionary with heading as key and concepts_covered_list as value
    data[heading] = concepts_covered_list

# Converting dictionary to JSON and printing it
print(json.dumps(data, indent = 1))
