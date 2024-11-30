# Data Perlengkapan Siaga
barang = [
    {
        'Nama Barang': 'APAR',
        'Stok': 5,
        'Kategori': 'Pemadam Kebakaran',
        'Harga Barang': 200000,
        'Total Biaya': 1000000,
        'Prioritas': 1
    },
    {
        'Nama Barang': 'Kotak P3K',
        'Stok': 10,
        'Kategori': 'Pertolongan Pertama',
        'Harga Barang': 85000,
        'Total Biaya': 850000,
        'Prioritas': 2
    },
    {
        'Nama Barang': 'Analgesik',
        'Stok': 10,
        'Kategori': 'Obat Siaga',
        'Harga Barang': 150000,
        'Total Biaya': 1700000,
        'Prioritas': 3
    },
]

# Data Admin
admins = {}

# Fungsi Validasi Kategori
def validasi_kategori(kategori):
    kategori_terdaftar = {item['Kategori'] for item in barang}
    return kategori in kategori_terdaftar

# Fungsi Menu Utama
def menu():
    while True:
        print()
        print('===== SISTEM PERLENGKAPAN SIAGA =====')
        print('1. Registrasi Admin')
        print('2. Login Admin')
        print('3. Keluar')

        code = input('Masukkan pilihan: ')
        if code == '1':
            registrasi()
        elif code == '2':
            if login():
                admin_menu()
        elif code == '3':
            print('Terima kasih telah menggunakan Sistem Perlengkapan Siaga.')
            break
        else:
            print('Pilihan tidak tersedia pada menu.')


# Fungsi Registrasi Admin
def registrasi():
    while True:
        print("***************************************************")
        print("=== SELAMAT DATANG DI SISTEM PERLENGKAPAN SIAGA ===")
        print("***************************************************")
        print("================  REGISTRASI ADMIN  ===============")
        username = input("Masukkan ID Admin baru: ")
        if username in admins:
            print("Username sudah terdaftar. Silakan coba username lain.")
        else:
            password = input("Masukkan Password baru: ")
            admins[username] = password
            print("Registrasi berhasil! Silakan login.")
            break

# Fungsi Login Admin
def login():
    if not admins :
        print("anda belum memiliki akun coba lah membuat akun terlebih dahulu")
        return False
    
    while True:
        jumlah_kesalahan = 0
        while jumlah_kesalahan < 3:
            print("***************************************************")
            print("===               Login Admin               ===")
            print("***************************************************")
            username_input = input("Masukkan ID Admin: ")
            password_input = input("Masukkan Password: ")

            if username_input in admins and admins[username_input] == password_input:
                print("Selamat datang, admin!")
                return True
            else:
                print("Username atau password salah. Coba lagi.")
                jumlah_kesalahan += 1
        if jumlah_kesalahan == 3:
            print("Anda sudah mencoba login 3 kali. Program berhenti.")
            exit()


# Fungsi Menu Admin
def admin_menu():
    while True:
        print()
        print('===== MENU ADMIN =====')
        print('1. Tambah Data Barang')
        print('2. Edit Data Barang')
        print('3. Hapus Data Barang')
        print('4. Tampilkan Data Barang')
        print('5. Cari Barang Berdasarkan Kategori')
        print('6. Keluar')

        code = input('Masukkan pilihan: ')
        if code == '1':
            tambah()
        elif code == '2':
            edit()
        elif code == '3':
            hapus()
        elif code == '4':
            tampil()
        elif code == '5':
            cari_kategori()
        elif code == '6':
            break
        else:
            print('Pilihan tidak tersedia pada menu.')

# Fungsi Tambah Barang
def tambah():
    print()
    print('========= TAMBAH DATA BARANG =========')
    if not barang:
        print('data masih kosong')
        return
    kategori = input('Masukkan kategori barang (contoh: Pemadam Kebakaran, Pertolongan Pertama, Obat Siaga): ')

    if not validasi_kategori(kategori):
        print(f'Kategori "{kategori}" tidak ditemukan. Tambahkan kategori yang sesuai dengan data.')
        return

    nama = input('Masukkan nama barang: ')
    stok = int(input('Masukkan stok barang: '))
    harga_barang = int(input('Harga Barang: '))
    total_pembelian_seluruh_barang = harga_barang * stok
    prioritas = int(input('Masukkan prioritas barang (angka, semakin kecil semakin tinggi): '))
    barang.append({
        'Nama Barang': nama,
        'Stok': stok,
        'Kategori': kategori,
        'Harga Barang': harga_barang,
        'Total Biaya': total_pembelian_seluruh_barang,
        'Prioritas': prioritas
    })
    print('Data barang berhasil ditambahkan.')

# Fungsi Edit Barang
def edit():
    print()
    print('========= EDIT DATA BARANG =========')
    if not barang:
        print('Data masih kosong.')
        return
    
    kategori = input('Masukkan kategori barang yang ingin diedit: ')

    if not validasi_kategori.lower()(kategori):
        print(f'Kategori "{kategori}" tidak ditemukan.')
        return

    hasil = [item for item in barang if item['Kategori'].lower() == kategori.lower()]
    if not hasil:
        print(f'Tidak ada barang dalam kategori "{kategori}".')
        return

    # Menampilkan daftar barang yang sesuai kategori
    for idx, item in enumerate(hasil, 1):
        print(f'{idx}. {item["Nama Barang"]}, Stok: {item["Stok"]}, Harga: {item["Harga Barang"]}')

    # Validasi input index
    index = input('Masukkan index barang yang ingin diedit: ')
    if not index.isdigit():
        print('Index harus berupa angka.')
        return

    index = int(index)
    if not (1 <= index <= len(hasil)):
        print('Index tidak valid.')
        return

    barang_edit = hasil[index - 1]

    # Menu pilihan edit
    print('1. Edit Nama Barang')
    print('2. Edit Stok')
    print('3. Ganti Harga Barang')
    print('4. Edit Prioritas')

    pilihan = input('Pilih action: ')
    if pilihan == '1':
        barang_edit['Nama Barang'] = input('Masukkan nama barang baru: ')
    elif pilihan == '2':
        stok_baru = input('Masukkan stok barang baru: ')
        if stok_baru.isdigit():
            barang_edit['Stok'] = int(stok_baru)
            barang_edit['Total Biaya'] = barang_edit['Harga Barang'] * barang_edit['Stok']
        else:
            print('Stok harus berupa angka.')
            return
    elif pilihan == '3':
        harga_baru = input('Masukkan harga barang baru: ')
        if harga_baru.isdigit():
            barang_edit['Harga Barang'] = int(harga_baru)
            barang_edit['Total Biaya'] = barang_edit['Harga Barang'] * barang_edit['Stok']
        else:
            print('Harga harus berupa angka.')
            return
    elif pilihan == '4':
        prioritas_baru = input('Masukkan prioritas baru (angka): ')
        if prioritas_baru.isdigit():
            barang_edit['Prioritas'] = int(prioritas_baru)
        else:
            print('Prioritas harus berupa angka.')
            return
    else:
        print('Pilihan tidak valid.')
        return

    print('Data barang berhasil diperbarui.')
# Fungsi Hapus Barang
def hapus():
    print()
    print('========= HAPUS DATA BARANG =========')
    if not barang:
        print('Data masih kosong.')
        return

    kategori = input('Masukkan kategori barang yang ingin dihapus: ')

    if not validasi_kategori(kategori):
        print(f'Kategori "{kategori}" tidak ditemukan.')
        return

    hasil = [item for item in barang if item['Kategori'].lower() == kategori.lower()]
    if not hasil:
        print(f'Tidak ada barang dalam kategori "{kategori}".')
        return

    for idx, item in enumerate(hasil, 1):
        print(f'{idx}. {item["Nama Barang"]}, Stok: {item["Stok"]}, Harga: {item["Harga Barang"]}')

    index = input('Masukkan index barang yang ingin dihapus: ')
    if not index.isdigit() or not (1 <= int(index) <= len(hasil)):
        print('Index tidak valid.')
        return

    barang_hapus = hasil[int(index) - 1]
    barang.remove(barang_hapus)
    print(f'Barang "{barang_hapus["Nama Barang"]}" berhasil dihapus.')

# Fungsi Tampilkan Barang
def tampil():
    print()
    print('=== DATA PERLENGKAPAN SIAGA ===')
    if len(barang) <= 0:
        print('Data masih kosong.')
    else:
        barang_sorted = sorted(barang, key=lambda x: x['Prioritas'])
        for idx, item in enumerate(barang_sorted, 1):
            print(f'{idx}. Nama: {item["Nama Barang"]}, Stok: {item["Stok"]}, '
                  f'Kategori: {item["Kategori"]}, Harga: {item["Harga Barang"]}, '
                  f'Total Biaya: {item["Total Biaya"]}, Prioritas: {item["Prioritas"]}')
    print('==============================================')

# cari kategori
def cari_kategori():
    print('\n===== CARI BARANG BERDASARKAN KATEGORI =====')
    print(' Pemadam Kebakaran')
    print(' Pertolongan Pertama')
    print(' Obat Siaga')
    if not barang:
        print('data masih kosong')
    kategori = input('Masukkan kategori yang ingin dicari: ').strip()
    hasil = [item for item in barang if item['Kategori'].lower() == kategori.lower()]
    if hasil:
        print(f'Barang dalam kategori "{kategori}":')
        for idx, item in enumerate(hasil, 1):
            print(f'{idx}. {item["Nama Barang"]}, Stok: {item["Stok"]}, Harga: {item["Harga Barang"]}')
    else:
        print(f'Tidak ada barang dalam kategori "{kategori}".')


# Menjalankan Program
menu()