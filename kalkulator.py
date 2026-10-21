import tkinter as tk
from tkinter import messagebox

# --- Tema Warna Modern 3D & Pink Pastel ---
BG_COLOR = "#FCE4EC"        # Pink soft background
DISPLAY_BG = "#FFF0F5"      # Putih ke-pink-an untuk layar
DISPLAY_FG = "#4A2E35"      # Warna teks layar
BTN_NUM_BG = "#FFF9FB"      # Tombol angka (Putih bersih)
BTN_OP_BG = "#F8BBD0"       # Tombol operator (Pink sedang)
BTN_EQUAL_BG = "#EC407A"    # Tombol sama dengan (Pink fanta tegas)
BTN_CLEAR_BG = "#E53935"    # Tombol C (Merah soft)
BTN_TEXT_DARK = "#4A2E35"   # Teks gelap untuk tombol terang
BTN_TEXT_LIGHT = "#FFFFFF"  # Teks putih untuk tombol gelap

FONT_DISPLAY = ("Segoe UI", 26, "bold")
FONT_BTN = ("Segoe UI", 16, "bold")

class KalkulatorModern3D:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator ✨")
        self.root.geometry("340x520")
        self.root.resizable(False, False)
        self.root.config(bg=BG_COLOR)

        self.equation = ""
        self.display_text = tk.StringVar()

        # --- Frame Utama dengan Padding ---
        main_frame = tk.Frame(self.root, bg=BG_COLOR)
        main_frame.pack(expand=True, fill="both", padx=15, pady=15)

        # --- Layar / Display 3D Style ---
        display_frame = tk.Frame(
            main_frame, 
            bg="#D81B60", # Border efek 3D luar layar
            bd=2, 
            relief=tk.SUNKEN
        )
        display_frame.pack(fill="x", pady=(0, 15))

        display = tk.Entry(
            display_frame,
            font=FONT_DISPLAY,
            textvariable=self.display_text,
            justify="right",
            bd=8,
            relief=tk.FLAT,
            bg=DISPLAY_BG,
            fg=DISPLAY_FG
        )
        display.pack(fill="x", ipady=10)

        # --- Frame Tombol ---
        btn_frame = tk.Frame(main_frame, bg=BG_COLOR)
        btn_frame.pack(expand=True, fill="both")

        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
        ]

        self.btn_widgets = {}

        for (text, row, col) in buttons:
            # Tentukan warna tombol dan warna teks
            if text == '=':
                bg_color = BTN_EQUAL_BG
                fg_color = BTN_TEXT_LIGHT
                cmd = lambda t=text: self.animate_and_run(t, self.calculate)
            elif text == 'C':
                bg_color = BTN_CLEAR_BG
                fg_color = BTN_TEXT_LIGHT
                cmd = lambda t=text: self.animate_and_run(t, self.clear)
            elif text in ('/', '*', '-', '+', '(', ')'):
                bg_color = BTN_OP_BG
                fg_color = BTN_TEXT_DARK
                cmd = lambda t=text: self.animate_and_run(t, lambda: self.press(t))
            else:
                bg_color = BTN_NUM_BG
                fg_color = BTN_TEXT_DARK
                cmd = lambda t=text: self.animate_and_run(t, lambda: self.press(t))

            # Efek 3D Timbul menggunakan relief=RAISED dan bd=3
            btn = tk.Button(
                btn_frame,
                text=text,
                font=FONT_BTN,
                bg=bg_color,
                fg=fg_color,
                bd=3,
                relief=tk.RAISED,
                activebackground="#F8BBD0",
                command=cmd
            )

            if text == '=':
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=4, pady=4)
            else:
                btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

            self.btn_widgets[text] = {"widget": btn, "normal_bg": bg_color}

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

    # --- Fungsi Animasi Tekan (Efek Tombol Masuk ke Dalam) ---
    def animate_and_run(self, text, action):
        btn_info = self.btn_widgets.get(text)
        if btn_info:
            widget = btn_info["widget"]
            # Ubah relief jadi SUNKEN (seperti tombol fisik yang ditekan ke dalam)
            widget.config(relief=tk.SUNKEN)
            self.root.after(100, lambda: widget.config(relief=tk.RAISED))
        
        action()

    def press(self, num):
        self.equation += str(num)
        self.display_text.set(self.equation)

    def clear(self):
        self.equation = ""
        self.display_text.set("")

    def calculate(self):
        try:
            result = str(eval(self.equation))
            self.display_text.set(result)
            self.equation = result
        except ZeroDivisionError:
            messagebox.showerror("Oops!", "Nggak boleh bagi nol ya!")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Formatnya salah..")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = KalkulatorModern3D(root)
    root.mainloop()