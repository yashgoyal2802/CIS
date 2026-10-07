import re,sys,urllib.request,concurrent.futures as cf,html
def get(i):
    u=f"https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id={i}&Mode=0"
    for _ in range(2):
        try:
            r=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124 Safari/537.36'})
            h=urllib.request.urlopen(r,timeout=30).read().decode('utf8','ignore')
            t=re.search(r'class="tableheader"[^>]*>.*?<b>(.*?)</b>',h,re.S)
            d=re.search(r'(\w{3} \d{1,2}, 20\d\d)',re.sub(r'<[^>]+>',' ',h[h.find('tableheader'):]) ) 
            txt=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h[h.find('tableheader'):]))[:260]
            return i,txt
        except Exception as e: err=str(e)
    return i,'ERR '+err
a,b=int(sys.argv[1]),int(sys.argv[2])
with cf.ThreadPoolExecutor(8) as ex:
    for i,t in ex.map(get,range(a,b)): print(i,html.unescape(t))
