import requests
import json
from bs4 import BeautifulSoup
  
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 'Accept':"application/json"}

bookLangBtk = '5663693268320256'
bookLangInd = '6260074016145408'
bookIds = [
    'f4392984-7a08-49e5-a4a4-56816f565d51',
    '7c4652a5-1b86-4af4-adff-ea82ace515af',
    # '2b226676-d3ca-41eb-860c-7fc44222751e',
    # 'e4d01e0e-71c1-4d6a-b341-8bad028d0e7e',
    # '7eb22438-84e9-4242-b86e-5ca5c6de3673',
    # '841c89ef-b760-4df7-a46b-690fee90a3bc',
    # '6826ae9d-b851-45c4-a93d-009a83101788',
    # '2c5a7fee-76f5-4b16-95bf-19c261dce242',
    # 'd40939ca-2c21-4145-8c72-d23365a21774',
    # '7964ad44-55de-4e5f-9fea-deafcb916c9a',
    # '58df69c5-1c1e-4575-b48e-3867e11c2054',
    # '9ca2ada4-2456-467e-8229-d3f00cdf27fd',
    # 'c7d00a36-0880-4c70-8c0f-b8111a43bbb7',
    # '6c7caaa6-e667-476f-a5b6-508c7219d0b5',
    # 'f1761a23-07a8-4490-b165-c1705489d3bc',
    # 'bf1cb4d7-55dc-44ae-9941-a68548f1c0c7',
    # 'd220da2d-f80e-4ee3-8e32-57abf8a40cd0',
]
# https://letsreadasia.org/api/v5/book/preview/language/5663693268320256/book/203e8d02-7768-4b16-8892-ff87ab2501d5

bookContents = []
for bookId in bookIds:
    URL = "https://letsreadasia.org/api/v5/book/preview/language/"+bookLangInd+"/book/" + bookId
    # URL = "https://letsreadasia.org/api/v5/book/preview/language/5663693268320256/book/203e8d02-7768-4b16-8892-ff87ab2501d5"
    # print(URL)
#     URL_indo = "https://letsreadasia.org/api/v5/book/preview/language/"+bookLangInd+"/book/"+id
    r_batak = requests.get(url=URL, headers=headers)
#     r_indo = requests.get(url=URL_indo, headers=headers)
    data_batak = json.loads(r_batak.content)
#     data_indo = json.loads(r_indo.content)
    print(URL)
    print(data_batak)
    # bookContents.append(data_batak['masterBookMetaData']['title']+'~'+data_indo['masterBookMetaData']['title'])
#     bookContents.extend([BeautifulSoup(x['extractedLongContentValue'].rstrip('\n'), 'html.parser').get_text()+ '~'+ BeautifulSoup(y['extractedLongContentValue'].rstrip('\n'), 'html.parser').get_text()  for x, y in zip(data_batak['pages'], data_indo['pages'])])

# for x in bookContents:
#     print(x)
