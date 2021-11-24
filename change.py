with open('text1.txt','r') as r1:
    data1 = r1.read()
with open('text2.txt','r') as r2:
    data2 = r2.read()
with open('text1.txt','w') as w1:
    w1.write(data2)
with open('text2.txt','w') as w2:
    w2.write(data1)