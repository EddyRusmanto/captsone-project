#dictionary yang berisi database awal
dataMahasiswa = [{
        'NIM' : '001',
        'Nama' : 'Eddy',
        'Jurusan' : 'Management',
        'Tahun' : '2019',
        'Nilai' : '3.5',
    },
    {
        'NIM' : '002',
        'Nama' : 'Angga',
        'Jurusan' : 'Management',
        'Tahun' : '2019',
        'Nilai' : '3.8',
    },
    {
        'NIM' : '003',
        'Nama' : 'Viana',
        'Jurusan' : 'Management',
        'Tahun' : '2019',
        'Nilai' : '3.75',
    }]
def lihatFakultas(nilai): #function ini digunakan untuk menampilkan data dalam dictionary dan digunakan pada sub menu "Data Seluruh Mahasiswa FEUP"
    print('Index\t | \tNIM\t | \tNama\t | \tJurusan\t\t | \tTahun\t | \tNilai')
    for i in range(len(nilai)):
        print(f"{i}\t | \t{nilai[i]['NIM']}\t | \t{nilai[i]['Nama']}\t | \t{nilai[i]['Jurusan']}\t | \t{nilai[i]['Tahun']}\t | \t{nilai[i]['Nilai']}\t")
    return
def lihatID(id_match): #Function ini digunakan untuk mencari data mahasiswa dan untuk sub menu "Cari Data Mahasiwa FEUP"
    print('\nIndex\t | \tNIM\t | \tNama\t | \tJurusan\t\t | \tTahun\t | \tNilai')
    for i in range(len(dataMahasiswa)):
        if id_match == dataMahasiswa[i]['NIM']:
            print(f"{i}\t | \t{dataMahasiswa[i]['NIM']}\t | \t{dataMahasiswa[i]['Nama']}\t | \t{dataMahasiswa[i]['Jurusan']}\t | \t{dataMahasiswa[i]['Tahun']}\t | \t{dataMahasiswa[i]['Nilai']}\t")
            break
    else:
        print('\nData Mahasiswa Tidak Ada')
    return id_match
def update(updateID, dataMahasiswa): #function ini digunakan untuk melakukan perubahan data dan digunakan untuk menu "Ubah Data Mahasiswa"
    while True:
        for i in range(len(dataMahasiswa)):
            if updateID == dataMahasiswa[i]['NIM']:
                nim = input('\nMasukan NIM Baru\t\t\t: ')
                nama = input('Masukan Nama Baru\t\t\t: ')
                jurusan = input('Masukan Jurusan Baru Mahasiswa\t\t: ')
                while True:
                    try:
                        tahun = int(input('Masukan Tahun Masuk Baru Mahasiswa\t: '))
                        break
                    except ValueError:
                        print("NOTE: Input harus berupa angka. Silakan masukkan kembali.\n") 
                while True:
                    try:
                        nilai = float(input('Masukan Nilai Baru Mahasiswa\t\t: '))
                        break
                    except ValueError:
                        print("NOTE: Input harus berupa angka dengan format desimal. Silakan masukkan kembali(Contoh: 3.80).\n")
                konfirmasiUpdate = str(input('\nApakah Anda Yakin Ingin Mengubah Data (y/n)\t: ')).lower()
                while True:
                    if konfirmasiUpdate == 'y':
                        dataMahasiswa [i]['NIM'] = nim
                        dataMahasiswa [i]['Nama'] = nama
                        dataMahasiswa [i]['Jurusa'] =jurusan
                        dataMahasiswa [i]['Tahunn'] = tahun
                        dataMahasiswa [i]['Nilai'] = nilai
                        print('\nData Telah Terupdate\n')
                        lihatFakultas(dataMahasiswa)
                        break
                    elif konfirmasiUpdate == 'n':
                        print('\nData Mahasiswa Tidak Tersimpan\n')
                        lihatFakultas(dataMahasiswa)
                        break
                    else:
                        print('\nInput Salah')
                        konfirmasiUpdate = str(input('\nApakah Anda Yakin Ingin Mengubah Data (y/n)\t: ')).lower()
        return

def header():
    header1 = ' Database Fakultas Ekonomi Universitas Pancasila (FEUP) '
    print('\n')
    print(header1.center(164, '='))
def menuUtama():
    header()
    print('''
    Menu Utama \n
    Silahkan Pilih Menu Dibawah Ini:\n 
    [1]. Lihat Data Mahasiswa FEUP
    [2]. Tambah Data Mahasiswa FEUP
    [3]. Ubah Data Mahasiswa FEUP
    [4]. Hapus Data Mahasiswa FEUP
    [5]. Keluar
    ''')
def menu1():
    header()
    print('''
     Lihat Data Mahasiswa FEUP \n
     Silahkan Pilih Menu Dibawah Ini:\n
     [1]. Lihat Seluruh Data Mahasiswa FEUP
     [2]. Cari Data Mahasiswa FEUP
     [0]. Kembali ke Menu Utama
    ''')
def menu2():
    header()
    print('''
    Tambah Data Mahasiswa FEUP \n 
    Silahkan Pilih Menu Dibawah Ini:\n
    [1]. Masukan Data Mahasiswa Baru FEUP
    [0]. Kembali ke Menu Utama
    ''')
def menu3():
    header()
    print('''
    Ubah Data Mahasiswa UP \n
    Silahkan Pilih Menu Dibawah Ini:\n
    [1]. Masukan Data Mahasiswa FEUP yang Ingin di Ubah
    [0]. Kembali ke Menu Utama
    ''')
def menu4():
    header()
    print('''
    Hapus Data Mahasiswa FEUP \n
    Silahkan Pilih Menu Dibawah Ini:\n 
    [1]. Hapus Data Mahasiswa
    [0]. Kembali ke Menu Utama
    ''')
def closeProgram():
    closeProgram1 = ' SELAMAT TINGGAL = PROGRAM DITUTUP '
    print('\n')
    print(closeProgram1.center(164, '='))
    print('\n')

# Program
def menu(inputOption):
    while True:
# Menu 1 Read
        if inputOption == '1':
            menu1()
            userPilihMenu1 = input('Masukan Pilihan Anda\t: ')
            if userPilihMenu1 == '1':
                print('\nData Seluruh Mahasiswa FEUP\n')
                lihatFakultas(dataMahasiswa)
            elif userPilihMenu1 == '2':
                lihatID(input('\nMasukan NIM\t: '))
            elif userPilihMenu1 == '0':
                menuUtama()
                menu(input('\nPilih Menu Utama Kembali\t: '))
            else:
                print('\nMenu yang Anda Pilih Salah')
                menu('1')
# Menu 2 Create
        elif inputOption == '2':
            global nim, nama, jurusan, tahun, nilai
            menu2()
            userPilihMenu2 = input('Masukan Pilihan Anda\t: ')
            while True:
                if userPilihMenu2 == '1':
                    def konfrimasi(): 
                        print('\nData Mahasiswa Baru')
                        print('\nNIM \t:', nim, '\nNama \t:', nama, '\nJurusan\t:', jurusan, '\nTahun \t:', tahun, '\nNilai \t:', nilai)
                        while True:
                            yaAtauTidak = input('\nYakin Ingin Memasukan Data (y/n)\t: ').lower()
                            if yaAtauTidak == 'y':
                                dataMahasiswa.append(studentData_dictionary)
                                print('\nData Baru Telah Tersimpan')
                                menu('2')
                            elif yaAtauTidak == 'n':
                                print('\nData Baru Tidak Jadi Tersimpan')
                                menu('2')
                            else:
                                print('\nMenu Konfirmasi yang Anda Pilih Salah')
                    nim = input('\nMasukan NIM\t: ')
                    dataMahasiswaNim = [i.setdefault('NIM') for i in dataMahasiswa]
                    for i in dataMahasiswaNim:
                        while True:
                            if nim != i:
                                break
                            else:
                                nim = input('\nData NIM Sudah Ada \n\nMasukan NIM Kembali: ')
                    nama = input('Masukan Nama\t: ')
                    jurusan = input('Masukan Jurusan\t: ')
                    while True:
                        try:
                            tahun = int(input('Masukan Tahun\t: '))
                            break
                        except ValueError:
                            print("NOTE: Input harus berupa angka. Silakan masukkan kembali.\n") 
                    while True:
                        try:
                            nilai = float(input('Masukan Nilai\t: '))
                            break
                        except ValueError:
                            print("NOTE: Input harus berupa angka dengan format desimal. Silakan masukkan kembali(Contoh: 3.80).\n") 
                    studentData_dictionary = {'NIM' : nim, 'Nama' : nama, 'Jurusan' : jurusan, 'Tahun' : tahun, 'Nilai' : nilai}
                    konfrimasi()
                elif userPilihMenu2 == '0':
                    menuUtama()
                    menu(input('\nPilih Menu Utama Kembali\t: '))
                else:
                    print('\nMenu yang Anda Pilih Salah')
                    menu('2')   
# Menu 3 Update       
        elif inputOption == '3':
            menu3()
            userPilihMenu3 = input('Masukan Pilihan Anda\t: ')
            if userPilihMenu3 == '1':
                print('\n')
                lihatFakultas(dataMahasiswa)
                updateID = lihatID(input('\nMasukan NIM Mahasiswa FEUP yang Ingin Diubah Datanya\t: '))
                update(updateID, dataMahasiswa)
            elif userPilihMenu3 == '0':
                menuUtama()
                menu(input('\nPilih Menu Utama Kembali\t: '))
            else:
                print('\nMenu yang Anda Pilih Salah')
                menu('3')
# Menu 4 Delete
        elif inputOption == '4':
            menu4()
            userPilihMenu4 = input('Masukan Pilihan Anda\t: ')
            if userPilihMenu4 == '1':
                lihatFakultas(dataMahasiswa)
                hapusNIM = input('\nMasukan NIM Mahasiwa FEUP yang Ingin Dihapus\t: ')
                def konfrimasi(): 
                    while True:
                        lihatID(hapusNIM)
                        yaAtauTidak = input('\nYakin Ingin Menghapus Data (y/n)\t: ').lower()
                        if yaAtauTidak == 'y':
                            dataMahasiswa.remove(i)
                            print('\nData Dihapus')
                            menu('4')
                        elif yaAtauTidak == 'n':
                            print('\nData Tidak Jadi Dihapus')
                            menu('4')
                        else:
                            print('\nMenu Konfirmasi yang Anda Pilih Salah')
                for i in dataMahasiswa:
                    if hapusNIM == i['NIM']:
                        konfrimasi()
                else:
                    print('\nData Tidak Ada')
            elif userPilihMenu4 == '0':
                menuUtama()
                menu(input('\nPilih Menu Utama Kembali\t: '))
            else:
                print('\nMenu yang Anda Pilih Salah')
                menu('4')
# Menu 5 Keluar       
        elif inputOption == '5':
            keluar = input('\nApakah Anda Yakin Ingin Keluar? (y/n)\t: ').lower()
            while True:
                if keluar == 'y':
                    closeProgram()
                    exit()
                elif keluar == 'n':
                    menuUtama()
                    menu(input('\nPilih Menu Utama Kembali: '))
                else:
                    keluar = input('\nInput Konfirmasi yang Anda Masukan Salah\n\nApakah Anda Yakin Ingin Keluar? (y/n)\t: ').lower()
        else:
            menuUtama()
            menu(input('Menu Utama yang Anda Pilih Salah\n\nSilahkan Pilih Menu Utama Kembali\t:'))
            continue
menuUtama()
menu(input('Pilih Menu Utama\t: '))