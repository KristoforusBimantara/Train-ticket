import uuid

pegawai = [
            {"ID": 123, "Nama": "Hudya", "Password": 123},
            {"ID": 333, "Nama": "Bima", "Password": 223}
          ]

tiket = [
            {'ID': 1, 'Berangkat': 'Jakarta', 'Tujuan': 'Yogyakarta', 'Harga': 250000},
            {'ID': 2,'Berangkat': 'Jakarta', 'Tujuan': 'Malang', 'Harga': 350000}
        ]


def lihatTiket():
    """
    Fungsi ini untuk melihat data tiket yang tersedia
    """
    i = 0
    for x in  tiket:
        i += 1
        print('-'*14+'Tiket'+' '+str(i)+'-'*15)
        print('ID:',x['ID'])
        print('Berangkat:',x['Berangkat'])
        print('Tujuan:',x['Tujuan'])
        print('Harga:',x['Harga'])


def tambahTiket():
    """
    Fungsi ini untuk menambahkan data tiket oleh user dengan memasukkan
    beberapa data yang dibutuhkan.
    """
    a = str(uuid.uuid4())
    b = input('Isikan kota asal :')
    c = input('Isikan kota tujuan perjalanan :')
    d = int(input('Isikan harga tiket :'))
    tiket.append({'ID': a,'Berangkat': b, 'Tujuan': c, 'Harga': d})
    #return True


def beliTiket():
    """
    Fungsi ini untuk membeli tiket dan menampilkan harga yang harus dibayar
    user akan memasukan data yang diminta untuk proses pembelian.
    """
    Nama_Pembeli = input("Isikan Nama Pembeli...")
    Nomor_KTP = int(input('Isikan Nomor KTP Pembeli :'))
    ID_Tiket = input('Isikan ID Tiket yang dibeli :')
    if len(ID_Tiket) == 1 :
        ID = int(ID_Tiket)
    else :
        ID = ID_Tiket
    Jumlah_Tiket = int(input('Isikan Jumlah Tiket yang dibeli :'))
    print('-'*13+'Pembayaran'+'-'*13)
    for x in tiket :
        if ID == x['ID']:
            totalHarga = Jumlah_Tiket * x['Harga']
            print('Nama Pembeli:',Nama_Pembeli)
            print('Nomor KTP:',Nomor_KTP)
            print('ID Tiket yang dibeli:',ID)
            print('Jumlah Tiket:',Jumlah_Tiket)
            print('Total Harga yang harus dibayarkan:',totalHarga)
            print('Terimakasih')
            break
    if ID != x['ID']:
        print('Tiket tidak tersedia')


while True:
    kondisi = True
    Id = int(input("Masukkan ID :"))
    pasw = int(input("Masukkan Password :"))
#--------------------------------------------------#
    if Id == 0 and pasw == 0:
        print('Sistem Penjualan OFF')
        break
#--------------------------------------------------#
    for k in pegawai:
        if Id == k['ID'] and pasw == k['Password']:
            kondisi = False
            print('-'*11+'Selamat Datang Mas'+' '+k['Nama']+'-'*11)
            break
    if Id != k['ID'] and pasw != k['Password'] :
        print('ID dan Password anda SALAH BOSSS')
#--------------------------------------------------#
    if kondisi == False:
        while True:
            print('-'*16+'MENU'+'-'*16)
            print('1. Lihat Data Tiket')
            print('2. Menambahkan Data Tiket')
            print('3. Membeli Tiket')
            print('4. Keluar Dari Menu')
            print('Silahkan pilih angka')
            pilih = int(input('Masukkan angka yang dipilih :'))
            if pilih == 1:
                lihatTiket()
                continue
            elif pilih == 2:
                tambahTiket()
                continue
            elif pilih == 3:
                beliTiket()
                continue
            elif pilih == 4:
                print('-'*35)
                print('Terimakasih...')
                break
            else:
                print('Angka salah')
                continue
            break
