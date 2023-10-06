import pandas as pd

df = pd.read_csv("i.csv")
# df['Name'] = df['Name'].str.title()

df['Category'] = df['Category'].str.title()


data_dict = df.to_dict('records')

#the name from csv should match here
a_names = [item['Name'] for item in data_dict]
names = a_names[::-1]
names = [s.split("/")[-1] for s in names]

cat = [item['Category'] for item in data_dict]



def get_names():
    return names


def get_c():
    return cat




