from tkinter import * # pip install tk
from tkinter import messagebox
import pyqrcode # pip install pyqrcode


ws = Tk()     # window setup
ws.config(bg='#52a2f2')
ws.title("QR Code generator")




def qr_generate(): # function to generate QR code

    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showwarning('Warning', 'Fill out the field.', font=('Calibri', 11))
    try:
        entered_value()
    except:
        pass



def entered_value(): # function to display the generated QR code
    img_lbl.config(image=img)



label = Label(ws, text="Enter the value: ",font=('Calibri', 14), bg='#52a2f2')  # label to display the text
label.pack()


user_input = StringVar()  # variable to store the user input
entry = Entry(ws, textvariable=user_input, bg='#000000')
entry.pack(padx=10)


button = Button(ws,text="Generate QR code!", font=('Calibri', 13), width=15,command=qr_generate) # button to generate QR code
button.pack(pady=10)


img_lbl = Label(ws, bg='#52a2f2') # label to display the generated QR code
img_lbl.pack()
output = Label(ws, text="", font=('Calibri', 14), bg='#52a2f2')
output.pack()


ws.mainloop()