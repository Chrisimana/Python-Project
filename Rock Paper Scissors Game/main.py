import tkinter as tk
import random
from tkinter import messagebox

# Variabel untuk menyimpan bahasa yang sedang digunakan
current_language = "indonesia"

# Teks dalam bahasa Indonesia dan Inggris
texts = {
    "indonesia": {
        "title": ".:: Permainan Suit/Pingsut ::.",
        "gajah": "1. Jempol (Gajah)",
        "manusia": "2. Telunjuk (Manusia)",
        "semut": "3. Kelingking (Semut)",
        "results": {
            1: {
                1: "Sama-sama Gajah! Sesama gajah saling membantu...",
                2: "Diinjek gajah.. kamu kalah!",
                3: "Kamu gigit gajah, kamu menang!"
            },
            2: {
                1: "Kamu abis nginjek manusia, kamu menang!",
                2: "Sama-sama Manusia! Jangan berantem lah...",
                3: "Kamu dibunuh manusia, kamu kalah!"
            },
            3: {
                1: "Kamu abis dikerjain sama semut, kamu kalah!",
                2: "Kamu gak sengaja injek semut, kamu menang!",
                3: "Sesama semut saling membahu..!"
            }
        },
        "computer_choice": "Pilihan Komputer: {} (1: Gajah, 2: Manusia, 3: Semut)"
    },
    "english": {
        "title": ".:: Rock Paper Scissors Game ::.",
        "gajah": "1. Thumb (Elephant)",
        "manusia": "2. Index Finger (Human)",
        "semut": "3. Little Finger (Ant)",
        "results": {
            1: {
                1: "Both chose Elephant! Elephants help each other...",
                2: "You got stepped on by an elephant.. you lose!",
                3: "You bit the elephant, you win!"
            },
            2: {
                1: "You stepped on a human, you win!",
                2: "Both chose Human! Don't fight...",
                3: "You were killed by a human, you lose!"
            },
            3: {
                1: "You got messed up by an ant, you lose!",
                2: "You accidentally stepped on an ant, you win!",
                3: "Ants help each other..!"
            }
        },
        "computer_choice": "Computer's choice: {} (1: Elephant, 2: Human, 3: Ant)"
    }
}

def play_game(pil):
    global current_language
    # Pilihan komputer
    kom = random.randint(1, 3)

    # Menentukan hasil permainan
    result = texts[current_language]["results"][kom][pil]

    # Menampilkan hasil
    messagebox.showinfo("Hasil Permainan", result + f"\n\n{texts[current_language]['computer_choice'].format(kom)}")

def change_language():
    global current_language
    if current_language == "indonesia":
        current_language = "english"
    else:
        current_language = "indonesia"
    update_ui()

def update_ui():
    global current_language
    label_title.config(text=texts[current_language]["title"])
    button_gajah.config(text=texts[current_language]["gajah"])
    button_manusia.config(text=texts[current_language]["manusia"])
    button_semut.config(text=texts[current_language]["semut"])

# Membuat jendela utama
root = tk.Tk()
root.title("Permainan Suit/Pingsut")

# Membuat label judul
label_title = tk.Label(root, text=texts[current_language]["title"], font=("Arial", 16))
label_title.pack(pady=10)

# Membuat tombol untuk pilihan
button_gajah = tk.Button(root, text=texts[current_language]["gajah"], command=lambda: play_game(1), width=30)
button_gajah.pack(pady=5)

button_manusia = tk.Button(root, text=texts[current_language]["manusia"], command=lambda: play_game(2), width=30)
button_manusia.pack(pady=5)

button_semut = tk.Button(root, text=texts[current_language]["semut"], command=lambda: play_game(3), width=30)
button_semut.pack(pady=5)

# Membuat tombol untuk mengganti bahasa
button_change_language = tk.Button(root, text="Change Language", command=change_language, width=30)
button_change_language.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()