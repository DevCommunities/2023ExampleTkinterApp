import customtkinter
from time import strftime
root = customtkinter.CTk()
root.title("CLOCK")

def time():
    string = strftime('%H:%M:%S %p')
    clocl_label.configure(text=string)
    clocl_label.after(1000, time)

clocl_label = customtkinter.CTkLabel(root,
                                     font=("ds-digital", 80, 'bold'),
                                     fg_color="black",
                                     text_color="green"
                                     )
clocl_label.grid(padx = 10 , pady=10)
time()
root.mainloop()