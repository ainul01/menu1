import json

def load_pesanan():

    file = open("listpesanNina.txt", "r") #membuka file data-pesan.txt

    data_pesan = json.load(file)

    return data_pesan

def tulis_pesan(data):

    with open("listpesanNina.txt", "w") as new_file: 

        json.dump(data,new_file)

def order():

    print("-"*30)

    nama = input("Masukan nama : ")

    pilih_makanan = int(input("Pilih makanan : "))

    jml_makan = int(input("Jumlah makanan : "))

    pilih_minuman = int(input("Pilih minuman : "))

    jml_minum = int(input("Jumlah minuman : "))

    

    if(pilih_makanan <= no and pilih_minuman <= no):

      makanan_selected = makanan[pilih_makanan-1]

      minuman_selected = minuman[pilih_minuman-1]

      total = (makanan_selected['harga']*jml_makan)+(minuman_selected['harga']*jml_minum)

# list berisi dat pesanan dari user berupa dictionary di dalam list

      list_pesanan = [

        {"makanan":makanan_selected["nama"],

        "jumlah_makanan":jml_makan,

        "minuman":minuman_selected["nama"],

        "jumlah_minuman":jml_minum,

        "total":total,

        "keterangan":""}

        ]

      

# membuat data dict pemesanan yang nanti disimpan dalam file

      data_pesan = load_pesanan()

      data_pesan[nama] = list_pesanan #menambahkan data baru ke dalam dictionary yaitu data pesan

#membuka dan menulis ulang file data-pesan.txt

      tulis_pesan(data_pesan)

      print("-"*30)

      print("Pesanan Berhasill!!!n")

      print("Nama :", nama)

      print(f"Makanan yang dipilih : {makanan_selected['nama']} ({makanan_selected['harga']}) ")

      print(f"minuman yang dipilih : {minuman_selected['nama']} ({minuman_selected['harga']}) ")

      print("jumlah makanan :", jml_makan)

      print("jumlah minuman :", jml_minum)

      print(f"Total : Rp.{total}")

      print("-"*30)

    else:

      print("Masukan Pilihan dengan benar")

    

print("JANGAN MAKAN DISINI")

while True:

    print("-"*30)

    print("Pilih : \n1. Order \n2. Bayar(belum dibuat)")

    print("-"*30)

    inp_menu_program = int(input("Masukan Pilihan : ")) #input pilih menu

    if inp_menu_program == 1: #jika input pilih menu = 1

        with open("menuMakanMinum.txt", 'r') as data: #membuka file didalam file data-makanan&minuman.txt

            data = json.load(data) #meload data json dari file

            makanan = data["makanan"] #mengambil data makanan dari file

            minuman = data["minuman"] #mengambil data minuman dari file

# menampilkan menu makanan

        print("-"*30)

        print("Daftar Makanan : ")

        no = 0

        for makan in makanan:

            no+=1

            print(f"{no}. {makan['nama']} | harga : {makan['harga']} ")

        

# menampilkan menu minuman

        print("-"*30)

        print("Daftar Minuman : ")

        no=0

        for minum in minuman:

            no+=1

            print(f"{no}. {minum['nama']} | harga : {minum['harga']} ")

        

# input pesanan

        order()

        order_lagi = input("Order Lagi [y/n]: ")

        if order_lagi == 'y':

            order()

        elif order_lagi == 'n':

            continue

    

    elif inp_menu_program == 2:

        print("-"*30)

        inp_nama = input("Masukan nama : ")

        data_pesan = load_pesanan() 

        data_pesanByName=data_pesan.get(inp_nama)[0]

     

# menampilkan data pesanan

        if data_pesanByName["keterangan"] == "":

            for i in data_pesanByName.keys():

                print(f"{i} : {data_pesanByName[i]}")

        print("-"*30)

        inp_bayar = int(input("Masukan Nominal : "))

        kembalian = inp_bayar - int(data_pesanByName['total'])

        print(f"kembaliannya adalah: {kembalian}")

        

        data_pesanByName['keterangan'] = "lunas"

        data_pesan[inp_nama]=data_pesanByName

        tulis_pesan(data_pesan)

        print("<<<TERIMAKASIH SUDAH MAMPIR>>>")

        break    

    else:

        print(f"Pembeli sudah membayar")

a = int(input("inpukan no.meja: "))

import datetime

 

x = datetime.datetime.now()

print ('Date: ',x)
