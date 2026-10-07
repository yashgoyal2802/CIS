import sys,re
f,pat=sys.argv[1],sys.argv[2]; w=int(sys.argv[3]); mx=int(sys.argv[4])
t=open(f,encoding='utf8',errors='ignore').read().split('\f')
n=0;last=-10**9
for i,p in enumerate(t,1):
    q=re.sub(r'\s+',' ',p);end=-1
    for m in re.finditer(pat,q,re.I):
        if m.start()<end: continue
        print(f'[pdfpage {i}]',q[max(0,m.start()-w):m.end()+w]);print();end=m.end()+w;n+=1
        if n>=mx: sys.exit()
