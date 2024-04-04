import os

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inputdir = 'Article notes PhD/_posts/reference-generated/'
    dataFileList = os.listdir(inputdir)

    for file in dataFileList:
        with open(inputdir + file, 'r+', encoding='utf-8') as inputfile:
            content = [line for line in inputfile]
            for i in range(len(content)):
                if content[i][:9] == 'journal: ':
                    content[i] = content[i].replace(',', '')
                    content[i][9:] = content[i][9:].replace(':','')
                    if len(content[i]) <= 10:
                        content.remove(content[i])
                        break
                    print(content[i])
                    print(len(content[i]))
                elif content[i][:8] == 'journal ':
                    content[i] = 'journal: '+content[i][8:]
                    print(content[i])
                    print(len(content[i]))
            inputfile.seek(0)
            inputfile.write(''.join(content))

if __name__ == "__main__":
    main()