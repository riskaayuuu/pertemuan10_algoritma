import pandas as pd
data = pd.DataFrame([
    [10,20,5],
    [30,10,7],
    [35,20,10],
    [8,7,9],
    [14,28,10],
    [10,20,5],
    [5,7,8]
], index=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Ahad'], columns=['Barang A','Barang B','Barang C'])
print(data)
total_penjualan_produk = data.sum(axis=0)
print('===Total penjualan untuk setiap produk selama seminggu===')
print(total_penjualan_produk)
total_penjualan_hari = data.sum(axis=1)
print('===Total penjualan set iap hari (Senin-Minggu)===')
print(total_penjualan_hari)
hari_terbanyak = total_penjualan_produk.idxmax()
print('===Produk dengan penjualan terbanyak selama seminggu===')
print(hari_terbanyak)
produk_terbanyak = total_penjualan_hari.idxmax()
print('===Hari dengan penjualan tertinggi untuk set iap produk===')
print(produk_terbanyak)