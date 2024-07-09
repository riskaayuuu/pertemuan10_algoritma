import pandas as pd

#CARA 1
data = [
    [5,6,7],
    [12,7,8],
    [5,10,9]
]
hari =['senin','selasa','rabu']
barang =['a','b','c']

df = pd.DataFrame(data, index=hari, columns=barang).T
print(pd)


#CARA 2
df = pd.DataFrame([
    [5,6,7],
    [12,7,8],
    [5,10,9]
], index=['senin','selasa','rabu'], columns=['a','b','c'])
#index= untuk mengganti nama kolom, columns= untuk mengganti nama baris
print(df)


total_perbaris = df.sum(axis=0)
total_perkolom = df.sum(axis=1)
print(total_perbaris)
print(total_perkolom)

index_tertinggi = df.idxmax()
index_tertinggi_baris = df.idxmax(axis=0)
print(index_tertinggi)
print(index_tertinggi_baris)

index_tertinggi_perbaris = total_perbaris.idxmax()
print(index_tertinggi_perbaris)