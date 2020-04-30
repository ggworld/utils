import pandas as pd
df=pd.read_html('/Users/allcloud/Downloads/Jira-Soft 2020-04-30T18_31_04+0300.html')
df[1][['Key','Summary','Status','Priority','Severity']].head(10).to_excel('/Users/allcloud/Downloads/shlo.xlsx',index=False)
