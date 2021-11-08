sh = input("insert Hours: ")
sr = input("insert Rate: ")
fh = float(sh)
fr = float(sr)
if fh > 40:
    #print("overPay")
    rep= fh * fr
    ovp = (fh - 40.0) * (fr * 0.5)
    tp = rep + ovp
    print(tp)
else:
    #print("Regular")
    rep= fh * fr
    print(rep)

#print("Total To Pay ", tp)
