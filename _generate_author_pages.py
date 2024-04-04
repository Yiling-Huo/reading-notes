import os

def main():
    inputdirs = ['Article notes PhD/_posts/reference-generated/','Article notes PhD/_posts/']

    outputdir = 'authors/author/'
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
        author_slugified = author.replace(', ', '-').replace(' ','-').replace('.','').lower()
        with open(outputdir+author_slugified+'.md', 'w', encoding='utf-8') as outputf:
            outputf.write('---\nlayout: author\nauthor: '+author+'\n---')

if __name__ == "__main__":
    main()