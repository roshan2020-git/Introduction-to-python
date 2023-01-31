'''
with open('index.html', 'r') as webpage:
    with open('excer2OP.txt' , 'a')as wf:
        for line in webpage.readlines():
            if '<a href=' in line:
                pos = line.find('<a href=')
                first_quote = line.find('\"' , pos)
                second_quote = line.find('\"' , first_quote+1)
                url = line[first_quote+1 : second_quote]
                wf.write(url + '\n')

'''
# better solution
with open('index.html' , 'r') as webpg:
    with open('output2.txt' , 'a') as wf:
        page = webpg.read()
        line_exist = True
        while line_exist:
            pos = page.find('<a href=')
            if pos == -1:
                line_exist = False
            else:
                first_quote = page.find('\"',pos)
                second_quote = page.find('\"' , first_quote+1)
                url = page[first_quote+1 : second_quote]
                wf.write(url + '\n')
                page = page[second_quote:]