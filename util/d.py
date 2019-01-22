a=[('a','b','c','d','e','f','g','h'),('aa','bb','cc','dd','ee','ff','gg','hh'),('aaa','bbb','ccd','ddd','eee','fff','ggg','hhh')]
b=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
c={}
d=[]
for j in a:
    for n,i in zip(j,b):
        c[i]=n
        print(c)
    d.append(c)
    c={}
print(d)
