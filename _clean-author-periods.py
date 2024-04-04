import os

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inputdir = 'Article notes PhD/_posts/reference-generated/'
    dataFileList = os.listdir(inputdir)

    for file in dataFileList:
        with open(inputdir + file, 'r+', encoding='utf-8') as inputfile:
            content = [line for line in inputfile]
            for i in range(len(content)):
                if content[i][:8] == 'author: ':
                    content[i] = content[i].replace('.', '')
                    print(content[i])
            inputfile.seek(0)
            inputfile.write(''.join(content))

if __name__ == "__main__":
    main()