import requests
import json
from bs4 import BeautifulSoup
import string
import os


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 'Accept': "application/json"}

bookLangBtk = '5663693268320256'
bookLangInd = '6260074016145408'
bookIds = [
    '100c0cd9-dea4-469d-90bf-0057a7ae4aba',
    '203e8d02-7768-4b16-8892-ff87ab2501d5',
    '5eb939b0-2493-4dbb-b206-b4ccb6c2a648',
    '434524bc-4284-444b-9091-784b311430ed',
    '9d6d2a26-ead5-4a0b-88ff-87c0775046c7',
    '7cc98d50-d522-47a7-a8e3-f48a3255b707',
    '1c0431b0-ff43-4995-8a3d-711d3ff0b165',
    'b722fa1d-4622-4f9d-828f-0a9ddedbd05a',
    'ad99cff1-9c00-4da4-a23f-bf0a5c5a2287',
    'cacbc648-f4a3-4d5c-94eb-aa925aa431e2',
    '10f8d8af-3dac-4874-9582-bff4e41b1fbd',
    'b2bcc483-536b-4368-a6f0-32a3011214cf',
    '48f1a952-9aff-4a1a-9dfc-32dbffd4aa80',
    '675274a3-e67e-4b35-b6a1-7498d960e28c',
    '59874445-5f7c-40fe-a8f5-47ac380d4a86',
    '4a5788cd-47bd-4c96-b357-e5c994b6c0b6',
    'f8b23649-dc7b-4a21-b3db-4a97634e7275',
]
# https://letsreadasia.org/api/v5/book/preview/language/5663693268320256/book/203e8d02-7768-4b16-8892-ff87ab2501d5
folder = "output"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' telah dibuat")

translator = str.maketrans('', '', string.punctuation)
bookContents = []
for bookId in bookIds:
    URL = "https://letsreadasia.org/api/v5/book/preview/language/" + \
        bookLangBtk + "/book/" + bookId
    # URL = "https://letsreadasia.org/api/v5/book/preview/language/5663693268320256/book/203e8d02-7768-4b16-8892-ff87ab2501d5"
    # print(URL)
    URL_indo = "https://letsreadasia.org/api/v5/book/preview/language/" + \
        bookLangInd+"/book/"+bookId
    r_batak = requests.get(url=URL, headers=headers)
    r_indo = requests.get(url=URL_indo, headers=headers)
    data_batak = json.loads(r_batak.content)
    data_indo = json.loads(r_indo.content)
    bookContents.append(data_batak['name']+'~'+data_indo['name'])
    pages_batak = {page['pageNum']: BeautifulSoup(page['extractedLongContentValue'].rstrip(
        '\n'), 'html.parser').get_text() for page in data_batak['pages']}
    pages_indo = {page['pageNum']: BeautifulSoup(page['extractedLongContentValue'].rstrip(
        '\n'), 'html.parser').get_text() for page in data_indo['pages']}
    if data_batak['description'] is not None and data_indo['description'] is not None:
        pages_batak[0] = BeautifulSoup(
            data_batak['description'].rstrip('\n'), 'html.parser').get_text()
        pages_indo[0] = BeautifulSoup(
            data_indo['description'].rstrip('\n'), 'html.parser').get_text()

    pages_batak = dict(sorted(pages_batak.items(), key=lambda item: item[0]))
    pages_indo = dict(sorted(pages_indo.items(), key=lambda item: item[0]))

    title = data_batak['name'].translate(translator)
    title = title.replace(' ', '_')

    file_path = os.path.join(folder, title+"_batak.txt")
    with open(file_path, 'w') as file:
        for key, value in pages_batak.items():
            file.write(value + "\n")

    file_path = os.path.join(folder, title+"_indo.txt")
    with open(file_path, 'w') as file:
        for key, value in pages_indo.items():
            file.write(value + "\n")

    # if (len(pages_batak) != len(pages_indo)):
    #     print(data_batak['name'])
    #     print(URL)
    #     print(URL_indo)
    #     print('ERROR JUMLAH HALAMAN TIDAK SAMA!',
    #           len(pages_batak), len(pages_indo))
    #     print()
    #     break

    # bookContents.extend([xvalue+'~'+yvalue for xkey, xvalue, ykey,
    #                     yvalue in zip(pages_batak.items(), pages_indo.items())])

    # for i in range(1, min(len(pages_batak), len(pages_indo))-1):
    #     print(pages_batak[i]+'~'+pages_indo[i])
# print(bookContents)
# print(data_batak[])
# print(pages_batak)
# file_path = "output.txt"
# print(len(bookContents))
# for x in bookContents:
# with open(file_path, 'w') as file:
#     # Write the string to the file
#     for x in bookContents:
#         file.write(x+"\n")
#     # print(x)


# # Open the file in write mode ('w' or 'wt' for text mode)
