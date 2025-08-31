import pandas as pd

data = {
    'name':['q','w','e','r','t','y'],
    'city':['a','s','d','f','j','k'],
    'age':[12,23,31,25,18,21]
}

df = pd.DataFrame(data,index=[1,2,3,4,5,6])
print(df)
print(df.loc[3])
print(df.loc[4,'name'])
print(df.loc[:,'city'])

print(df.iloc[0,2])
print(df.iloc[2])
print(df.iloc[1,:])

# Filtering

print(df[(df['age']>20)])
print(df[(df['age']>20) & (df['city']=='s')])

print(df[df['name'].str.startswith('t')])

# Slicing

print(df[['age']])
print(df[1:2],'\n')

df2 = df.set_index('name')
print(df2)

df2.reset_index(inplace=True)

print(df2)

df2.rename(columns={'city':'location','name':'buttler'},inplace=True)
print(df2)

df2.rename(index={0:'first'},inplace=True)
print(df2)