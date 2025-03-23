import tkinter as tk
from tkinter import scrolledtext

# Fungsi untuk mendapatkan respons dari chatbot
def get_response(user_input):
    user_input = user_input.lower()
    
    if "hai" in user_input or "halo" in user_input:
        return "Halo! Apa kabar?"
    elif "apa kabar" in user_input:
        return "Saya baik-baik saja, terima kasih! Bagaimana dengan Anda?"
    elif "siapa nama kamu" in user_input:
        return "Saya adalah chatbot sederhana. Anda bisa memanggil saya Chatbot."
    elif "apa yang bisa kamu lakukan" in user_input:
        return "Saya bisa menjawab pertanyaan sederhana dan berbicara dengan Anda."
    elif "terima kasih" in user_input:
        return "Sama-sama! Jika ada yang ingin ditanyakan, silakan."
    elif "selamat tinggal" in user_input or "bye" in user_input:
        return "Selamat tinggal! Semoga hari Anda menyenangkan."
    else:
        return "Maaf, saya tidak mengerti. Bisa Anda ulangi?"

# Fungsi untuk mengirim pesan
def send_message():
    user_input = entry_message.get()
    if user_input:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Anda: " + user_input + "\n")
        response = get_response(user_input)
        chat_area.insert(tk.END, "Chatbot: " + response + "\n")
        chat_area.config(state=tk.DISABLED)
        entry_message.delete(0, tk.END)

# Membuat jendela utama
root = tk.Tk()
root.title("Chatbot Sederhana")

# Membuat area chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20)
chat_area.pack(pady=10)

# Membuat entry untuk pesan
entry_message = tk.Entry(root, width=50)
entry_message.pack(pady=10)

# Membuat tombol untuk mengirim pesan
send_button = tk.Button(root, text="Kirim", command=send_message)
send_button.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()