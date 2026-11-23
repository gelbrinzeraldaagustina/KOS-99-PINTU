import pandas as pd
import os
from datetime import date

def siapin_file():
    try:
        pd.read_csv("data_USER.csv")
    except FileNotFoundError:
        user = {
            'Username' : ['admin', 'saffa', 'vale', 'zera', 'putri'],
            'Password' : ['admin123', 'saffa21', 'vale123', 'zera73', 'putri32'],
            'Nama' : ['Admini', 'Saffanah', 'Valerine', 'Zeralda', 'Putriii'],
            'Role' : ['admin', 'penghuni', 'penghuni', 'penghuni', 'penghuni'],
            'No_Kamar' : ['', 'K02', 'K03', 'K11', 'K12']
        }
        pd.DataFrame(user).to_csv("data_USER.csv", index=False)

    try:
        pd.read_csv("data_KAMAR.csv")
    except FileNotFoundError:
        kamar = {
            'No_Kamar' : ['K01', 'K02', 'K03', 'K11', 'K12', 'K13'],
            'Tipe' : ['Single', 'Single', 'Single', 'Double', 'Double', 'Double'],
            'Harga_Sewa' : [500000, 500000, 500000, 750000, 750000, 750000],
            'Status' : ['Kosong', 'Terisi', 'Terisi', 'Terisi', 'Terisi', 'Kosong'],
            'Penghuni' : ['', 'saffa', 'vale', 'zera', 'putri', '']
        }
        pd.DataFrame(kamar).to_csv("data_KAMAR.csv", index=False)

    try:
        pd.read_csv("data_TAGIHAN.csv")
    except FileNotFoundError:
        tagihan = {
            'ID_Tagihan' : ['T001', 'T002', 'T003', 'T004'],
            'Username' : ['saffa', 'zera', 'vale', 'putri'],
            'Bulan' : ['Oktober 2026', 'November 2026', 'Oktober 2026', 'November 2026'],
            'Jumlah' : [500000, 500000, 750000, 750000],
            'Tanggal_Jatuh_Tempo' : ['10-10-2026', '10-11-2026', '10-10-2026', '10-11-2026'],
            'Status' : ['Belum Lunas', 'Lunas', 'Belum Lunas', 'Lunas']
        }
        pd.DataFrame(tagihan).to_csv("data_TAGIHAN.csv", index=False)

    try:
        pd.read_csv("data_PENGADUAN.csv")
    except FileNotFoundError:
        pengaduan = {
            'ID_Pengaduan' : ['P001', 'P002'],
            'Nama' : ['Saffanah', 'Putriii'],
            'No_Kamar' : ['K01', 'K11'],
            'Fasilitas' : ['AC', 'Lampu'],
            'Deskripsi' : ['tidak dingin', 'mati'],
            'Tanggal' : ['21-11-2026', '02-10-2026'],
            'Status' : ['Diproses', 'Selesai']
        }
        pd.DataFrame(pengaduan).to_csv("data_PENGADUAN.csv", index=False)

    try:
        pd.read_csv("data_BARANG.csv")
    except FileNotFoundError:
        barang = {
            'No' : ['B001', 'B002', 'B003', 'B004', 'B005', 'B006', 'B007', 'B008', 'B009', 'B010'],
            'Nama_Barang' : ['Air Mineral 600ml', 'Mie Instan Goreng', 'Mie Instan Kuah', 'Deterjen Sachet', 'Air Galon',
                       'Kopi Sachet', 'Teh', 'Tisu', 'Sabun Mandi', 'Sampo Sachet'],
            'Harga' : [4000, 3500, 3500, 2000, 22000, 2000, 5000, 7000, 5000, 1500],
            'Stok' : [100, 50, 200, 150, 30, 200, 100, 80, 120, 90]
        }
        pd.DataFrame(barang).to_csv("data_BARANG.csv", index=False)

    try:
        pd.read_csv("data_PESANAN.csv")
    except FileNotFoundError:
            pesanan = {
                'ID_Pesanan' : ['P001', 'P002'],
                'Nama' : ['saffa', 'vale'],
                'No_Kamar' : ['K02', 'K11'],
                'Nama_Barang' : ['Detergen', 'Sabun'],
                'Harga' : [15000, 15000], 
                'Jumlah_Barang' : [1, 1],
                'Total' : [15000, 15000],
                'Tanggal' : ['01-10-2026', '01-11-2026'],
                'Status' : ['Diterima', 'Diproses']
            }
            pd.DataFrame(pesanan).to_csv("data_PESANAN.csv", index=False)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def garis():
    print("="*50)

def tampilkan_judul(teks):
    clear()
    garis()
    print('~~~ K O S T E R A ~~~'.center(50))
    print(teks.center(50))
    garis()

def enter_lanjut():
    input('\nKlik Enter untuk lanjut')

def rupiah(angka):
    return f'Rp{int(angka):,}'.replace(',', '.')

def bacakan(nama_file):
    data = pd.read_csv(nama_file, dtype=str)
    data = data.fillna('')
    return data

def simpan_data(data, nama_file):
    data.to_csv(nama_file, index=False)
    
def bikin_id(data, kolom, awalan):
    if len(data) == 0:
        nomor = 1
    else:
        angka_terakhir = data[kolom].str[len(awalan):].astype(int).max()
        nomor = angka_terakhir + 1
    return f'{awalan}{nomor:03d}'

def pilih_angka(jumlah):
    ketik = input('Pilih nomor (0 untuk batal): ')
    if not ketik.isdigit():
        print('Masukkan angka yang benar.')
        return -1
    nomor = int(ketik)
    if nomor == 0:
        return -1
    if nomor < 1 or nomor > jumlah:
        print('Nomor tidak tersedia.')
        return -1
    return nomor - 1

def tampilkan_data(data, kolom):
    if len(data) == 0:
        print('Belum ada data.')
        return
    print()
    print(' | '.join(kolom))
    garis()
    nomor = 1
    for i in range(len(data)):
        baris = data.iloc[i]
        isi = [str(nomor)]
        for nama in kolom:
            isi.append(str(baris[nama]))
        print(' | '.join(isi))
        nomor = nomor + 1

def masuk():
    tampilkan_judul('LOGIN')
    username = input('Username : ').strip()
    pw = input('Password : ').strip()
    user = bacakan('data_USER.csv')
    sesuai = user[(user['Username'] == username) & (user['Password'] == pw)]
    if len(sesuai) == 0:
        print('\nUsername atau password salah.')
        enter_lanjut()
        return

    akun = sesuai.iloc[0]
    if akun['Role'] == 'admin':
        menu_ADMIN(akun['Username'], akun['Nama'])
    else:
        menu_PENGHUNI(akun['Username'], akun['Nama'])

def daftar():
    clear()
    print('=== DAFTAR AKUN BARU - CALON PENGHUNI ===')

    user = bacakan('data_USER.csv')
    kamar = bacakan('data_KAMAR.csv')

    nama = input('Nama: ').strip()
    if nama == '':
        print('Nama tidak boleh kosong!')
        enter_lanjut()
        return

    while True:
        username = input('Username (tanpa spasi): ').strip()
        if username == '':
            print('Username tidak boleh kosong!')
            continue
        if ' ' in username:
            print('Username tidak boleh pakai spasi!')
            continue
        if username in list(user['Username']):
            print(f"Username '{username}' sudah dipakai! Coba yang lain.")
            continue
        break

    while True:
        password = input('Password (minimal 5 karakter): ').strip()
        if len(password) < 5:
            print(f'Password minimal 5 karakter ya!')
            continue
        break
    print()
    print('--- Pilih Kamar Yang Masih Kosong ---')
    kamar_kosong = kamar[kamar['Status'] == 'Kosong']
    if len(kamar_kosong) == 0:
        print('Maaf, semua kamar sudah penuh.')
        enter_lanjut()
        return

    tampilkan_data(kamar_kosong, ['No_Kamar', 'Tipe', 'Harga_Sewa', 'Status'])
    nomor = pilih_angka(len(kamar_kosong))
    if nomor == -1:
        print('Pendaftaran dibatalkan.')
        enter_lanjut()
        return

    kamar_dipilih = kamar_kosong.iloc[nomor]['No_Kamar']
    user_baru = {
        'Username': username,
        'Password': password,
        'Nama': nama,
        'No_Kamar': kamar_dipilih,
        'Role': 'penghuni',
    }
    user = pd.concat([user, pd.DataFrame([user_baru])], ignore_index=True)
    simpan_data(user, 'data_USER.csv')


    for i, k in kamar.iterrows():
        if k['No_Kamar'] == kamar_dipilih:
            kamar.loc[i, 'Status'] = 'Terisi'
            kamar.loc[i, 'Penghuni'] = username
            break
    simpan_data(kamar, 'data_KAMAR.csv')

    print()
    print('=== PENDAFTARAN BERHASIL! ===')
    print(f'Selamat datang, {nama}! Kamar kamu: {kamar_dipilih}')
    print('Silakan login di menu Masuk.')
    enter_lanjut()

def lihat_kamar_umum():
    kamar = bacakan('data_KAMAR.csv')
    clear()
    print('=== INFORMASI KAMAR ===')
    print('Kamar yang tersedia untuk calon penghuni:')

    kamar_kosong = kamar[kamar['Status'] == 'Kosong']

    if len(kamar_kosong) == 0:
        print('Maaf, saat ini semua kamar sudah terisi penuh.')
    else:
        tampilkan_data(kamar_kosong, ['No_Kamar', 'Tipe', 'Harga_Sewa', 'Status'])

    print()
    print('Tertarik? Silakan Daftar Akun Baru di menu utama.')
    enter_lanjut()   


# ========================= KELOLA KAMAR ==============================

def menu_Kamar():
    while True:
        tampilkan_judul('KELOLA KAMAR')
        kamar = bacakan('data_KAMAR.csv')
        tampilkan_data(kamar, ['No_Kamar', 'Tipe', 'Harga_Sewa', 'Status', 'Penghuni'])
        print('\n1. Tambahkan Kamar')
        print('2. Ubah/Kelola Data Kamar')
        print('3. Hapus Kamar')
        print('0. Kembali')
        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            nomor = input("Nomor kamar: ").strip()
            if nomor == '' or nomor in kamar ['No_Kamar'].tolist():
                print('Nomor kamar tidak tersedia atau sudah ada.')
            else:
                tipe = input('Tipe Kamar (Single/Double): ').strip().capitalize()
                try:
                    harga = int(input('Harga Sewa: '))
                    if tipe not in ['Single', 'Double'] or harga <= 0:
                        print('Tipe kamar harus Single atau Double dan harga tidak valid!')
                    else:
                        kamar.loc[len(kamar)] = [nomor, tipe, str(harga), 'Kosong', '']
                        simpan_data(kamar, 'data_KAMAR.csv')
                        print('Kamar baru berhasil ditambahkan')
                except ValueError:
                    print('Harga sewa harus berupa angka.')

        if pilihan == '2':
            nomor = pilih_angka(len(kamar))
            if nomor != -1:
                print('Kosongkan/enter saja jika tidak ingin mengubah')
                tipe = input('Tipe Kamar Baru: ').strip().capitalize()
                harga = input('Harga Sewa Baru: ').strip()
                if tipe:
                    if tipe in ['Single', 'Double']:
                        kamar.at[nomor, 'Tipe'] = tipe
                    else:
                        print('Tipe kamar tidak valid!')
                        enter_lanjut()
                        continue
                if harga:
                    if harga.isdigit() and int(harga) > 0:
                        kamar.at[nomor, 'Harga_Sewa'] = harga
                    else:
                        print('Harga sewa tidak valid!')
                        enter_lanjut()
                        continue
                    simpan_data(kamar, 'data_KAMAR.csv')
                    print('Data kamar berhasil diubah.')

        elif pilihan == '3':
            nomor = pilih_angka(len(kamar))
            if nomor != -1:
                if kamar.at[nomor, 'Status'] == 'Terisi':
                    print('Kamar sedang ditempati, tidak bisa dihapus.')
                else:
                    kamar = kamar.drop(nomor).reset_index(drop=True)
                    simpan_data(kamar, 'data_KAMAR.csv')
                    print('Kamar berhasil dihapus.')
                
        elif pilihan == '0':
             return
        else:
            print('Maaf pilihan menu tidak tersedia.')
        enter_lanjut()


def MenuData_Penghuni():
    while True:
        tampilkan_judul('KELOLA DATA PENGHUNI')
        user = bacakan('data_USER.csv')
        penghuni = user[user['Role'] == 'penghuni'].reset_index(drop=True)
        tampilkan_data(penghuni, ['Username', 'Nama', 'No_Kamar'])
        print('\n1. Cari Penghuni')
        print('2. Tambahkan Penghuni')
        print('3. Ubah Data Penghuni')
        print('4. Hapus Penghuni')
        print('0. Kembali')
        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            cari = input("Cari Nama / Username Penghuni: ").strip()
            user = bacakan('data_USER.csv')
            penghuni = user  
            tampilkan_data(penghuni, ['Username', 'Nama', 'Role', 'No_Kamar'])
            hasil = user[user['Nama'].str.contains(cari, case=False, na=False) | user['Username'].str.contains(cari, case=False, na=False)]
            if hasil.empty:
                print(f"Penghuni tidak teridentifikasi '{cari}'")
            else:
                print(f"Hasil pencarian '{cari}':")
                tampilkan_data(hasil, ['Username', 'Nama', 'No_Kamar'])

        elif pilihan == '2':
            kamar = bacakan('data_KAMAR.csv')
            kosong = kamar[kamar['Status'] == 'Kosong'].reset_index(drop=True)
            if len(kosong) == 0:
                print('Maaf kamar kosong tidak tersedia.')
                continue
            username = input('Username: ').strip()
            nama = input('Nama: ').strip()
            pw = input('Password (minimal 5 karakter): ').strip()
            tampilkan_data(kosong, ['No_Kamar', 'Tipe', 'Harga_Sewa'])
            nomor = pilih_angka(len(kosong))
            if nomor != -1:
                if username == '' or nama == '' or username in user['Username'].tolist():
                    print('Username sudah ada atau data kosong!')
                elif len(pw) < 5:
                    print('Password minimal 5 karakter!')
                else:
                    no_kamar = kosong.loc[nomor, 'No_Kamar']
                    user.loc[len(user)] = [username, pw, nama, 'penghuni', no_kamar]
                    simpan_data(user, 'data_USER.csv')
                    kamar.loc[kamar['No_Kamar'] == no_kamar, 'Status'] = 'Terisi'
                    simpan_data(kamar, 'data_KAMAR.csv')
                    print('Penghuni baru berhasil ditambahkan.')

        elif pilihan == '3':
            nomor = pilih_angka(len(penghuni))
            if nomor != -1:
                print('Kosongkan/enter saja jika tidak ingin mengubah')
                username = penghuni.loc[nomor, 'Username']
                indeks = user[user['Username'] == username].index[0]
                nama = input('Nama Baru: ').strip()
                pw = input('Password Baru: ').strip()
                if nama:
                    penghuni.loc[indeks, 'Nama'] = nama
                if pw:
                    if len(pw) >= 5:
                        penghuni.loc[indeks, 'Password'] = pw
                    else:
                        print('Password minimal 5 karakter!')
                        continue
                simpan_data(user, 'data_USER.csv')
                print('Data penghuni berhasil diubah.')

        elif pilihan == '4':
            nomor = pilih_angka(len(penghuni))
            if nomor != -1:
                username = penghuni.loc[nomor, 'Username']
                no_kamar = penghuni.loc[nomor, 'No_Kamar']
                user = user[user['Username'] != username].reset_index(drop=True)
                simpan_data(user, 'data_USER.csv')
                kamar = bacakan ('data_KAMAR.csv')
                kamar.loc[kamar['No_Kamar'] == no_kamar, 'Status'] = 'Kosong'
                simpan_data(kamar, 'data_KAMAR.csv')
                print('Data penghuni berhasil dihapus dan kamar dikosongan.')

        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia.')

        enter_lanjut()


# ========================= KELOLA TAGIHAN ==============================

def MenuTagihan_Admin():
    while True:
        tampilkan_judul('KELOLA TAGIHAN')
        tagihan = bacakan('data_TAGIHAN.csv')
        tampilkan_data(tagihan, ['ID_Tagihan', 'Username', 'Bulan', 'Jumlah', 'Tanggal_Jatuh_Tempo', 'Status'])
        print('\n1. Tambahkan Tagihan')
        print('2. Ubah Status Tagihan')
        print('3. Hapus Tagihan')
        print('0. Kembali')
        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            user = bacakan('data_USER.csv')
            penghuni = user[user['Role'] == 'penghuni']
            kamar = bacakan('data_KAMAR.csv')
            bulan = input('Bulan Tagihan (contoh: November 2026): ').strip()
            jumlah = input('Jumlah Tagihan: ').strip()
            jatuh_tempo = input('Tanggal Jatuh Tempo (dd-mm-yyyy): ').strip()
            try:
                date.strptime(jatuh_tempo, '%d-%m-%Y')
                if bulan == '':
                    raise ValueError
            except ValueError:
                print('Format tanggal/bulan tidak valid!')

            buat = 0
            for _, orang in penghuni.iterrows():
                sudah = tagihan[(tagihan['Username'] == orang['Username']) & (tagihan['Bulan'] == bulan)]
                if len(sudah) == 0:
                    data_kamar = kamar[kamar['No_Kamar'] == orang['No_Kamar']]
                    if len(data_kamar) > 0:
                        jumlah = data_kamar.iloc[0]['Harga_Sewa']
                        tagihan.loc[len(tagihan)] = [
                            bikin_id(tagihan, 'ID_Tagihan', 'T'), orang['Username'],
                            bulan, jumlah, jatuh_tempo, 'Belum Lunas'
                        ]
                        buat += 1
            simpan_data(tagihan, 'data_TAGIHAN.csv')
            print(f'{buat} tagihan baru berhasil dibuat untuk bulan {bulan}.')
        
        elif pilihan == '2':
            nomor = pilih_angka(len(tagihan))
            if nomor != -1:
                status_baru = input('Status Baru (Belum Lunas/Lunas): ').strip().capitalize()
                if status_baru not in ['Belum Lunas', 'Lunas']:
                    print('Status tidak valid!')
                else:
                    tagihan.loc[nomor, 'Status'] = status_baru
                    simpan_data(tagihan, 'data_TAGIHAN.csv')
                    print('Status tagihan berhasil diubah.')

        elif pilihan == '3':
            nomor = pilih_angka(len(tagihan))
            if nomor != -1:
                tagihan = tagihan.drop(nomor).reset_index(drop=True)
                simpan_data(tagihan, 'data_TAGIHAN.csv')
                print('Tagihan berhasil dihapus.')

        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia!')
        enter_lanjut()


def LihatTagihan_Penghuni(username):
    tampilkan_judul('TAGIHANKU')
    tagihan = bacakan('data_TAGIHAN.csv')
    punyaku = tagihan[tagihan['Username'] == username]
    if len(punyaku) == 0:
        print('Belum ada tagihan yang tersedia')
    else:
        tampilkan_data(punyaku, ['ID_Tagihan', 'Bulan', 'Jumlah', 'Tanggal_Jatuh_Tempo', 'Status'])
    enter_lanjut()


# ========================= LAYANAN PENGADUAN KOST  ==============================

def bikin_aduan(username, nama):
    tampilkan_judul('BUAT ADUAN FASILITAS KOST')
    user = bacakan('data_USER.csv')
    akun = user[user['Username'] == username].iloc[0]
    fasilitas = input('Fasilitas apa yang bermasalah? ').strip()
    deskripsi = input('Deskripsikan masalahnya: ').strip()
    if fasilitas == '' or deskripsi == '':
        print('Fasilitas dan deskripsi tidak boleh kosong!')
    else:
        data = bacakan('data_PENGADUAN.csv')
        data.loc[len(data)] = [
            bikin_id(data, 'ID_Pengaduan', 'P'), nama, 
            akun['No_Kamar'], fasilitas, deskripsi, date.today().strftime('%d-%m-%Y'), 'Diproses'
        ]
        simpan_data(data, 'data_PENGADUAN.csv')
        print('Aduan berhasil dibuat, menunggu konfirmasi admin.')
    enter_lanjut()


def MenuPengaduan_Admin():
    while True:
        tampilkan_judul('KELOLA PENGADUAN')
        aduan = bacakan('data_PENGADUAN.csv')
        tampilkan_data(aduan, ['ID_Pengaduan', 'Nama', 'No_Kamar', 'Fasilitas', 'Deskripsi', 'Status'])
        print('\n1. Perbarui Status Pengaduan')
        print('0. Kembali')
        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            nomor = pilih_angka(len(aduan))
            if nomor != -1:
                status_baru = input('Status Baru (Menunggu/Diproses/Selesai): ').strip().capitalize()
                if status_baru not in ['Menunggu', 'Diproses', 'Selesai']:
                    print('Status tidak valid!')
                else:
                    aduan.loc[nomor, 'Status'] = status_baru
                    simpan_data(aduan, 'data_PENGADUAN.csv')
                    print('Status pengaduan berhasil diperbarui.')

        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia!')
            enter_lanjut()


def pengaduanku(username):
    tampilkan_judul('PENGADUAN SAYA')
    aduan = bacakan('data_PENGADUAN.csv')
    punyaku = aduan[aduan['Nama'] == username]
    tampilkan_data(punyaku, ['ID_Pengaduan', 'Fasilitas', 'Deskripsi', 'Status'])
    enter_lanjut()


#   ========================= PEMESANAN BARANG  ==============================          

def MenuBarang_Admin():
    while True:
        tampilkan_judul('KATALOG BARANG')
        barang = bacakan('data_BARANG.csv')
        tampilkan_data(barang, ['No', 'Nama_Barang', 'Harga', 'Stok'])
        print('\n1. Tambahkan Barang')
        print('2. Ubah Data Barang')
        print('0. Kembali')
        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            nama = input('Nama Barang: ').strip()
            try:
                harga = int(input('Harga Barang: '))
                stok = int(input('Stok Barang: '))
                if nama == '' or harga <= 0 or  stok < 0:
                    print('Data tidak valid!')
                else:
                    barang.loc[len(barang)] = [bikin_id(barang, 'No', 'B'), nama, harga, stok]
                    simpan_data(barang, 'data_BARANG.csv')
                    print('Barang baru berhasil ditambahkan.')
            except ValueError:
                print('Harga dan stok harus berupa angka!')

        if pilihan == '2':
            nomor = pilih_angka(len(barang))
            if nomor != -1:
                print('Kosongkan/enter saja jika tidak ingin mengubah')
                nama = input('Nama Baru: ').strip()
                harga = input('Harga Baru: ').strip()
                stok = input('Stok Baru: ').strip()
                if nama:
                    barang.loc[nomor, 'Nama'] = nama
                if harga:
                    if harga.isdigit() and int(harga) > 0:
                        barang.loc[nomor, 'Harga'] = harga
                else:
                    print('Harga tidak valid! Harus angka dan lebih dari 0.')
                    enter_lanjut()
                    continue

                if stok:
                    if stok.isdigit(): 
                        barang.loc[nomor, 'Stok'] = stok
                    else:
                        print('Stok tidak valid! Harus angka.')
                        continue
                simpan_data(barang, 'data_BARANG.csv')
                print('Data barang berhasil diubah.')

        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia!')
        enter_lanjut()


def pesan_Barang(username, nama):
    tampilkan_judul('PESAN BARANG')
    barang = bacakan('data_BARANG.csv')
    tersedia = barang[pd.to_numeric(barang['Stok']) > 0].reset_index(drop=True)
    tampilkan_data(tersedia, ['Nama_Barang', 'Harga', 'Stok'])
    if len(tersedia) == 0:
        enter_lanjut()
        return
    nomor = pilih_angka(len(tersedia))
    
    if nomor == '1':
        return
    try:
        jumlah = int(input('Jumlah barang yang dipesan: '))
    except ValueError:
        print('Jumlah barang harus berupa angka!')
        enter_lanjut()
        return  
    stok = int(tersedia.loc[nomor, 'Stok'])
    if jumlah <= 0 or jumlah > stok:
        print('Jumlah barang tidak valid/melebihi stok!')
    else:
        harga = int(tersedia.loc[nomor, 'Harga'])
        total = harga * jumlah
        user = bacakan('data_USER.csv')
        akun = user[user['Username'] == username].iloc[0]
        pesanan = bacakan('data_PESANAN.csv')
        pesanan.loc[len(pesanan)] = [
            bikin_id(pesanan, 'ID_Pesanan', 'O'), nama, akun['No_Kamar'], tersedia.loc[nomor, 'Nama_Barang'], 
            str(harga), str(jumlah), str(total), date.today().strftime('%d-%m-%Y'), 'Menunggu Konfirmasi'
        ]
        simpan_data(pesanan, 'data_PESANAN.csv')
        print('\nPesanan berhasil dibuat!')
        print(f'Berikut total belanjaanmu ->> {rupiah(total)}')
        enter_lanjut()


def MenuPesanan_Admin():
    while True:
        tampilkan_judul('DAFTAR PESANAN')
        pesanan = bacakan('data_PESANAN.csv')
        tampilkan_data(pesanan, ['ID_Pesanan', 'Nama', 'No_Kamar', 'Nama_Barang', 'Harga', 'Jumlah_Barang', 'Total', 'Tanggal', 'Status'])
        print('\n1. Perbarui atau Konfirmasi Pesanan')
        print('0. Kembali')
        pilihan = input('Pilih Menu: ')

        if pilihan == '1':
            nomor = pilih_angka(len(pesanan))
            if nomor != -1:
                status_lama = pesanan.loc[nomor, 'Status']
                print('1. Diproses')
                print('2. Sedang Diantar')
                print('3. Selesai')
                status = input('Status baru: ').strip()

                if status == '1':
                    status_baru = 'Diproses'
                elif status == '2':
                    status_baru = 'Sedang Diantar'
                elif status == '3':
                    status_baru = 'Selesai'
                else:
                    print('Pilihan status tidak tersedia.')
                    continue

                if status_lama == 'Menunggu Konfirmasi' and status_baru == 'Diproses':
                    barang = bacakan('data_BARANG.csv')
                    nama_pesan = pesanan.loc[nomor, 'Nama_Barang']
                    jumlah = int(pesanan.loc[nomor, 'Jumlah_Barang'])
                    sesuai = barang[barang['Nama_Barang'] == nama_pesan]
                    if len(sesuai) == 0:
                        print('Barang tidak ditemukan.')
                        continue

                    stok_sekarang = int(sesuai.iloc[0]['Stok'])
                    if stok_sekarang < jumlah:
                        print('Stok tidak mencukupi. Pesanan belum dapat dikonfirmasi.')
                        continue

                    for i, b in barang.iterrows():
                        if b['Nama_Barang'] == nama_pesan:
                            barang.loc[i, 'Stok'] = stok_sekarang - jumlah
                            break

                    simpan_data(barang, 'data_BARANG.csv')
                    pesanan.loc[nomor, 'Status'] = 'Diproses'
                    simpan_data(pesanan, 'data_PESANAN.csv')
                    print('Pesanan dikonfirmasi dan stok telah dikurangi.')
                else:
                    pesanan.loc[nomor, 'Status'] = status_baru
                    simpan_data(pesanan, 'data_PESANAN.csv')
                    print('Status pesanan diperbarui.')
        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia.')
            enter_lanjut()


def pesananku(username):
    tampilkan_judul('PESANAN SAYA')
    pesanan = bacakan('data_PESANAN.csv')
    punyaku = pesanan[pesanan['Nama'] == username]
    tampilkan_data(punyaku, ['ID_Pesanan', 'Nama_Barang', 'Harga', 'Jumlah_Barang', 'Total', 'Tanggal', 'Status'])
    enter_lanjut()


#   ========================= MENU USER/PENGGUNA  ==============================

def menu_ADMIN(username, nama):
    while True:
        tampilkan_judul('MENU ADMIN')
        print(f'Admin: {nama}')
        print('\n1. Kelola Kamar')
        print('2. Kelola Data Penghuni')
        print('3. Kelola Tagihan')
        print('4. Kelola Pengaduan')
        print('5. Katalog Barang')
        print('6. Daftar Pesanan Penghuni')
        print('0. Logout')

        pilihan = input('\nPilih Menu: ')
        if pilihan == '1':
            menu_Kamar()
        elif pilihan == '2':
            MenuData_Penghuni()
        elif pilihan == '3':
            MenuTagihan_Admin()
        elif pilihan == '4':
            MenuPengaduan_Admin()
        elif pilihan == '5':
            MenuBarang_Admin()
        elif pilihan == '6':
            MenuPesanan_Admin()
        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia.')
            enter_lanjut()


def menu_PENGHUNI(username, nama):
    while True:
        tampilkan_judul('MENU PENGHUNI')
        print(f'Haloo {nama}')
        print('\n1. Informasi Kamar Kost')
        print('2. Informasi Tagihan')
        print('3. Buat Pengaduan Kost')
        print('4. Lihat Pengaduan Saya')
        print('5. Katalog dan Pemesanan Barang')
        print('6. Lihat Pesanan Saya')
        print('0. Logout')

        pilihan = input('\nPilih menu: ')
        if pilihan == '1':
            user = bacakan('data_USER.csv')
            akun = user[user['Username'] == username].iloc[0]
            kamar = bacakan('data_KAMAR.csv')
            data = kamar[kamar['No_Kamar'] == akun['No_Kamar']]
            tampilkan_judul('INFORMASI KAMAR')
            tampilkan_data(data, ['No_Kamar', 'Tipe', 'Harga_Sewa', 'Status'])
            enter_lanjut()
        elif pilihan == '2':
            LihatTagihan_Penghuni(username)
        elif pilihan == '3':
            bikin_aduan(username, nama)
        elif pilihan == '4':
            pengaduanku(username)
        elif pilihan == '5':
            pesan_Barang(username, nama)
        elif pilihan == '6':
            pesananku(username)
        elif pilihan == '0':
            return
        else:
            print('Maaf pilihan menu tidak tersedia.')
            enter_lanjut()


def tampilan_awal():
    siapin_file()
    while True:
        tampilkan_judul('SISTEM PENGELOLAAN KOST')
        print('\n1. Masuk (Login)')
        print('2. Daftar Akun Baru')
        print('3. Lihat Informasi Kamar (Tanpa Login)')
        print('0. Logout')
        pilihan = input('Pilih menu: ').strip()

        if pilihan == '1':
            masuk()
        elif pilihan == '2':
            daftar()
        elif pilihan == '3':
            lihat_kamar_umum()
        elif pilihan == '0':
            print('Terima kasih telah menggunakan KOSTERA...')
            break
        else:
            print('Maaf pilihan menu tidak tersedia.')
            enter_lanjut()

tampilan_awal()
