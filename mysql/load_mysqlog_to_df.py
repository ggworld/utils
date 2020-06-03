import pandas as pd 
general_log = open("/Users/allcloud/Downloads/mysql-slowquery.log.11.txt")
log = SlowQueryLog(general_log)
c=0
try:
    while True:
        t=log.next()
        if c==0:
            df=pd.DataFrame(t,index=[0])
        else:
            df=df.append(pd.DataFrame(t,index=[0]))
        
        c+=1 
except StopIteration:
    print(c)
df.head()
