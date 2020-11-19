from os import system
import sys

def print_menu():
	system("cls")
	menu_tampilan = """
	***************
	PENDAFTARAN SISWA BARU
	***************
	[A]. Mendaftarkan Murid (Tambah Kontak)
	[B]. Lihat Daftarkan Murid (Lihat Semua Kontak)
	[C]. Edit Informasi Murid (Cari Kontak)(Edit Informasi Kontak)
	[D]. Keluar Dari Dftar(Hapus Kontak)(Keluar Aplikasi) 
	"""
	print(menu_tampilan)



def Mendaftarkan_Murid():
	system("cls")
	print("Menambahkan Kontak Baru\nInformasi Kontak")
	nama = input("Nama\t:")
	telp = input("Telp\t:")
	alamat = input("Alamat\t:")
	asal = input("Asal\t:")
	respon = input(f"Yakin ingin menyimpan {nama} ? (Y/N) ")
	if respon.upper() == "Y":
		contacts[nama] = {
			"telp" : telp,
			"asal" : asal,
			"alamat" : alamat
		}
		print("Data Kontak Tersimpan.")
	else:
		print("Batal menyimpan.")
	input("Tekan ENTER untuk kembali ke MENU")

def Lihat_Daftarkan_Murid():
	system("cls")
	print("Daftar Kontak Yang Telah Disimpan")
	if len(contacts) == 0:
		print("Belum ada data yg disimpan saat ini.")
	else:
		print("NAMA |\t |NOMOR TELEPON|\t |ASAL|\t |ALAMAT")
		for contact in contacts:
			print(contact,"|\t|", contacts[contact]["telp"],"|\t|", contacts[contact]["asal"],"|\t|", contacts[contact]["alamat"])
	input("Tekan ENTER untuk kembali ke MENU")

def cari_kontak(contact):
	if contact in contacts:
		print("- RESULT -")
		print("Nama :",contact)
		print("Telp :",contacts[contact]["telp"])
		print("Asal :",contacts[contact]["asal"])
		print("Alamat :",contacts[contact]["alamat"])
		return True
	else:
		print("Data tidak ditemukan.")
		return False

def edit_telp(contact):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Telp\t:{contacts[contact]['telp']}")
	new_telp = input("Masukan Nomor Telp Baru : ")
	contacts[contact]["telp"] = new_telp
	print("Telp berhasil diperbarui.")
	cari_kontak(contact)

def edit_asal(contact):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Hobi\t:{contacts[contact]['hobi']}")
	new_hobby = input("Masukan Hobi Baru : ")
	contacts[contact]["hobi"] = new_hobby
	print("Hobi berhasil diperbarui.")
	cari_kontak(contact)

def edit_alamat(contact):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Alamat\t:{contacts[contact]['alamat']}")
	new_address = input("Masukan Hobi Baru : ")
	contacts[contact]["alamat"] = new_address
	print("Alamat berhasil diperbarui.")
	cari_kontak(contact)

def edit_nama(contact):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Nama\t:{contacts}")
	new_name = input("Masukan Nama Baru : ")
	#copy data lama ke kontak baru, yg lama di hapus.
	contacts[new_name] = contacts[contact]
	del contacts[contact]
	print("Nama berhasil diperbarui")
	cari_kontak(new_name)

def Edit_Informasi_Murid():
	system("cls")
	print("EDIT INFO KONTAK")
	nama = input("Nama Kontak yang akan di edit infonya : ")
	result = cari_kontak(nama)
	if result:
		print("EDIT [1]NAMA, [2]TELP, [3]ASAL, [4]ALAMAT")
		respon = input("Pilihan Informasi yg akan diedit (1/2/3/4) : ")
		if respon == "1":
			edit_nama(nama)
		elif respon == "2":
			edit_telp(nama)
		elif respon == "3":
			edit_asal(nama)
		elif respon == "4":
			edit_alamat(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def cek_respon_user(char):
	if char == "A":
		Mendaftarkan_Murid()
	elif char == "B":
		Lihat_Daftarkan_Murid()
	elif char == "C":
		Edit_Informasi_Murid()
	elif char == "D":
		pass
	else:
		print("INVALID RESPON")
		input("Enter to Back ...")

contacts = {
	'Bamband' : {
		'telp' : '082281490664',
		'asal' : 'SD IGS',
		'alamat' : 'Jl.Mayor Ruslan No.35'
	},
	'Budi' : {
		'telp' : '081254926777',
		'asal' : 'SD IGS',
		'alamat' : 'Jl.Bangau No.46'
	}
}
user_respon = ""
while user_respon != "D":
	print_menu()
	user_respon = input("RESPON : ").upper()
	cek_respon_user(user_respon)
else:
	system("cls")
	print("Good Bye....")
	#sys.exit()