import pandas as pd

'''df1= pd.read_csv("f1.csv")

df2 = pd.read_csv("f2.csv")
combdf = pd.concat([df1, df2], ignore_index=True)
comb = 'comb.csv'
combdf.to_csv(comb, index=False)
for i in range(3,368):
    file='f'+str(i)+'.csv'
    try:
        dfc=pd.read_csv(comb, low_memory=False)   
        df2 = pd.read_csv(file)
        combdf = pd.concat([dfc, df2], ignore_index=True)
        comb = 'comb.csv'
        combdf.to_csv(comb, index=False)
    except:
        pass'''
d={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
df = pd.read_csv("comb.csv", low_memory=False)
#print(df["DATE1"][:6])
for i in range(1,6684012):
    v=str(df[' DATE_1'][i]).split('-')
    df["date_python"][i]=v[0]+'/'+d[v[1]]+'/'+v[2][2:4]


