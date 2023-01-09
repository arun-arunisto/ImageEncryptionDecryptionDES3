from tkinter import *
import tkinter.messagebox as mbox
from tkinter import filedialog as fd
from Crypto.Cipher import DES3
from hashlib import md5

window = Tk()
window.geometry("1000x700")
window.title("Image Encryption Decryption DES")

def path_to_image():
    path = fd.askopenfilename(filetypes=[("Image File", '.jpg')])
    path_entry.insert(0, path)

def Encryption_Image():
    file_path = path_entry.get()
    key = key_entry.get()
    key_hash = md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = cipher.encrypt(file_bytes)
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        mbox.showinfo("Success", "Encrypted SuccessFully!!")

def Decryption_Image():
    file_path = path_entry.get()
    key = key_entry.get()
    key_hash = md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = cipher.decrypt(file_bytes)
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        mbox.showinfo("Success", "Decrypted Successfully!!")


path_label = Label(text="Path", font=("Arial", 15))
path_label.place(x=100, y=240)
path_entry = Entry(font=("Arial", 15))
path_entry.place(x=150, y=240)
key_label = Label(text="Key", font=("Arial", 15))
key_label.place(x=100, y=300)
key_entry = Entry(font=("Arial", 15))
key_entry.place(x=150, y=300)


# choose button created
chooseb = Button(window, text="Choose",command=path_to_image,font=("Arial", 15), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
chooseb.place(x =400 , y =232 )

# Encrypt button created
enb = Button(window, command=Encryption_Image, text="Encrypt",font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
enb.place(x =150 , y =620 )

# decrypt button created
deb = Button(window, command=Decryption_Image, text="Decrypt",font=("Arial", 20), bg = "blue", fg = "white", borderwidth=3, relief="raised")
deb.place(x =800 , y =620 )



# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =880 , y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()