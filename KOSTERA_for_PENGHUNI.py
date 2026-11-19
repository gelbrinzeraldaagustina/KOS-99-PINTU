# KODE PROGRAM UNTUK TAMPILAN PENGHUNI

# LOGIN & INFORMASI KAMAR

# PEMBAYARAN DAN TAGIHAN 

# PENGADUAN

# PESAN BARANG

import pandas as pd
import os

folder = os.path.dirname(__file__)

file_barang = os.path.join(folder, "data_barang.csv")
file_pesanan = os.path.join(folder, "data_pesanan.csv")


def tampilkan_data():
    data = pd.read_csv(file_barang)

    print("\n========= KATALOG BARANG =========")
    print(data.to_string(index=False))

    return data


def pesan_barang():
    data = tampilkan_data()

    pilihan = int(input("\nMasukkan nomor barang: "))

    if pilihan in data["No"].values:

        index_barang = data[data["No"] == pilihan].index[0]

        nama = data.loc[index_barang, "Nama"]
        harga = data.loc[index_barang, "Harga"]
        stok = data.loc[index_barang, "Stok"]

        jumlah = int(input("Masukkan jumlah pembelian: "))

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

            konfirmasi = input(
                "\nKirim pesanan? (Y/N): "
            )

            if konfirmasi.upper() == "Y":

                pesanan = pd.read_csv(file_pesanan)

                nomor_pesanan = len(pesanan) + 1

                data_baru = {
                    "ID": nomor_pesanan,
                    "No": pilihan,
                    "Nama": nama,
                    "Jumlah": jumlah,
                    "Total": total,
                    "Status": "Menunggu"
                }

                pesanan.loc[len(pesanan)] = data_baru

                pesanan.to_csv(
                    file_pesanan,
                    index=False
                )

                print("\nPesanan berhasil dikirim!")
                print("Status: Menunggu konfirmasi admin")

            else:
                print("Pesanan dibatalkan!")

    else:
        print("Nomor barang tidak ditemukan!")

pesan_barang()