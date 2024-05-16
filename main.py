import tkinter as tk
from tkinter import messagebox

def encrypt_decrypt(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                offset = ord('a')
            else:
                offset = ord('A')
            shifted = (ord(char) - offset + shift) % 26 + offset
            result += chr(shifted)
        else:
            result += char
    return result

def perform_operation():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        if mode.get() == "Encrypt":
            result = encrypt_decrypt(text, shift, mode="encrypt")
        else:
            result = encrypt_decrypt(text, -shift, mode="decrypt")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")

# gui creation
root = tk.Tk()
root.title("Caesar Cipher")

label_text = tk.Label(root, text="Enter text:")
label_text.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_text = tk.Entry(root, width=30)
entry_text.grid(row=0, column=1, padx=5, pady=5)

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

mode = tk.StringVar(value="Encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode, value="Encrypt")
encrypt_radio.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode, value="Decrypt")
decrypt_radio.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

encrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=perform_operation)
encrypt_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_text = tk.Text(root, height=5, width=30)
result_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
