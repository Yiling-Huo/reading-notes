import os

def main():
    inputdir = 'Article notes PhD/_posts/'
    dataFileList = os.listdir(inputdir)

    outputdir = 'authors/author/'
    author_list = []

    for dataFile in dataFileList:
        if dataFile[-3:]=='.md':
            with open(inputdir + dataFile, 'r', encoding='utf-8') as inputf:
                for line in inputf.readlines():
                    string = str(line)
                    if 'author: ' in string:
                        authors = string[:-1].replace('author: ','').split(' and ')
                        for author in authors:
                            author_list.append(author.strip('"'))

    # print(author_list)

    for author in author_list:
        author_slugified = author.replace(', ', '-').replace(' ','-').lower()
        with open(outputdir+author_slugified+'.md', 'w', encoding='utf-8') as outputf:
            outputf.write('---\nlayout: author\nauthor: '+author+'\n---')

if __name__ == "__main__":
    main()