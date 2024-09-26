from datetime import datetime, timedelta
import requests
import pandas as pd


def download_file(url, filename):
    try:
        response = requests.get(url)
        v=response.status_code
        print(v)
        if v == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    return 1



today = datetime.now()
st="https://archives.nseindia.com/products/content/sec_bhavdata_full_"
end=".csv"
curr = str(today).split('-')
#link=st+curr[-1][:2]+curr[-2]+curr[-3]+end
link="https://archives.nseindia.com/products/content/sec_bhavdata_full_25092024.csv"
download_file(link,"combine_F.csv")
df = pd.read_csv("combine_F.csv")
df['date_python']=str(today)
for i in range(8,370):
    v=today - timedelta(days=i)
    curr = str(v).split('-')
    link=st+curr[-1][:2]+curr[-2]+curr[-3]+end
    date_object = datetime.strptime(curr[0]+'-'+curr[1]+'-'+curr[2][:2], '%Y-%m-%d')
    day_name = date_object.strftime('%A')
    if day_name in ["Sunday", "Saturday"]:
        #print('sunday or staurday')
        continue
    cr_file='f'+str(i)+'.csv'
    f=download_file(link,cr_file)
    if f:
        df1 = pd.read_csv("combine_F.csv")
        df2 = pd.read_csv(cr_file)
        df2['date_python']=str(v)
        combined_df = pd.concat([df1, df2], ignore_index=True)
        combine_F = 'combine_F.csv'
        combined_df.to_csv(combine_F, index=False)

print(f'Combined Excel file saved as: {combine_F}')