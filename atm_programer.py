import random
import datetime
from customer import Customer

atm = Customer (id)
while True:
    id = int (input ("Masukan PIN:  "))
    trial = 0
    while (id != int (atm.Pin_customer ()) and trial < 3):
        id = int (input ("PIN yang anda masukan salah, masukan kembali PIN anda :  "))
        trial += 1
        if trial == 3:
            print ("PIN eror, anda salah memasukkan 3 kali, harap menghubungi CS kami")
            exit ()
        else:
            break
    else:
        print ("Selamat Datang")
        print (" \n1. Cek Saldo \t 2. Debet \t 3. Simpan \t 4. Ganti PIN \t 5. Keluar")
        select_menu = int (input ("Silahkan Pilih Menu:  "))
        if select_menu == 1:
            print ("Saldo sekarang adalah: Rp. "+ str(atm.Saldo_awal()) + "\n")
        elif select_menu == 2:
            nominal = float (input ("Masukan nominal yang ingin anda ambil:  "))
            verifikasi  = input ("Konfirmasi: Apakah anda yakin ingin debet dengan nominal berikut? y/n  " + str(nominal) + " ")
            if verifikasi == "y":
                print ("Saldo awal anda adalah: Rp. " + str (atm.Saldo_awal()))
                if nominal < atm.Saldo_awal():
                    atm.debit(nominal)
                    print ("Transaksi Debet berhasil !")
                    print ("Saldo sekarang anda adalah Rp " + str(atm.Saldo_awal()) + " ")
                else:
                    print ("Saldo anda tidak mencukupi untuk melakukan debet")
                    print ("Silahkan lakukan penambahan saldo")
            else:
                break            
        elif select_menu == 3:
            nominal_simpan = int (input ("Masukan nominal yang ingin anda simpan:  "))
            verifikasi = input ("Apakah anda yakin? y/n  " + str (nominal_simpan) + " ")
            if verifikasi == "y":
                atm.simpan(nominal_simpan)
                print ("Saldo anda sekarang adalah : Rp. " + str(atm.Saldo_awal()))
            else:
                break
        elif select_menu == 4:
            Pin_awal = int (input ("Masukan PIN anda: "))
            trial = 0
            if Pin_awal != atm.Pin_customer():
                Pin_awal2 = int(input ("PIN yang anda masukan salah, harap masukan kembali: "))
                trial += 1
                if trial == 3:
                    print ("PIN eror, anda salah memasukkan 3 kali, harap menghubungi CS kami")
                    exit ()
                else:
                    break
            else:
                Pin_baru = int (input ("Masukan PIN baru anda: "))
                verify_newpin = int (input ("Masukan kembali PIN baru anda: "))
                if verify_newpin == Pin_baru:
                    print ("Selamat PIN anda telah berubah")
                else:
                    print ("Maaf PIN anda tidak cocok")
                    
        elif select_menu == 5:
            print("Resi transaksi akan dicetak \n Harap simpan resi sebagai tanda bukti anda")
            print ("No. Record: ", random.randint (100000, 1000000))
            print ("Tanggal transaksi: ", datetime.datetime.now ())
            print ("Saldo terakhir anda adlah : Rp. " + str(atm.Saldo_awal()))
            print ("Terimakasih telah menggunakan ATM KIA")
            exit ()
        else:
            print ("Maaf menu tidak tersedia")