# ZERA


# PUTRI


# VALE


# SAFFA
import pandas as pd

def tampilkan_data():
    fileDB = pd.read_csv("data_barang.csv")
    print("========= KATALOG BARANG =========")
    
    print(fileDB.to_string(index=False))
    return fileDB
tampilkan_data()

pilihan = int(input("\nMasukkan nomor barang: "))
if pilihan in fileDB["No"].values:
    jumlah = int(input("Masukkan jumlah pembelian: "))

    # Mengambil data barang yang dipilih
    index_barang = fileDB[
        fileDB["No"] == pilihan
    ].index[0]

    nama = fileDB.loc[index_barang, "Nama"]
    harga = fileDB.loc[index_barang, "Harga"]
    stok = fileDB.loc[index_barang, "Stok"]

    # Memeriksa jumlah pembelian
    if jumlah <= 0:
        print("Jumlah pembelian tidak valid!")

    elif jumlah > stok:
        print("Stok barang tidak mencukupi!")

    else:
        total = harga * jumlah

        print("\n===== DETAIL PESANAN =====")
        print("Nama barang:", nama)
        print("Harga satuan: Rp", harga)
        print("Jumlah:", jumlah)
        print("Total harga: Rp", total)

        # Konfirmasi admin
        konfirmasi = input(
            "\nKonfirmasi pesanan oleh admin (Y/N): "
        )

        if konfirmasi.upper() == "Y":

            # Mengurangi stok barang
            fileDB.loc[index_barang, "stok"] -= jumlah

            # Menyimpan perubahan ke CSV
            fileDB.to_csv(
                "data_barang.csv",
                index=False
            )

            print("\nPesanan berhasil dikonfirmasi!")
            print("Sisa stok:", fileDB.loc[index_barang, "stok"])

        else:
            print("Pesanan dibatalkan!")

else:
    print("Nomor barang tidak ditemukan!")