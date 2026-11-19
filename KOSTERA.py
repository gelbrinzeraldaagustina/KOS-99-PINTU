# ZERA
import pandas as pd
def cari_kamar():
    kamar = pd.read_csv("C:/Users/Admini/Documents/PROJECT ALGO SEM 1/KOS-99-PINTUdata_KAMAR.csv")

    print("\n========= PENCARIAN DATA KAMAR =========")
    print("1. Cari berdasarkan nomor kamar")
    print("2. Cari berdasarkan tipe kamar")
    print("3. Cari berdasarkan status kamar")

    pilihan = input("Pilih kategori pencarian: ")

    if pilihan == "1":
        kata_kunci = input("Masukkan nomor kamar: ")

        hasil = kamar[
            kamar["No_Kamar"].astype(str).str.contains(
                kata_kunci, case=False
            )
        ]

    elif pilihan == "2":
        kata_kunci = input("Masukkan tipe kamar: ")

        hasil = kamar[
            kamar["Tipe"].astype(str).str.contains(
                kata_kunci, case=False
            )
        ]

    elif pilihan == "3":
        kata_kunci = input("Masukkan status kamar: ")

        hasil = kamar[
            kamar["Status"].astype(str).str.contains(
                kata_kunci, case=False
            )
        ]

    else:
        print("Pilihan tidak valid!")
        return

    if len(hasil) > 0:
        print("\n========= HASIL PENCARIAN =========")
        print(hasil.to_string(index=False))
    else:
        print("\nData kamar tidak ditemukan!")

def menu_admin():

    while True:
        print("\n========= MENU ADMIN =========")
        print("1. Lihat informasi kamar")
        print("2. Cari data kamar")
        print("3. Tambah data kamar")
        print("4. Ubah data kamar")
        print("5. Hapus data kamar")
        print("6. Lihat data penghuni")
        print("7. Logout")


        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kamar()

        elif pilihan == "2":
            cari_kamar()

        elif pilihan == "3":
            tambah_kamar()

        elif pilihan == "4":
            ubah_kamar()

        elif pilihan == "5":
            hapus_kamar()

        elif pilihan == "6":
            tampilkan_penghuni()

        elif pilihan == "7":
            print("Logout berhasil!")
            break

        else:
            print("Pilihan tidak valid!")

menu_admin()


# PUTRI


# VALE
# import csv

# FILE_ADU = "data_PENGADUAN.csv"
# FILE_PENGHUNI = "data_PENGHUNI.csv"
# KOLOM = ["ID_Pengaduan", "ID_Penghuni", "Nama", "Fasilitas", "Deskripsi", "Identitas", "Status"]


# def baca_csv(nama_file):
#     try:
#         with open(nama_file, newline="", encoding="utf-8") as f:
#             return list(csv.DictReader(f))
#     except FileNotFoundError:
#         return []


# def simpan_pengaduan(data):
#     with open(FILE_ADU, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=KOLOM)
#         writer.writeheader()
#         writer.writerows(data)


# def buat_pengaduan():
#     data = baca_csv(FILE_ADU)
#     print("\n=== FORM PENGADUAN FASILITAS ===")

#     pakai_identitas = input("Gunakan identitas? (y/n): ").lower()
#     if pakai_identitas == "y":
#         id_penghuni = input("Masukkan ID penghuni (contoh P001): ").upper()
#         penghuni = next((p for p in baca_csv(FILE_PENGHUNI) if p["ID_Penghuni"] == id_penghuni), None)
#         if penghuni is None:
#             print("ID penghuni tidak ditemukan.")
#             return
#         nama, identitas = penghuni["Nama"], "Ya"
#     else:
#         id_penghuni, nama, identitas = "", "Anonim", "Tidak"

#     fasilitas = input("Fasilitas yang rusak: ")
#     deskripsi = input("Deskripsi kerusakan: ")

#     nomor = max([int(d["ID_Pengaduan"][1:]) for d in data], default=0) + 1
#     data.append({"ID_Pengaduan": f"A{nomor:03d}", "ID_Penghuni": id_penghuni, "Nama": nama,
#                  "Fasilitas": fasilitas, "Deskripsi": deskripsi,
#                  "Identitas": identitas, "Status": "Menunggu"})
#     simpan_pengaduan(data)
#     print(f"\nPengaduan A{nomor:03d} terkirim! Status: Menunggu")


# def lihat_pengaduan():
#     data = baca_csv(FILE_ADU)
#     print("\n=== DAFTAR PENGADUAN ===")
#     if not data:
#         print("Belum ada pengaduan.")
#     for d in data:
#         print(f"[{d['ID_Pengaduan']}] {d['Nama']} | {d['Fasilitas']} | {d['Deskripsi']} | {d['Status']}")
#     return data


# def ubah_status():
#     data = lihat_pengaduan()
#     if not data:
#         return

#     id_pilih = input("\nMasukkan ID pengaduan (contoh A001): ").upper()
#     status = {"1": "Menunggu", "2": "Diproses", "3": "Selesai"}

#     for d in data:
#         if d["ID_Pengaduan"] == id_pilih:
#             print("1. Menunggu\n2. Diproses\n3. Selesai")
#             pilih = input("Pilih status baru: ")
#             if pilih not in status:
#                 print("Pilihan tidak valid.")
#                 return
#             d["Status"] = status[pilih]
#             simpan_pengaduan(data)
#             print("Status pengaduan berhasil diperbarui!")
#             return

#     print("ID pengaduan tidak ditemukan.")


# def menu_penghuni():
#     while True:
#         print("\n=== MENU PENGHUNI ===")
#         print("1. Buat pengaduan\n2. Kembali")
#         pilih = input("Pilih menu: ")
#         if pilih == "1":
#             buat_pengaduan()
#         elif pilih == "2":
#             break
#         else:
#             print("Pilihan tidak valid!")


# def menu_admin():
#     while True:
#         print("\n=== MENU ADMIN ===")
#         print("1. Lihat daftar pengaduan\n2. Perbarui status pengaduan\n3. Kembali")
#         pilih = input("Pilih menu: ")
#         if pilih == "1":
#             lihat_pengaduan()
#         elif pilih == "2":
#             ubah_status()
#         elif pilih == "3":
#             break
#         else:
#             print("Pilihan tidak valid!")


# # Program utama (hanya jalan kalau file ini dijalankan langsung)
# if __name__ == "__main__":
#     while True:
#         print("\n==============================")
#         print("          KOSTERA")
#         print("   LAYANAN PENGADUAN KOS")
#         print("==============================")
#         print("1. Penghuni\n2. Admin\n3. Keluar")
#         pilih = input("Pilih menu: ")
#         if pilih == "1":
#             menu_penghuni()
#         elif pilih == "2":
#             menu_admin()
#         elif pilih == "3":
#             print("Terima kasih!")
#             break
#         else:
#             print("Pilihan tidak valid!")
   
# # SAFFA
# import pandas as pd
# import os

# folder = os.path.dirname(__file__)

# file_barang = os.path.join(folder, "data_barang.csv")
# file_pesanan = os.path.join(folder, "data_pesanan.csv")


# def tampilkan_barang():
#     data = pd.read_csv(file_barang)

#     print("\n========= DATA BARANG =========")
#     print(data.to_string(index=False))


# def tampilkan_pesanan():
#     pesanan = pd.read_csv(file_pesanan)

#     print("\n========= DATA PESANAN =========")
#     print(pesanan.to_string(index=False))


# def konfirmasi_pesanan():

#     pesanan = pd.read_csv(file_pesanan)
#     barang = pd.read_csv(file_barang)

#     tampilkan_pesanan()

#     pilihan = int(input("\nMasukkan ID pesanan: "))

#     if pilihan in pesanan["ID"].values:

#         index_pesanan = pesanan[
#             pesanan["ID"] == pilihan
#         ].index[0]

#         status = pesanan.loc[index_pesanan, "Status"]

#         if status != "Menunggu":
#             print("Pesanan sudah diproses!")

#         else:
#             nomor_barang = pesanan.loc[index_pesanan, "No"]
#             jumlah = pesanan.loc[index_pesanan, "Jumlah"]

#             index_barang = barang[
#                 barang["No"] == nomor_barang
#             ].index[0]

#             stok = barang.loc[index_barang, "Stok"]

#             if jumlah > stok:
#                 print("Stok tidak mencukupi!")
#                 pesanan.loc[index_pesanan, "Status"] = "Ditolak"

#             else:
#                 barang.loc[index_barang, "Stok"] -= jumlah

#                 pesanan.loc[index_pesanan, "Status"] = "Dikonfirmasi"

#                 print("Pesanan berhasil dikonfirmasi!")
#                 print("Sisa stok:", barang.loc[index_barang, "Stok"])

#             barang.to_csv(file_barang, index=False)
#             pesanan.to_csv(file_pesanan, index=False)

#     else:
#         print("ID pesanan tidak ditemukan!")


# # PROGRAM UTAMA
# while True:

#     print("\n========= MENU ADMIN =========")
#     print("1. Lihat data barang")
#     print("2. Lihat pesanan")
#     print("3. Konfirmasi pesanan")
#     print("4. Keluar")

#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
#         tampilkan_barang()

#     elif pilihan == "2":
#         tampilkan_pesanan()

#     elif pilihan == "3":
#         konfirmasi_pesanan()

#     elif pilihan == "4":
#         print("Program admin selesai!")
#         break

#     else:
#         print("Pilihan tidak valid!")
