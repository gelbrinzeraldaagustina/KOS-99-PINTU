# ZERA


# PUTRI


# VALE
import os

print("Lokasi program:", os.path.dirname(os.path.abspath(__file__)))
print("Lokasi terminal:", os.getcwd())

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("File penghuni ditemukan:", os.path.exists("data_PENGHUNI.csv"))
print("File pengaduan ditemukan:", os.path.exists("data_PENGADUAN.csv"))

import pandas as pd

filePenghuni = pd.read_csv("data_PENGHUNI.csv", dtype=str, keep_default_na=False, encoding="utf-8-sig")
filePengaduan = pd.read_csv("data_PENGADUAN.csv", dtype=str, keep_default_na=False, encoding="utf-8-sig")

pesanStatus = {
    "Menunggu": "Pengaduan belum ditanggapi oleh ibu kos.",
    "Diproses": "Ibu kos sedang menangani pengaduan ini.",
    "Selesai": "Pengaduan sudah selesai ditangani oleh ibu kos."
}

print("\n========= LAYANAN PENGADUAN KOSTERA =========")
print("1. Penghuni")
print("2. Admin (Ibu Kos)")
peran = input("\nPilih peran: ")

# ================= PENGHUNI =================
if peran == "1":
    print("\n1. Buat pengaduan")
    print("2. Cek status pengaduan")
    menu = input("Pilih menu: ")

    idPenghuni = input("Masukkan ID penghuni (contoh P001): ").strip().upper()

    if idPenghuni in filePenghuni["ID_Penghuni"].values:

        # Mengambil data penghuni yang login
        index_penghuni = filePenghuni[
            filePenghuni["ID_Penghuni"] == idPenghuni
        ].index[0]

        nama = filePenghuni.loc[index_penghuni, "Nama"]

        # ---------- Buat pengaduan ----------
        if menu == "1":
            fasilitas = input("Fasilitas yang rusak: ")
            deskripsi = input("Deskripsi kerusakan: ")

            if fasilitas.strip() == "" or deskripsi.strip() == "":
                print("Fasilitas dan deskripsi tidak boleh kosong!")

            else:
                # Membuat ID pengaduan baru (A001, A002, ...)
                if filePengaduan.empty:
                    nomor = 1
                else:
                    nomor = filePengaduan["ID_Pengaduan"].str[1:].astype(int).max() + 1

                idBaru = f"A{nomor:03d}"

                # Menambah pengaduan baru
                filePengaduan.loc[len(filePengaduan)] = [
                    idBaru, idPenghuni, nama, fasilitas, deskripsi, "Ya", "Menunggu"
                ]

                # Menyimpan perubahan ke CSV
                filePengaduan.to_csv(
                    "data_PENGADUAN.csv",
                    index=False
                )

                print("\nPengaduan", idBaru, "berhasil dikirim!")
                print("Status: Menunggu")

        # ---------- Cek status pengaduan ----------
        elif menu == "2":
            hasil =
   
# SAFFA
import os

print("Lokasi program:", os.path.dirname(__file__))
print("Lokasi terminal:", os.getcwd())
print("File CSV ditemukan:", os.path.exists("data_barang.csv"))

import pandas as pd

def tampilkan_data():
    fileDB = pd.read_csv("data_barang.csv")
    print("========= KATALOG BARANG =========")
    
    print(fileDB.to_string(index=False))
    return fileDB
fileDB = tampilkan_data()

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
            fileDB.loc[index_barang, "Stok"] -= jumlah

            # Menyimpan perubahan ke CSV
            fileDB.to_csv(
                "data_barang.csv",
                index=False
            )

            print("\nPesanan berhasil dikonfirmasi!")
            print("Sisa stok:", fileDB.loc[index_barang, "Stok"])

        else:
            print("Pesanan dibatalkan!")

else:
    print("Nomor barang tidak ditemukan!")
