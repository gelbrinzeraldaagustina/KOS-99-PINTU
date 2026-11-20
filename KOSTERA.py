import csv
import os

FILE_KAMAR = "data_kamar.csv"
FILE_PENGHUNI = "data_penghuni.csv"
FILE_TAGIHAN = "data_tagihan.csv"
FILE_PENGADUAN = "data_pengaduan.csv"
FILE_BARANG = "data_barang.csv"
FILE_PESANAN = "data_pesanan.csv"

# [No.1] Tipe Data: string, int, float, boolean
NAMA_APP = "KOSTERA"  
  

# ---------- Helper CSV ----------
def baca_csv(nama_file):
    # [No.6] File Handling: Membaca file
    if not os.path.exists(nama_file):
        return []
    with open(nama_file, mode='r', newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def tulis_csv(nama_file, fieldnames, data):
    # [No.6] File Handling: Menyimpan file
    with open(nama_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def garis():
    print("="*60)

def buat_id(prefix, data, key):
    if not data:
        return f"{prefix}001"
    nums = []
    for d in data:
        try:
            
            kode = str(d.get(key, "")).strip()
            if not kode:
                continue
            
            angka = kode[len(prefix):]
            if angka.isdigit():
                nums.append(int(angka))
        except:
            continue
    if not nums:
        return f"{prefix}001"
    return f"{prefix}{max(nums)+1:03d}"

# ---------- A. PENGELOLAAN KAMAR ----------
def lihat_kamar():
    data = baca_csv(FILE_KAMAR)
    garis()
    print("                     DAFTAR KAMAR")
    print(f"{'No':<8} {'Tipe':<10} {'Harga':<12} {'Status':<10}")
    # [No.2] List + [No.5] For
    for k in data:
        print(f"{k['No_Kamar']:<8} {k['Tipe']:<10} Rp{k['Harga_Sewa']:<10} {k['Status']:<10}")
    garis()

def cari_kamar():
    data = baca_csv(FILE_KAMAR)
    garis()
    print("                     CARI KAMAR")
    keyword = input("Kata kunci (101 / Single / Kosong): ").lower()  # [No.3] Manipulasi string
    hasil = [k for k in data if keyword in k['No_Kamar'].lower() or keyword in k['Tipe'].lower() or keyword in k['Status'].lower() or keyword in k['Harga_Sewa']]
    if not hasil:
        print("Kamar tidak ditemukan!")
    else:
        print(f"Ditemukan {len(hasil)} kamar:")
        for k in hasil:
            print(f"- {k['No_Kamar']} | {k['Tipe']} | Rp{k['Harga_Sewa']} | {k['Status']}")
    garis()

def tambah_kamar():
    data = baca_csv(FILE_KAMAR)
    no = input("No Kamar (misal 106): ").upper()  # [No.3] String
    # [No.4] Operator NOT + AND
    if not no.isdigit() and not no.isalnum():
        print("No Kamar tidak valid!")
        return
    if any(k['No_Kamar'] == no for k in data):
        print("Kamar sudah ada!")
        return
    tipe = input("Tipe (Single/Double): ")
    harga = int(input("Harga Sewa: "))  # [No.1] int
    # [No.4] OR untuk validasi
    if harga <= 0 or tipe == "":
        print("Data tidak valid!")
        return
    data.append({"No_Kamar": no, "Tipe": tipe, "Harga_Sewa": str(harga), "Status": "Kosong"})
    tulis_csv(FILE_KAMAR, ["No_Kamar","Tipe","Harga_Sewa","Status"], data)
    print("Kamar berhasil ditambah!")

def ubah_kamar():
    data = baca_csv(FILE_KAMAR)
    no = input("No Kamar yang diubah: ")
    for k in data:
        if k['No_Kamar'] == no:
            k['Tipe'] = input(f"Tipe baru ({k['Tipe']}): ") or k['Tipe']
            k['Harga_Sewa'] = input(f"Harga baru ({k['Harga_Sewa']}): ") or k['Harga_Sewa']
            k['Status'] = input(f"Status baru Kosong/Terisi ({k['Status']}): ") or k['Status']
            tulis_csv(FILE_KAMAR, ["No_Kamar","Tipe","Harga_Sewa","Status"], data)
            print("Kamar berhasil diubah!")
            return
    print("Kamar tidak ditemukan!")

def hapus_kamar():
    data = baca_csv(FILE_KAMAR)
    no = input("No Kamar yang dihapus: ")
    # [No.4] NOT untuk cek
    if not any(k['No_Kamar'] == no for k in data):
        print("Kamar tidak ditemukan!")
        return
    baru = [k for k in data if k['No_Kamar'] != no]
    tulis_csv(FILE_KAMAR, ["No_Kamar","Tipe","Harga_Sewa","Status"], baru)
    print("Kamar berhasil dihapus!")

def tambah_penghuni():
    penghuni = baca_csv(FILE_PENGHUNI)
    kamar = baca_csv(FILE_KAMAR)
    tagihan = baca_csv(FILE_TAGIHAN)
    id_baru = buat_id("P", penghuni, "ID_Penghuni")
    nama = input("Nama: ").title()
    no_kamar = input("No Kamar: ")
    k = next((x for x in kamar if x['No_Kamar'] == no_kamar), None)
    # [No.4] AND + NOT
    if k is None or k['Status'] == "Terisi":
        print("Kamar tidak ada atau sudah terisi!")
        return
    hp = input("No HP: ")
    penghuni.append({"ID_Penghuni": id_baru, "Nama": nama, "No_Kamar": no_kamar, "No_HP": hp})
    tulis_csv(FILE_PENGHUNI, ["ID_Penghuni","Nama","No_Kamar","No_HP"], penghuni)
    k['Status'] = "Terisi"
    tulis_csv(FILE_KAMAR, ["No_Kamar","Tipe","Harga_Sewa","Status"], kamar)
    id_tag = buat_id("T", tagihan, "ID_Tagihan")
    tagihan.append({"ID_Tagihan": id_tag, "ID_Penghuni": id_baru, "Bulan": "November 2026", "Jumlah": k['Harga_Sewa'], "Tanggal_Jatuh_Tempo": "10-11-2026", "Status": "Belum Lunas"})
    tulis_csv(FILE_TAGIHAN, ["ID_Tagihan","ID_Penghuni","Bulan","Jumlah","Tanggal_Jatuh_Tempo","Status"], tagihan)
    print(f"Berhasil! ID: {id_baru}, Login pakai {id_baru} / {hp}")

def data_penghuni_admin():
    penghuni = baca_csv(FILE_PENGHUNI)
    garis()
    print("DATA PENGHUNI")
    for p in penghuni:
        print(f"{p['ID_Penghuni']} | {p['Nama']} | Kamar {p['No_Kamar']} | HP {p['No_HP']}")
    garis()
    if input("1. Tambah Penghuni  2. Kembali : ") == "1":
        tambah_penghuni()

# ---------- B. PEMBAYARAN ----------
def lihat_tagihan(id_penghuni=None):
    data = baca_csv(FILE_TAGIHAN)
    penghuni = {p['ID_Penghuni']: p for p in baca_csv(FILE_PENGHUNI)}
    if id_penghuni:
        data = [t for t in data if t['ID_Penghuni'] == id_penghuni]
    garis()
    print("TAGIHAN PEMBAYARAN")
    for t in data:
        nama = penghuni.get(t['ID_Penghuni'], {}).get('Nama', '-')
        # [No.1] boolean untuk status lunas
        is_lunas = (t['Status'] == "Lunas")  # boolean
        print(f"{t['ID_Tagihan']} | {nama} | {t['Bulan']} | Rp{t['Jumlah']} | Jatuh Tempo: {t['Tanggal_Jatuh_Tempo']} | Lunas: {is_lunas} | Status: {t['Status']}")
    garis()

def update_pembayaran():
    lihat_tagihan()
    data = baca_csv(FILE_TAGIHAN)
    id_tag = input("ID Tagihan yang dibayar (T001): ").upper()
    for t in data:
        if t['ID_Tagihan'] == id_tag:
            # [No.1] boolean untuk status lunas - tanpa diskon
            is_lunas = True
            if is_lunas:
                t['Status'] = "Lunas"
                tulis_csv(FILE_TAGIHAN, ["ID_Tagihan","ID_Penghuni","Bulan","Jumlah","Tanggal_Jatuh_Tempo","Status"], data)
                print("Status diubah menjadi LUNAS!")
            return
    print("ID tidak ditemukan!")

# ---------- C. PENGADUAN (TANPA ANONIM) ----------
def buat_pengaduan(id_penghuni, nama_penghuni):
    data = baca_csv(FILE_PENGADUAN)
    garis()
    print("                     BUAT PENGADUAN FASILITAS")
    fasilitas = input("Fasilitas: ")
    deskripsi = input("Deskripsi: ")
    id_baru = buat_id("A", data, "ID_Pengaduan")
    data.append({"ID_Pengaduan": id_baru, "ID_Penghuni": id_penghuni, "Nama": nama_penghuni, "Fasilitas": fasilitas, "Deskripsi": deskripsi, "Identitas": "Ya", "Status": "Menunggu"})
    tulis_csv(FILE_PENGADUAN, ["ID_Pengaduan","ID_Penghuni","Nama","Fasilitas","Deskripsi","Identitas","Status"], data)
    print(f"Pengaduan {id_baru} berhasil dikirim atas nama {nama_penghuni}!")

def lihat_pengaduan(id_penghuni=None):
    data = baca_csv(FILE_PENGADUAN)
    if id_penghuni:
        data = [p for p in data if p['ID_Penghuni'] == id_penghuni]
    garis()
    print("                     DAFTAR PENGADUAN")
    for p in data:
        print(f"{p['ID_Pengaduan']} | {p['Nama']} | {p['Fasilitas']} | {p['Deskripsi']} | Status: {p['Status']}")
    garis()

def update_pengaduan():
    lihat_pengaduan()
    data = baca_csv(FILE_PENGADUAN)
    id_p = input("ID Pengaduan: ").upper()
    for p in data:
        if p['ID_Pengaduan'] == id_p:
            print("1. Menunggu  2. Diproses  3. Selesai")
            pil = input("Status baru: ")
            mapping = {"1": "Menunggu", "2": "Diproses", "3": "Selesai"}
            if pil in mapping:
                p['Status'] = mapping[pil]
                tulis_csv(FILE_PENGADUAN, ["ID_Pengaduan","ID_Penghuni","Nama","Fasilitas","Deskripsi","Identitas","Status"], data)
                print("Status diperbarui!")
            return
    print("ID tidak ditemukan!")

# ---------- D. PESAN BARANG ----------
def katalog_barang():
    data = baca_csv(FILE_BARANG)
    garis()
    print("                     KATALOG BARANG")
    for b in data:
        print(f"{b['No']}. {b['Nama']} | Rp{b['Harga']} | Stok: {b['Stok']}")
    garis()

def cari_barang():
    data = baca_csv(FILE_BARANG)
    keyword = input("Cari Barang (Mi / Galon / Kopi): ").lower()
    hasil = [b for b in data if keyword in b['Nama'].lower()]
    if not hasil:
        print("Barang tidak ditemukan!")
    else:
        for b in hasil:
            print(f"- {b['No']}. {b['Nama']} | Rp{b['Harga']} | Stok: {b['Stok']}")

def pesan_barang(id_penghuni):
    katalog_barang()
    barang_list = baca_csv(FILE_BARANG)
    pesanan = baca_csv(FILE_PESANAN)

    no = input("Pilih No Barang: ").strip()
    # try HANYA di sini, buat jumlah
    try:
        jumlah = int(input("Jumlah: ").strip())
    except ValueError:
        print("Jumlah harus angka!")
        return

    barang = next((b for b in barang_list if b['No'].strip() == no), None)
    if barang is None or jumlah <= 0:
        print("Barang / jumlah tidak valid!")
        return
    if jumlah > int(barang['Stok']):
        print(f"Stok tidak cukup! Sisa {barang['Stok']}")
        return

    total = int(barang['Harga']) * jumlah
    print(f"Total: Rp{total} ({barang['Nama']} x {jumlah})")
    lanjut = input("Lanjut? (y/n): ").strip().lower()
    if lanjut == "y":
        id_baru = buat_id("O", pesanan, "ID_Pesanan")
        pesanan.append({"ID_Pesanan": id_baru, "ID_Penghuni": id_penghuni, "Nama_Barang": barang['Nama'], "Jumlah": str(jumlah), "Total": str(total), "Status": "Diproses"})
        tulis_csv(FILE_PESANAN, ["ID_Pesanan","ID_Penghuni","Nama_Barang","Jumlah","Total","Status"], pesanan)
        print(f"Pesanan {id_baru} berhasil dibuat!")
    else:
        print("Pesanan dibatalkan.")

def kelola_pesanan():
    data = baca_csv(FILE_PESANAN)
    garis()
    print("DAFTAR PESANAN")
    print(f"File dibaca dari: {FILE_PESANAN}")
    if not data:
        print("Belum ada pesanan. Coba buat pesanan dulu dari akun penghuni.")
        return
    for p in data:
        print(f"{p['ID_Pesanan']} | {p['ID_Penghuni']} | {p['Nama_Barang']} x{p['Jumlah']} | Rp{p['Total']} | {p['Status']}")
    garis()
    print("1. Konfirmasi & Kurangi Stok  2. Update Status  3. Kembali")
    pil = input("Pilih: ")
    if pil == "1":
        id_p = input("ID Pesanan: ").upper()
        for p in data:
            if p['ID_Pesanan'] == id_p and p['Status'] == "Diproses":
                barang_list = baca_csv(FILE_BARANG)
                b = next((x for x in barang_list if x['Nama'] == p['Nama_Barang']), None)
                if b and int(b['Stok']) >= int(p['Jumlah']):
                    b['Stok'] = str(int(b['Stok']) - int(p['Jumlah']))
                    tulis_csv(FILE_BARANG, ["No","Nama","Harga","Stok"], barang_list)
                    p['Status'] = "Sedang Diantar"
                    tulis_csv(FILE_PESANAN, ["ID_Pesanan","ID_Penghuni","Nama_Barang","Jumlah","Total","Status"], data)
                    print("Dikonfirmasi! Stok dikurangi, status jadi Sedang Diantar.")
                else:
                    print("Stok tidak cukup!")
                return
        print("Pesanan tidak ditemukan / sudah dikonfirmasi!")
    elif pil == "2":
        id_p = input("ID Pesanan: ").upper()
        for p in data:
            if p['ID_Pesanan'] == id_p:
                print("1. Diproses  2. Sedang Diantar  3. Selesai")
                st = input("Status baru: ")
                mapping = {"1": "Diproses", "2": "Sedang Diantar", "3": "Selesai"}
                if st in mapping:
                    p['Status'] = mapping[st]
                    tulis_csv(FILE_PESANAN, ["ID_Pesanan","ID_Penghuni","Nama_Barang","Jumlah","Total","Status"], data)
                    print("Status diperbarui!")
                return
            
def lihat_pesanan_saya(id_penghuni):
    if not os.path.exists(FILE_PESANAN):
        print("Belum ada pesanan.")
        return
    data = [p for p in baca_csv(FILE_PESANAN) if p['ID_Penghuni'] == id_penghuni]
    for p in data:
        print(f"- {p['ID_Pesanan']} | {p['Nama_Barang']} x{p['Jumlah']} | Rp{p['Total']} | {p['Status']}")

# ---------- FITUR TAMBAHAN: REKAP (NESTED LOOP) ----------
def rekap_laporan():
    kamars = baca_csv(FILE_KAMAR)
    penghunis = baca_csv(FILE_PENGHUNI)
    tagihans = baca_csv(FILE_TAGIHAN)
    garis()
    print("             REKAP KOSTERA - PENDAPATAN & TAGIHAN")
    total_pendapatan = 0
    total_lunas = 0
    
    for k in kamars:
        print(f"\nKamar {k['No_Kamar']} ({k['Tipe']} - {k['Status']}):")
        ada = False
        
        for p in penghunis:
            if p['No_Kamar'] == k['No_Kamar']:
                ada = True
                
                for t in tagihans:
                    if t['ID_Penghuni'] == p['ID_Penghuni']:
                        print(f"  - {p['Nama']} | Tagihan {t['Bulan']} Rp{t['Jumlah']} | {t['Status']}")
                        if t['Status'] == "Lunas":
                            total_pendapatan += int(t['Jumlah'])
                            total_lunas += 1
        if not ada:
            print("  - (Kosong, belum ada penghuni)")
    print(f"\nTotal Tagihan Lunas: {total_lunas} | Total Pendapatan: Rp{total_pendapatan}")
    garis()

# ---------- MENU ----------
def menu_admin():
    while True:  
        garis()
        print("                 MENU ADMIN - KOSTERA")
        print("A. KAMAR: 1.Lihat  2.Cari  3.Tambah  4.Ubah  5.Hapus  6.Data Penghuni")
        print("B. BAYAR: 7.Lihat Tagihan  8.Update Lunas")
        print("C. ADUAN: 9.Lihat Aduan  10.Update Status")
        print("D. BARANG: 11.Katalog  12.Cari Barang  13.Kelola Pesanan  14.Rekap")
        print("0. Logout")
        pil = input("Pilih menu: ")
        if pil == "1": lihat_kamar()
        elif pil == "2": cari_kamar()
        elif pil == "3": tambah_kamar()
        elif pil == "4": ubah_kamar()
        elif pil == "5": hapus_kamar()
        elif pil == "6": data_penghuni_admin()
        elif pil == "7": lihat_tagihan()
        elif pil == "8": update_pembayaran()
        elif pil == "9": lihat_pengaduan()
        elif pil == "10": update_pengaduan()
        elif pil == "11": katalog_barang()
        elif pil == "12": cari_barang()
        elif pil == "13": kelola_pesanan()
        elif pil == "14": rekap_laporan()
        elif pil == "0": break
        else: print("Menu tidak valid!")

def menu_penghuni(id_penghuni, nama):
    while True:
        garis()
        print(f"          MENU PENGHUNI - Halo, {nama} ({id_penghuni})")
        print("1. Lihat Kamar  2. Cari Kamar  3. Lihat Tagihan Saya")
        print("4. Buat Pengaduan  5. Lihat Pengaduan Saya")
        print("6. Katalog  7. Cari Barang  8. Pesan Barang  9. Pesanan Saya")
        print("0. Logout")
        pil = input("Pilih menu: ")
        if pil == "1": lihat_kamar()
        elif pil == "2": cari_kamar()
        elif pil == "3": lihat_tagihan(id_penghuni)
        elif pil == "4": buat_pengaduan(id_penghuni, nama)
        elif pil == "5": lihat_pengaduan(id_penghuni)
        elif pil == "6": katalog_barang()
        elif pil == "7": cari_barang()
        elif pil == "8": pesan_barang(id_penghuni)
        elif pil == "9": lihat_pesanan_saya(id_penghuni)
        elif pil == "0": break
        else: print("Menu tidak valid!")

def main():
    while True:
        garis()
        print(f"                SELAMAT DATANG DI {NAMA_APP}            ")
        print("                Sistem Pengelolaan Kost 99            ")
        garis()
        print("1. Login Admin  2. Login Penghuni  0. Keluar")
        pil = input("Pilih jenis pengguna: ")
        if pil == "1":
            user = input("Username Admin: ")
            pw = input("Password: ")
            # [No.4] AND
            if user == "admin" and pw == "admin123":
                menu_admin()
            else:
                print("Login admin gagal!")
        elif pil == "2":
            user = input("ID Penghuni (P001): ").upper()
            pw = input("Password (No HP): ")
            penghuni = baca_csv(FILE_PENGHUNI)
            p = next((x for x in penghuni if x['ID_Penghuni'] == user and x['No_HP'] == pw), None)
            if p:
                menu_penghuni(p['ID_Penghuni'], p['Nama'])
            else:
                print("Login gagal! Cek ID & No HP.")
        elif pil == "0":
            print("Terima kasih sudah pakai KOSTERA!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()