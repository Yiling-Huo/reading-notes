import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    input_list = ['_new.bib']
    for file in input_list:
        with open(file, 'r', encoding='utf-8') as inputfile:
            content = [line.replace('  ','') for line in inputfile]
            for line in content:
                if line[:5] in ['@misc','@book','@Manu']:
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
                elif line[:8] == 'title = ':
                    print(line)
                    title = line[8:].replace('{','').replace('},','').replace('}','').replace(': ', ' - ')
                elif line[:9] == 'author = ':
                    print(line)
                    author_string = line[10:-3] # is the last character the line break?
                    author = author_string.split(' and ')
                    print(author)
                    try:
                        first_author_name = author[0].split(', ')[0].lower().replace(' ','')
                    except IndexError:
                        first_author_name = author[0].split(' ')[-1].lower().replace(' ','')
                elif line[:10] == 'journal = ':
                    print(line)
                    journal = line[10:].replace('{','').replace('},','').replace(',','')
                elif line[:6] == 'doi = ':
                    print(line)
                    url = 'https://doi.org/'+line[6:].replace('{','').replace('},','')
                elif line[:11] == 'keywords = ':
                    tags = line[11:].replace('{','').replace('},','').split(',')
                elif line[:7] == 'year = ':
                    print(line)
                    year = line[8:12]
                elif line[0] == '}':
                    if title:
                        try:
                            with open('Article notes PhD/_posts/1996-01-01-'+first_author_name+'-'+str(year)+'.md', 'w', encoding='utf-8') as outputfile:
                                output = '---\nlayout: post\ntitle: '+title+'\ndate: 1996-01-01 00:00\nauthor: '+author_string+'\ntags: ["'+'","'.join(tags).lower()+'"]\njournal: '+journal+'\nlink: '+url+'\n---'
                                output = output.replace('tags: [""]\n', '').replace('link: \n','').replace('author: \n','').replace('journal: \n','')
                                outputfile.write(output)
                        except OSError:
                            pass

if __name__ == "__main__":
    main()