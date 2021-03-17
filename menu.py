import json,getpass,os
from datetime import datetime as dt
DataUser = list()
ItemUser = dict()
fileUser = 'checkout.json'

filename = 'login.json'
Datalogin = list()
Login = dict()

filedata = 'DataBarang.json'
databarang = list()
itemBarang = dict()

def clear():
    os.system('cls')

def kembaliToko():
    input('ENTER UNTUK KEMBALI... ')
    menuadmin()

def kembaliAkun():
    input('ENTER UNTUK KEMBALI...')
    menuAdminUtama()

def kembaliUser():
    input('ENTER UNTUK KEMBALI...')
    menuuser()
    
def login():
    clear()
    lihat()
    Lihatbarang1()
    datapelanggan()
    while True:
        print('''=====================================
========> SELAMAT DATANG DI <========
============> GY - SHOP <============
=====================================''')
        print('''Silahkan pilih mode login:
1. Admin Utama
2. Admin Toko
3. User
4. Logout
''')
        sebagai = input('Pilih mode sebagai : ')
        if sebagai == 'Admin Utama' or sebagai == '1':
            print('Login terlebih dahulu')
            login1()
            input('ENTER UNTUK MELANJUTKAN... ')
            menuAdminUtama()
        elif sebagai == 'Admin Toko' or sebagai == '2':
            print('Login terlebih dahulu')
            login1()
            input('ENTER UNTUK MELANJUTKAN... ')
            menuadmin()
        elif sebagai == 'User' or sebagai == '3':
            menuuser()
        elif sebagai == 'Logout' or sebagai == '4':
            print('''=====================================
===========> TERIMAKASIH <===========
=======> TELAH BERKUNJUNG DI <=======
============> GY - SHOP <============
=====================================''')
            break
    else:
        print('Mohon maaf perintah yang anda masukan salah')        

def menuAdminUtama():
    print('''
Silahkan pilih menu ke:
1. Check akun
2. Tambah akun
3. Hapus akun
4. Menu awal
''')
    milih = int(input('Pilih menu ke: '))
    if milih == 1:
        print(Datalogin)
        kembaliAkun()
    elif milih == 2:
        tambah()
        print('Akun telah ditambahkan')
        kembaliAkun()
    elif milih == 3:
        hapus()
        print('Akun telah dihapus')
        kembaliAkun()
    elif milih == 4:
        login()
    else:
        print('Menu tidak sesuai')
        menuAdminUtama
def hapus():
    clear() 
    hapusLogin = int(input('Hapus akun ke: '))
    hapusLogin -= 1
    del Datalogin[hapusLogin]

    with open(filename, 'w') as file:
        json.dump(Datalogin, file, indent=2)    

def tambah():
    clear()
    user = input('Username: ')
    pswd = input('Password: ')
    Login[user] = 'Username'
    Login[pswd] = 'Password'
    Datalogin.append(Login)

    with open(filename, 'w') as file:
        json.dump(Datalogin, file, indent=2)
def lihat():
    clear()
    with open(filename, 'r') as file:
        BacaLogin = json.load(file)
        for baris in BacaLogin:
            Datalogin.append(baris)
def login1():
    a = dict(Datalogin)
    percobaan = 1
    while percobaan <=5:
        user = input('Username: ')
        Password = getpass.getpass()
        if Password == a[user]:
            print('Login sukses')
            break
        percobaan +=1
    else:
        print('''Anda gagal login lebih dari 5x
Silahkan hubungi admin utama
''')
        
def menuadmin():
    print('''
Silahkan pilih menu ke:
1. Lihat barang
2. Tambah barang
3. Hapus barang
4. Update harga barang
5. Data pelanggan
6. Menu awal
''')
    pilih1 = int(input('Pilih menu ke: '))
    if pilih1 == 1:
        print('''
Berikut daftar barang yang tersedia:''')
        Lihatbarang()
        kembaliToko()
    elif pilih1 == 2:
        print('''
Silahkan tambahkan barang''')
        tambahBarang()
        print('Barang berhasil ditambahkan')
        kembaliToko()
    elif pilih1 == 3:
        print('''
Silahkan pilih barang yang dihapus''')
        hapusbarang()
        print('Barang berhasil dihapus')
        kembaliToko()
    elif pilih1 == 4:
        print('''
Silahkan update harga barang''')
        update_harga()
        kembaliToko()
    elif pilih1 == 5:
        print('''
Berikut data pelanggan:''')
        print(DataUser)
        kembaliToko()
    elif pilih1 == 6:
        login()
    else:
        print('Pilihan menu tidak sesuai')
        menuadmin()

def menuuser():
    print('''
Silahkan pilih menu:
1. Lihat barang G-Shop
2. Checkout barang
3. Menu awal
''')
    pilih = int(input('Pilih menu ke: '))
    if pilih == 1:
        print('Berikut daftar barang yang tersedia: ')
        Lihatbarang()
        kembaliUser()
    elif pilih == 2:
        Checkout()
        kembaliUser()
    elif pilih == 3:
        login()
    else:
        print('Pilihan menu tidak sesuai')
        menuuser()

def Lihatbarang():
    clear()
    with open(filedata, 'r') as file:
        baca = json.load(file)
        print('No Nama Barang \t\t Harga Barang')
        print('=====================================')
        for baris in baca:
            print(f"{baris['No']} {baris['Nama barang']} \t\t Rp {baris['Harga barang']}")

def Lihatbarang1():
    clear()
    with open(filedata, 'r') as file:
        baca = json.load(file)
        for baris in baca:
            databarang.append(baris)

def tambahBarang():
    clear()
#    Lihatbarang1()
    No = int(input('No urut barang: '))
    NamaBarang = input('Nama Barang(min 5, max 12 char): ')
    HargaBarang = int(input('Harga Barang: '))
    itemBarang['No'] = No
    itemBarang['Nama barang'] = NamaBarang
    itemBarang['Harga barang'] = HargaBarang
    databarang.append(itemBarang)
    with open(filedata, 'w') as file:
        json.dump(databarang, file, indent=2)
    with open(filedata, 'r') as file:
        baca = json.load(file)

def update_harga():
    clear()
#    Lihatbarang1()
    nobarang = int(input('Barang ke: '))
    nobarang -=1
    update = int(input('Harga barang: Rp '))
    databarang[nobarang]['Harga barang'] = update
    with open(filedata, 'w') as file:
        json.dump(databarang, file, indent=2)
    with open(filedata, 'r') as file:
        baca = json.load(file)

def hapusbarang():
    clear()
    hapus = int(input('Hapus barang ke: '))
    hapus -= 1
    del databarang[hapus]
    with open(filedata, 'w') as file:
        json.dump(databarang, file, indent=2)

def datapelanggan():
    clear()
    with open(fileUser, 'r') as file:
        baca = json.load(file)
        for baris in baca:
            DataUser.append(baris)
            
def Checkout():
    clear()
    Lihatbarang1()
    print('Isikan nama, alamat pemesanan, dan barang yang dipesan')
    namaBeli = input('Masukan nama: ')
    alamat = input('Masukan alamat: ')
    tanggal = dt.now().strftime('%Y-%m-%d')
    namabarang = input('Masukan nama barang: ')
    jumlahbarang = int(input('Masukan jumlah barang: '))
    nobarang = int(input('Masukan no barang ke: '))
    nobarang -= 1
    totalharga = jumlahbarang * databarang[nobarang]['Harga barang']
    print('''=====================================
=========== STRUK BELANJA ===========
============= GY - SHOP =============
=====================================
''')
    print('NAMA           : ' ,namaBeli)
    print('ALAMAT         : ' ,alamat)
    print('TANGGAL        : ' ,tanggal)
    print('NAMA BARANG    : ' ,namabarang)
    print('JUMLAH BARANG  : ' ,jumlahbarang)
    print('TOTAL HARGA    : Rp' ,totalharga)
    print('''
=====================================
============ TERIMAKASIH ============
======== TELAH BERBELANJA DI ========
============= GY - SHOP =============
=====================================
''')
    ItemUser['NAMA PELANGGAN'] = namaBeli
    ItemUser['ALAMAT PELANGGAN'] = alamat
    ItemUser['TANGGAL'] = tanggal
    ItemUser['NAMA BARANG'] = namabarang
    ItemUser['JUMLAH BARANG'] = jumlahbarang
    ItemUser['TOTAL HARGA'] = totalharga
    DataUser.append(ItemUser)
    with open(fileUser, 'w')as file:
        json.dump(DataUser,file,indent=2)
#Lihatbarang1()
#lihat()
#datapelanggan()
login()
#update_harga()