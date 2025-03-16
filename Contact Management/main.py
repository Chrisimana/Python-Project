import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os
import phonenumbers
import re

# Nama file untuk menyimpan kontak
FILENAME = 'kontak.json'

# Fungsi untuk memuat kontak dari file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan kontak ke file
def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file)

# Fungsi untuk memvalidasi email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Fungsi untuk menampilkan semua kontak
def show_contacts():
    contacts_list.delete(*contacts_list.get_children())  # Menghapus daftar yang ada
    for contact in Kontak:
        contacts_list.insert('', tk.END, values=(contact['Nama'], contact['Hp'], contact['Email']))

# Fungsi untuk menambahkan kontak baru
def add_contact():
    Nama = simpledialog.askstring("Input", "Masukkan nama kontak:")
    Hp = simpledialog.askstring("Input", "Masukkan nomor hp kontak (misal: +62123456789):")
    Email = simpledialog.askstring("Input", "Masukkan email kontak:")
    
    if Nama and Hp and Email:
        if not is_valid_email(Email):
            messagebox.showwarning("Warning", "Email tidak valid.")
            return
        
        try:
            phone_number = phonenumbers.parse(Hp, None)
            if not phonenumbers.is_valid_number(phone_number):
                raise ValueError("Nomor HP tidak valid.")
            
            if any(contact['Nama'] == Nama for contact in Kontak):
                messagebox.showwarning("Warning", "Kontak dengan nama ini sudah ada.")
                return
            
            Kontak.append({'Nama': Nama, 'Hp': Hp, 'Email': Email})
            save_contacts(Kontak)
            show_contacts()
            messagebox.showinfo("Info", "Kontak berhasil ditambahkan.")
        except Exception as e:
            messagebox.showwarning("Warning", str(e))
    else:
        messagebox.showwarning("Warning", "Semua field harus diisi!")

# Fungsi untuk menghapus kontak
def delete_contact():
    selected_item = contacts_list.selection()
    if selected_item:
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus kontak ini?")
        if confirm:
            index = contacts_list.index(selected_item[0])
            Kontak.pop(index)
            save_contacts(Kontak)
            show_contacts()
            messagebox.showinfo("Info", "Kontak berhasil dihapus.")
    else:
        messagebox.showwarning("Warning", "Silakan pilih kontak yang ingin dihapus.")

# Inisialisasi kontak
Kontak = load_contacts()

# Membuat jendela utama
root = tk.Tk()
root.title("Contact Management")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Frame utama
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

# Label Judul
label_title = tk.Label(root, text="Contact Management", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#333")
label_title.pack(pady=10)

# Treeview untuk daftar kontak
columns = ('Nama', 'Hp', 'Email')
contacts_list = ttk.Treeview(frame, columns=columns, show='headings', height=10)
contacts_list.heading('Nama', text='Nama')
contacts_list.heading('Hp', text='No. HP')
contacts_list.heading('Email', text='Email')
contacts_list.pack(side=tk.LEFT)

# Scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=contacts_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
contacts_list.configure(yscrollcommand=scrollbar.set)

# Tombol
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=20)

add_button = ttk.Button(button_frame, text="Tambah Kontak", command=add_contact)
add_button.grid(row=0, column=0, padx=10)

delete_button = ttk.Button(button_frame, text="Hapus Kontak", command=delete_contact)
delete_button.grid(row=0, column=1, padx=10)

# Menampilkan kontak yang ada
show_contacts()

# Menjalankan aplikasi
root.mainloop()
