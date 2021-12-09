fname = input('insert file name: ')
try:
    fhandle = open(fname)
except:
    print('the file dont exist')
    quit()
for line in fhandle:
    line = str.upper(line.rstrip())
    print(line)
