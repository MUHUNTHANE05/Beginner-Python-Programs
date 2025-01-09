prev=0
cur=1
nxt=0
for i in range(0,12):
    nxt=prev+cur
    prev=cur
    cur=nxt    
    print(nxt)
    
    
    
