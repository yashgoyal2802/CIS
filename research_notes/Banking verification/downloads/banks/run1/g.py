import sys,re
f,pat=sys.argv[1],sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 300
t=open(f,encoding='utf8',errors='ignore').read().split('\f')
for i,p in enumerate(t,1):
    q=re.sub(r'\s+',' ',p)
    for m in re.finditer(pat,q,re.I):
        print(f'[pdfpage {i}]',q[max(0,m.start()-w):m.end()+w]);print()
