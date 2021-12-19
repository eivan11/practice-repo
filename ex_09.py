file_name = "wordlist.txt"
try:
    file_handel = open(file_name)
except:
    print(f"Systen can't find {file_name}")
    quit()

dic = dict()
pos = 1
for line in file_handel:
    words = line.split()
    for word   in words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] =dic[word] + 1
print(dic)
