#file_name =insert(" inset one of this file mbox-short.txt or mbox.txt: ")
file_name ='mbox.txt'
try:
    file_handel = open(file_name)
except:
    print(f"Systen can't find {file_name}")
    quit()
cout_most_regular = 0
dictionari = dict()
for file_line in file_handel:
    file_line = file_line.rstrip()
    if file_line.startswith('From'):
        mail_detail = file_line.split()
        if len(mail_detail) < 3:
            continue
        else:
            if mail_detail[1] not in dictionari:
                dictionari[mail_detail[1]] = 1
            else:
                dictionari[mail_detail[1]] = dictionari[mail_detail[1]] + 1
max_value = 0
mail = list(dictionari.keys())
for key_of_value in mail:
    temp_value = dictionari [key_of_value]
    if temp_value > max_value:
        max_value = temp_value
        max_mail = key_of_value

print(max_mail," ", max_value)
