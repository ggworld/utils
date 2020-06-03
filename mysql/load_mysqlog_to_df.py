#using the sql_log_parser.py delivery
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', -1)
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
df['query_time']=df.query_time.astype(float)
df.nlargest(10,'query_time')
