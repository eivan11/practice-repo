file_name = "mbox-short.txt"
try:
    file_handel = open(file_name)
except:
    print(f"Systen can't find {file_name}")
    quit()
cout_most_regular = 0
find_from = "From"
print('# DEBUG: ',find_from)
dictionari = dict()
for file_line in file_handel:
    file_line = file_line.rstrip()
    list_content_line = file_line.split()
    for find_from in list_content_line:
        mail_position = max(list_content_line)
        #w = mail_position.split()
        if find_from not in list_content_line or '@' not in mail_position : continue

        #print('# DEBUG: ',mail_position)
        if mail_position not in dictionari:
            dictionari[mail_position] = 1
        else:
            dictionari[mail_position] = dictionari[mail_position] + 1
print(dictionari)
