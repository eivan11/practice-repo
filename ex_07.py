try:
    fhandle = open('mbox2-short.txt')
except:
    print('file dont exict')
    quit()
count = 0
suma = 0.0
for line in fhandle:

    line = line.rstrip()
    if line.startswith('X-DSPAM-C'):
        count = count + 1
        bpos = line.find(':')
        suma = suma + float(line[bpos + 1 : ])
media =  suma/count    
print(media)
