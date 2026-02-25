import os
from unidecode import unidecode

def main():
    inputdirs = ['References/_posts/','Article notes PhD/_posts/', 'Article notes 2025/_posts/']

    outputdir = 'authors/'
    author_list = []

    for dir in inputdirs:
        dataFileList = os.listdir(dir)
        for dataFile in dataFileList:
            if dataFile[-3:]=='.md':
                with open(dir + dataFile, 'r', encoding='utf-8') as inputf:
                    for line in inputf.readlines():
                        string = str(line)
                        if 'author: ' in string:
                            authors = string[:-1].replace('author: ','').split(' and ')
                            for author in authors:
                                author_list.append(author.strip('"'))

    # print(author_list)

    for author in author_list:
        author_slugified = unidecode(author).replace(', ', '-').replace(' ','-').replace('.','').lower() # use unaccented version for urls
        with open(outputdir+author_slugified+'.md', 'w', encoding='utf-8') as outputf:
            outputf.write('---\nlayout: author\nauthor: '+author+'\n---')
            print("Author page created: " + author)

if __name__ == "__main__":
    main()