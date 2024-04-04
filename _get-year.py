import os

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    inputdirs = ['Article notes PhD/_posts/reference-generated/','Article notes PhD/_posts/']

    # inputdirs = ['Article notes PhD/_posts/test/']

    for dir in inputdirs:
        dataFileList = os.listdir(dir)
        for file in dataFileList:
            if file[-3:] == '.md':
                with open(dir + file, 'r+', encoding='utf-8') as inputfile:
                    year = file[-7:-3]
                    content = [line for line in inputfile]
                    first = True
                    # first_year_line = True
                    for i in range(len(content)):
                        if '---' in content[i] and first:
                            first = False
                        # break if year already exists
                        elif 'year: ' in content[i]:
                            break
                        # elif 'year: ' in content[i] and not first_year_line:
                        #     content.remove(content[i])
                        #     break
                        elif '---' in content[i] and not first:
                            try:
                                year1 = float(year)
                                content[i] = 'year: '+ year + '\n---\n'
                                print(year)
                                break
                            except ValueError:
                                break
                    inputfile.seek(0)
                    inputfile.write(''.join(content))

if __name__ == "__main__":
    main()