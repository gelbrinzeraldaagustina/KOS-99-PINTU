import csv

FILE_ADU = "data_PENGADUAN.csv"
FILE_PENGHUNI = "data_PENGHUNI.csv"
KOLOM = ["ID_Pengaduan", "ID_Penghuni", "Nama", "Fasilitas", "Deskripsi", "Identitas", "Status"]


def baca_csv(nama_file):
    try:
        with open(nama_file, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def simpan_pengaduan(data):
    with open(FILE_ADU, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=KOLOM)
        writer.writeheader()
        writer.writerows(data)


def buat_pengaduan():
    data = baca_csv(FILE_ADU)
    print("\n=== FORM PENGADUAN FASILITAS ===")

    pakai_identitas = input("Gunakan identitas? (y/n): ").lower()
    if pakai_identitas == "y":
        id_penghuni = input("Masukkan ID penghuni (contoh P001): ").upper()
        penghuni = next((p for p in baca_csv(FILE_PENGHUNI) if p["ID_Penghuni"] == id_penghuni), None)
        if penghuni is None:
            print("ID penghuni tidak ditemukan.")
            return
        nama, identitas = penghuni["Nama"], "Ya"
    else:
        id_penghuni, nama, identitas = "", "Anonim", "Tidak"

    fasilitas = input("Fasilitas yang rusak: ")
    deskripsi = input("Deskripsi kerusakan: ")

    nomor = max([int(d["ID_Pengaduan"][1:]) for d in data], default=0) + 1
    data.append({"ID_Pengaduan": f"A{nomor:03d}", "ID_Penghuni": id_penghuni, "Nama": nama,
                 "Fasilitas": fasilitas, "Deskripsi": deskripsi,
                 "Identitas": identitas, "Status": "Menunggu"})
    simpan_pengaduan(data)
    print(f"\nPengaduan A{nomor:03d} terkirim! Status: Menunggu")


def lihat_pengaduan():
    data = baca_csv(FILE_ADU)
    print("\n=== DAFTAR PENGADUAN ===")
    if not data:
        print("Belum ada pengaduan.")
    for d in data:
        print(f"[{d['ID_Pengaduan']}] {d['Nama']} | {d['Fasilitas']} | {d['Deskripsi']} | {d['Status']}")
    return data


def ubah_status():
    data = lihat_pengaduan()
    if not data:
        return

    id_pilih = input("\nMasukkan ID pengaduan (contoh A001): ").upper()
    status = {"1": "Menunggu", "2": "Diproses", "3": "Selesai"}

    for d in data:
        if d["ID_Pengaduan"] == id_pilih:
            print("1. Menunggu\n2. Diproses\n3. Selesai")
            pilih = input("Pilih status baru: ")
            if pilih not in status:
                print("Pilihan tidak valid.")
                return
            d["Status"] = status[pilih]
            simpan_pengaduan(data)
            print("Status pengaduan berhasil diperbarui!")
            return

    print("ID pengaduan tidak ditemukan.")


def menu_penghuni():
    while True:
        print("\n=== MENU PENGHUNI ===")
        print("1. Buat pengaduan\n2. Kembali")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            buat_pengaduan()
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!")


def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat daftar pengaduan\n2. Perbarui status pengaduan\n3. Kembali")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            lihat_pengaduan()
        elif pilih == "2":
            ubah_status()
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")


# Program utama (hanya jalan kalau file ini dijalankan langsung)
if __name__ == "__main__":
    while True:
        print("\n==============================")
        print("          KOSTERA")
        print("   LAYANAN PENGADUAN KOS")
        print("==============================")
        print("1. Penghuni\n2. Admin\n3. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            menu_penghuni()
        elif pilih == "2":
            menu_admin()
        elif pilih == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")