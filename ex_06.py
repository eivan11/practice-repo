
def payment( h, r):
    if h > 40:
        ovp = (h - 40) * (r * .5)
        reg = (h * r)
        pay= reg + ovp
    else:
        pay = h * r
    return pay


sh = input("insert hours: ")
sr = input("insert rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("it's something wrong")
    quit()

paym = payment(fh, fr)

print("the payment is: ",paym)
=======
fname = input('insert file name: ')
try:
    fhandle = open(fname)
except:
    print('the file dont exist')
    quit()
for line in fhandle:
    line = str.upper(line.rstrip())
    print(line)

