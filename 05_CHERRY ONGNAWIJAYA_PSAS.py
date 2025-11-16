import tkinter as tk
from tkinter import *
from tkinter import ttk

dropdown_option = ["Archive81", "Adolescence", "Clickbait", "The Guilty"]
data = []

def tampilkan(frame):
    frame.tkraise()

def hal1_login():
    username = str(entry.get())
    password = str(entry2.get())
    if password == "1" and username == "c":
        tampilkan(hal2)
    elif password == "ad123" and username == "admin":
        tampilkan(hal6)
    else:
        label_hasil.config(text=f"Password atau Username salah!", font=("Times New Roman", 10, "bold", "italic"), fg="red")

def hal2_simpandata():
    nama = str(entry3.get())
    film = str(select.get())
    pembayaran = str(status.get())

    if not nama or film == "Select a film" or not pembayaran:
        label_hasil2.config(text="Semua data harus diisi dengan benar!", font=("Times New Roman", 10, "bold", "italic"), fg="red")
        return
    
    try:
        harga = float(entry6.get())
        jumlah_tiket = int(entry5.get())
    except ValueError:
        label_hasil2.config(text="Semua data harus diisi dengan benar!", font=("Times New Roman", 10, "bold", "italic"), fg="red")
        return

    data.append({"Nama": nama, "Film": film, "Jumlah Tiket": jumlah_tiket, "Harga": harga, "Pembayaran": pembayaran})
    label_hasil2.config(text="Data berhasil disimpan!", font=("Times New Roman", 10, "bold", "italic"), fg="green")

    entry3.delete(0, tk.END)
    select.set("Select a film")
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    status.set("")
    
    tampilkan(hal2)

def hal3_tampilkandata():
    for i in tabel.get_children():
        tabel.delete(i)

    if data:
        for item in data:
            tabel.insert("", tk.END, values=(item["Nama"], item["Film"], item["Jumlah Tiket"], item["Harga"], item["Pembayaran"]))
    else:
        tabel.insert("", tk.END, values=("Belum ada data", "-", "-", "-", "-"))

    tampilkan(hal3)

def hal4_caridata():
    keyword = entry10.get().lower()

    for i in tabel_cari.get_children():
        tabel_cari.delete(i)

    hasil = [item for item in data if keyword in item["Nama"].lower()]

    if hasil:
        for item in hasil:
            tabel_cari.insert("", tk.END, values=(item["Nama"], item["Film"], item["Jumlah Tiket"], item["Harga"], item["Pembayaran"]))
    else:
        tabel_cari.insert("", tk.END, values=("Data tidak ditemukan", "-", "-", "-", "-"))

    tampilkan(hal4)

def hal5_laporandata():
    total_qris = 0
    total_cash = 0

    for i in data:
        if i["Pembayaran"] == "QRIS":
            total_qris += i["Harga"]
        elif i["Pembayaran"] == "Cash":
            total_cash += i["Harga"]

    label_hasil3.config(text=f"Rp. {total_cash}")
    label_hasil4.config(text=f"Rp. {total_qris}")

    total = total_qris + total_cash

    label_hasil5.config(text=f"Rp. {total}")


    tampilkan(hal5)

def hal6_tambahdata():
    addon = entry11.get()

    label_hasil6.config(text="")
    
    if addon == "":
        label_hasil6.config(text="Masukkan Judul Film yang Belum Ada!", font=("Times New Roman", 10, "bold", "italic"), fg="red")
    elif any(addon in element for element in dropdown_option) == True:
        label_hasil6.config(text="Masukkan Judul Film yang Belum Ada!", font=("Times New Roman", 10, "bold", "italic"), fg="red")
    else:
        dropdown_option.append(addon)

        dropdown["menu"].delete(0, tk.END)

        for newfilm in dropdown_option:
            dropdown["menu"].add_command(label=newfilm, command=tk._setit(select, newfilm))

        entry11.delete(0, tk.END)

        label_hasil6.config(text=f"{addon} berhasil ditayangkan!", font=("Times New Roman", 10, "bold", "italic"), fg="green")

    tampilkan(hal6)

def hal7_hapusdata():
    rev = entry12.get()

    label_hasil7.config(text="")

    if rev == "":
        label_hasil7.config(text="Masukkan Judul Film yang Sudah Ada!", font=("Times New Roman", 10, "bold", "italic"), fg="red")
    elif not any(rev in element for element in dropdown_option):
        label_hasil7.config(text="Masukkan Judul Film yang Sudah Ada!", font=("Times New Roman", 10, "bold", "italic"), fg="red")
    else:
        dropdown_option.remove(rev)

        dropdown["menu"].delete(0, tk.END)

        for newfilm in dropdown_option:
            dropdown["menu"].add_command(label=newfilm, command=tk._setit(select, newfilm))

        entry12.delete(0, tk.END)

        label_hasil7.config(text=f"{rev} berhasil dihapus!", font=("Times New Roman", 10, "bold", "italic"), fg="green")

    tampilkan(hal7)

jendela = tk.Tk()
jendela.title("Aplikasi Pemesanan Bioskop")
jendela.geometry("800x500")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Times New Roman", 12, "bold"), background="#D2E1E9", foreground="black")
style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="black")

# HALAMAN 7 [ PENGHAPUSAN FILM ]
hal7 = Frame(jendela, bg="#BDD5E3")
label17 = Label(hal7, text="( Penghapusan Jenis Film )", font=("Georgia", 20, "bold"), fg="black", bg="#BDD5E3")
label17.pack(pady=5)
label18 = Label(hal7, text="Tuliskan Nama Film yang Akan Dihapus: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label18.pack()
entry12 = Entry(hal7)
entry12.pack()
label_hasil7 = Label(hal7, text="", font=("Times New Roman", 15, "bold"), bg="#BDD5E3")
label_hasil7.pack(pady=5)
button15 = Button(hal7, text="Remove", command= hal7_hapusdata, font=("Times New Roman", 10, "bold"))
button15.pack(pady=5)
button13 = Button(hal7, text="Previous Page", command= lambda:tampilkan(hal6), font=("Times New Roman", 10, "bold"))
button13.pack(pady=5)

# HALAMAN 6 [ PENAMBAHAN FILM ]
hal6 = Frame(jendela, bg="#BDD5E3")
label15 = Label(hal6, text="( Penambahan Jenis Film )", font=("Georgia", 20, "bold"), fg="black", bg="#BDD5E3")
label15.pack(pady=5)
label16 = Label(hal6, text="Tambahkan Nama Film yang Akan Tayang: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label16.pack()
entry11 = Entry(hal6)
entry11.pack()
label_hasil6 = Label(hal6, text="", font=("Times New Roman", 15, "bold"), bg="#BDD5E3")
label_hasil6.pack(pady=5)
button14 = Button(hal6, text="Add", command= hal6_tambahdata, font=("Times New Roman", 10, "bold"))
button14.pack(pady=5)

button_frame2 = Frame(hal6, bg="#BDD5E3")
button_frame2.pack()
button10 = Button(button_frame2, text="Logout", command= lambda:tampilkan(hal1), bg="#FFFFFF", font=("Times New Roman", 10, "bold"), fg="red")
button10.pack(side=tk.LEFT,pady=5,padx=10)
button12 = Button(button_frame2, text="Next Page", command = lambda: tampilkan(hal7), bg="#FFFFFF", font=("Times New Roman", 10, "bold"))
button12.pack(side=tk.LEFT,pady=5,padx=10)

# HALAMAN 5 [ LAPORAN ]
hal5 = Frame(jendela, bg="#BDD5E3")
label11 = Label(hal5, text="( Laporan Data )", font=("Georgia", 20, "bold"), fg="black", bg="#BDD5E3")
label11.pack(pady=5)
label12 = Label(hal5, text=f"Jumlah Pendapatan Cash Hari Ini: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label12.pack()
label_hasil3 = Label(hal5, text="", font=("Times New Roman", 15, "bold"), bg="#BDD5E3")
label_hasil3.pack()
label13 = Label(hal5, text=f"Jumlah Pendapatan QRIS Hari Ini: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label13.pack()
label_hasil4 = Label(hal5, text="", font=("Times New Roman", 15, "bold"), bg="#BDD5E3")
label_hasil4.pack()
label14 = Label(hal5, text=f"Jumlah Pendapatan Total Hari Ini: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label14.pack()
label_hasil5 = Label(hal5, text="", font=("Times New Roman", 15, "bold"), bg="#BDD5E3")
label_hasil5.pack(pady=5)
button8 = Button(hal5, text="Kembali", command= lambda: tampilkan(hal2), bg="#FFFFFF")
button8.pack()

# HALAMAN 4 [ PENCARIAN DATA ]
hal4 = Frame(jendela, bg="#BDD5E3")
label9 = Label(hal4, text="( Cari Data Pemesanan Film Bioskop )", font=("Georgia", 20, "bold"), fg="black", bg="#BDD5E3")
label9.pack(pady=5)
label10 = Label(hal4, text="Masukkan Nama: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label10.pack(pady=5)
entry10 = Entry(hal4)
entry10.pack()
button6 = Button(hal4, text="Cari Data", command=hal4_caridata, bg="#FFFFFF")
button6.pack()

kolom_cari = ("Nama", "Film", "Jumlah Tiket", "Harga", "Pembayaran")
tabel_cari = ttk.Treeview(hal4, columns=kolom_cari, show="headings", height=10)
for kol in kolom_cari:
    tabel_cari.heading(kol, text=kol)
tabel_cari.pack(pady=5)

button7 = Button(hal4, text="Kembali", command= lambda: tampilkan(hal2), bg="#FFFFFF")
button7.pack()

# HALAMAN 3 [ TAMPIL DATA ]
hal3 = Frame(jendela, bg="#BDD5E3")
label8 = Label(hal3, text="( Data Pemesanan Film Bioskop )", font=("Georgia", 20, "bold"), fg="black", bg="#BDD5E3")
label8.pack(pady=5)

kolom = ("Nama", "Film", "Jumlah Tiket", "Harga", "Pembayaran")
tabel = ttk.Treeview(hal3, columns=kolom, show="headings", height=10)
for kol in kolom:
    tabel.heading(kol, text=kol)
tabel.pack(pady=5)

button5 = Button(hal3, text="Kembali", command= lambda: tampilkan(hal2), bg="#FFFFFF")
button5.pack()

# HALAMAN 2 [ FORM INPUT DATA ]
hal2 = tk.Frame(jendela, bg="#BDD5E3")
judul2 = Label(hal2, text="( Input Data )", font=("Georgia", 20, "bold"), bg="#BDD5E3", fg="black")
judul2.pack(pady=5)
label3 = Label(hal2, text=f"Nama: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label3.pack()
entry3 = Entry(hal2)
entry3.pack()
label4 = Label(hal2, text=f"Film: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label4.pack()

select = tk.StringVar(hal2)
select.set("Select a film")
dropdown = tk.OptionMenu(hal2, select, *dropdown_option)
dropdown.pack()

dropdown.config(bg="#FFFFFF",  activebackground="#FFFFFF", highlightthickness=0, font=("Times New Roman", 10, "italic", "bold"))

label5 = Label(hal2, text=f"Jumlah Tiket: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label5.pack()
entry5 = Entry(hal2)
entry5.pack()
label6 = Label(hal2, text=f"Harga: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label6.pack()
entry6 = Entry(hal2)
entry6.pack()
label7 = Label(hal2, text=f"Bentuk Pembayaran: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label7.pack()

status = StringVar()
status.set("")
option1 = Checkbutton(hal2, text="Cash", variable=status, onvalue="Cash", offvalue="", bg="#BDD5E3", font=("Times New Roman", 10, "bold", "italic"))
option1.pack()
option2 = Checkbutton(hal2, text="QRIS", variable=status, onvalue="QRIS", offvalue="", bg="#BDD5E3", font=("Times New Roman", 10, "bold", "italic"))
option2.pack()

label_hasil2 = Label(hal2, text="", bg="#BDD5E3")
label_hasil2.pack(pady=5)

button2 = Button(hal2, text="Simpan Data", command= hal2_simpandata, bg="#FFFFFF", font=("Times New Roman", 10, "bold"))
button2.pack(pady=5)

button_frame = Frame(hal2, bg="#BDD5E3")
button_frame.pack()
button3 = Button(button_frame, text="Lihat Data", command= hal3_tampilkandata, bg="#FFFFFF", font=("Times New Roman", 10, "bold"))
button3.pack(side=tk.LEFT,pady=5,padx=10)
button4 = Button(button_frame, text=f"Cari Data", command= lambda: tampilkan(hal4), bg="#FFFFFF", font=("Times New Roman", 10, "bold"))
button4.pack(side=tk.LEFT,pady=5,padx=10)

button9 = Button(hal2, text="Laporan", command= hal5_laporandata, bg="#FFFFFF", font=("Times New Roman", 10, "bold"))
button9.pack(pady=5)

button11 = Button(hal2, text="Logout", command= lambda: tampilkan(hal1), bg="#FFFFFF", font=("Times New Roman", 10, "bold"), fg="red")
button11.pack(pady=20)

# HALAMAN 1 [ LOGIN ]
hal1 = Frame(jendela, bg="#BDD5E3")
judul = Label(hal1, text="( Data Pemesanan Tiket Bioskop )", font=("Georgia", 20, "bold"), bg="#BDD5E3", fg="black")
judul.pack(pady=5)
label = Label(hal1, text=f"Username: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label.pack()
entry = Entry(hal1)
entry.pack()
label2 = Label(hal1, text=f"Password: ", font=("Times New Roman", 10, "bold"), bg="#BDD5E3")
label2.pack()
entry2 = Entry(hal1)
entry2.pack()
label_hasil= Label(hal1, text="", bg="#BDD5E3")
label_hasil.pack(pady=5)
button = Button(hal1, text="Login", command= hal1_login, font=("Times New Roman", 10, "bold"), bg="#FFFFFF", fg="green")
button.pack(pady=2)

for frame in (hal1, hal2, hal3, hal4, hal5, hal6, hal7): 
    frame.place(x=0,y=0,relwidth=1,relheight=1)

jendela.mainloop()