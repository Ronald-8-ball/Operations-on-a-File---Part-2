with open('file.txt','w') as f1:
    f1.write("I replaced this line")
f1.close()

with open('file.txt','r') as f1:
    f1.readlines()
    for x in f1:
        data = x.split()
        print(data)
f1.close()


