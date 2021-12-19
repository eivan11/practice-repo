file_name = "mbox-short.txt"
try:
    file_handel = open(file_name)
except:
    print(f"Systen can't find {file_name}")
    quit()
cout_most_regular = 0
dictionari = dict()
for file_line in file_handel:
    file_line = file_line.rstrip()
    if file_line.startswith("From"):
        mail_detail = file_line.split()
        if len(mail_detail) < 3:
            continue
        else:
            if mail_detail[2] not in dictionari:
                dictionari[mail_detail[2]] = 1
            else:
                dictionari[mail_detail[2]] = dictionari[mail_detail[2]] + 1
print(dictionari)
