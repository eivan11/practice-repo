sh = input("insert Hours: ")
sr = input("insert rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("insert the rigth values")
    quit()
if fh > 40 :
    ovp = (fh - 40) * (fr * .5)
    rp = (fh * fr)
    py = ovp + rp
else:
    py = fh * fr
print(py)

    

