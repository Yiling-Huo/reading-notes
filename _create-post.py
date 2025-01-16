import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def fix_title(title, file_path):
    # if file already exists, check if the title in the file and here is the same, if so, skip everything, if not, append '-a' to the file name. 
    if os.path.exists(file_path):
        with open(file_path,'r', encoding='utf-8') as check_file:
            filec = [line for line in check_file]
            for line in filec:
                if line[:5] == 'title':
                    if title.lower() == line[7:].lower() or title == line[7:-1].lower(): # in case the last character is line break?
                        return file_path
                    else:
                        return fix_title(title, file_path.replace('.md', '') + '-a' + '.md')
    else:
        return file_path

def main():
    input_list = ["P://refs//library.bib", "P://refs//citations-merged.bib", "P://refs//references.bib"]
    for file in input_list:
        with open(file, 'r', encoding='utf-8') as inputfile:
            content = [line.replace('   ','').replace('  ','').replace('\t', '').replace(' = ','').replace(' =','').replace('=','') for line in inputfile]
            for line in content:
                if line[:5] in ['@misc','@book','@Manu','@inbook']:
                    print(line[:5])
                    title = ''
                    author_string = ''
                    author = []
                    tags = []
                    journal = ''
                    url = ''
                    year = ''
                    pass
                elif line[0] == '@':
                    print(line)
                    title = ''
                    author_string = ''
                    author = []
                    tags = []
                    journal = ''
                    url = ''
                    year = ''
                elif line[:5] == 'title':
                    print(line)
                    title = line[5:].replace('{','').replace('},','').replace('}','').replace(': ', ' - ')
                elif line[:6] == 'author':
                    print(line)
                    author_string = line[6:-3]
                    # first replace irregular alphabet with its form
                    author_string = author_string.replace('{\"a}', 'ä').replace('{\"o}', 'ö').replace('{\"u}', 'ü').replace('{\"i}', 'ï').replace('{\"e}', 'ë').replace("{\'a}", 'á').replace("{\'e}", 'é').replace("{\'i}", 'í').replace("{\'o}", 'ó').replace("{\'u}", 'ú').replace("{\'c}", 'ç').replace('{\~n}', 'ñ').replace('{\~a}', 'ã').replace('{\~o}', 'õ').replace('{\o}', 'ø').replace('{\`a}', 'à').replace('{\`e}', 'è').replace('{\`i}', 'ì').replace('{\`o}', 'ò').replace('{\`u}', 'ù')
                    # then replace the brackets
                    author_string = author_string.replace('{','').replace('},','').replace('}','') # is the last character the line break?
                    author = author_string.split(' and ')
                    print(author)
                    try:
                        first_author_name = author[0].split(', ')[0].lower().replace(' ','')
                        print(author[0].split(', ')[1]) # ask to print the second element so that split(',') has at least two elements
                    except IndexError:
                        first_author_name = author[0].split(' ')[-1].lower().replace(' ','')
                        author_string = ' and '.join([a.split(' ')[-1]+', '+' '.join(a.split(' ')[:-1]) for a in author])
                        print(author_string)
                elif line[:7] == 'journal':
                    print(line)
                    journal = line[7:].replace('{','').replace('},','').replace(',','')
                elif line[:3] == 'doi':
                    print(line)
                    url = 'https://doi.org/'+line[3:].replace('{','').replace('},','')
                elif line[:8] == 'keywords':
                    tags = line[8:].replace('{','').replace('},','').replace('\n','').split(',')
                elif line[:4] == 'year':
                    print(line)
                    year = line[5:9]
                elif line[0] == '}':
                    if len(title)>0:
                        file_path = fix_title(title, 'Article notes PhD/_posts/reference-generated/1996-01-01-'+first_author_name+'-'+str(year)+'.md')
                        try:
                            with open(file_path, 'w', encoding='utf-8') as outputfile:
                                output = '---\nlayout: post\ntitle: '+title+'\ndate: 1996-01-01 00:00\nauthor: '+author_string+'\ntags: ["'+'","'.join(tags).lower()+'"]\njournal: '+journal+'\nlink: '+url+'\nyear: '+year+'\n---'
                                output = output.replace('tags: [""]\n', '').replace('link: \n','').replace('author: \n','').replace('journal: \n','')
                                outputfile.write(output)
                        except OSError:
                            pass

if __name__ == "__main__":
    main()