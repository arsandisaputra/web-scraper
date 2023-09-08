import requests
import json
from bs4 import BeautifulSoup
  
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 'Accept':"application/json"}

cursors = ['', '1', '2']
URL = "https://letsreadasia.org/api/book/elastic/search/?searchText=&lId=5663693268320256&countryOfOrigin=&audio=false&activity=false&altImage=false&limit=20&cursor="

books = {}
for c in cursors:
    r_list_books = requests.get(url=URL+''+c, headers=headers)
    data_books = json.loads(r_list_books.content)

    for o in data_books['other']:
        books[o['name']] = o['id']
        # print(o['id']+' '+o['name'])
sorted_books = dict(sorted(books.items()))
# print(sorted_books)
for key, value in sorted_books.items():
    print(value +' '+ key)