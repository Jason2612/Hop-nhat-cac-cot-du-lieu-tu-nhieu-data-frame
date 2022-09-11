import pandas as pd
df = pd.read_csv("data\FoodPrice_in_Turkey.csv")

df = df.drop_duplicates(['ProductId'], keep = 'last').reset_index(drop=True)

df_pro = df.loc[:, ['ProductId','ProductName','UmId','Umnane']]

df_pro10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]

df1 = pd.merge(df_pro, df_pro10, on = 'ProductId')

df2 = pd.concat([df_pro, df_pro10], axis=1)
print(df2)