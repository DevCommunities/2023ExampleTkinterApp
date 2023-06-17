import customtkinter as ctk # ใช้คำสั่ง as เพื่อตั้งชื่อให้โมดูลเรียกใช้ง่ายขึ้น
import math

# http://marcuscode.com/lang/python/dictionary
# เป็นการเก็บข้อมูลเเบบ Dictionary 
SI = {'T':math.pow(10,12),
      'G':math.pow(10,9),
      'M':math.pow(10,6),
      'k':math.pow(10,3),
      'h':math.pow(10,2),
      'da':math.pow(10,1),
      'P':float(10**-12),
      'n':float(math.pow(10,-9)),
      'u':float(math.pow(10,-6)),
      'm':float(math.pow(10,-3)),
      'c':float(math.pow(10,-2)),
      'd':float(math.pow(10,-1))}

app = ctk.CTk() #เป็นคำสั่งสำหรับสร้างหน้าต่างเเอพขึ้นมา
app.title("Convert SI Unit") # ตั้งชือเเอพของเรา
app.geometry("400x200") #เป็นการกำหนดขนาดหน้าต่างของเเอพเรา
    
# เป็นฟังก์ชั่นที่สร้างขึ้นมาเพื่อใช้คำนวนเเละเเสดงผลคำตอบ
def Click(choice):
    choice = choice
    inputs = input_Entry.get() # เป็นคำสั่งเก็บข้อมูลจากกล่องแสดงข้อมูล
    string = inputs[:len(inputs)-1]
    
    if str(string[-1]) == 'a':
        num = string[:len(string)-2]
        result = str(float(num) * ( SI['da']/SI[choice] )), choice+inputs[-1]
    elif choice == 'da':
        unit = string[len(string)-1:]
        num = string[:len(string)-1]
        result = str(float(num) * ( SI[unit]/SI[choice] )), choice+inputs[-1]
    elif (choice[-1] and string[-1] != 'a'):
        unit = string[len(string)-1:]
        num = string[:len(string)-1]
        result = str(float(num) * ( SI[unit]/SI[choice] )), choice+inputs[-1]

    result_Label.configure(text=result) # เป็นคำสั่งแก้ข้อมูลในกล่องแสดงข้อมูล

#สร้างกล่องแสดงข้อมูล
title = ctk.CTkLabel(app, text="เปลี่ยนหน่วย SI",
                     font=('Arial', 25),
                     pady=4,
                     corner_radius=20,
                     fg_color="#7DFAB6"
                     )
title.pack() 

# สร้างกล่องเก็บข้อมูล
input_Entry = ctk.CTkEntry(app,
                           placeholder_text="ใส่เลขเเละหน่วยที่ต้องการเปลี่ยน เช่น 10km",
                           width=300)
input_Entry.pack()

# สร้าง Combobox
combobox = ctk.CTkComboBox(master=app,
                                     values=['T', "G",
                                             "M", "k",
                                             "h", "da",
                                             "d", "c",
                                             "m", "u",
                                             "n", "P"
                                              ],
                                     width=60,
                                     command=Click)
combobox.pack(padx=10, pady=10)
combobox.set(" ")  # set initial value

# สร้างกล่องข้อความแสดงผลคำตอบ
result_Label = ctk.CTkLabel(app, text="00",
                            padx=20, pady=20,
                            font=('Arial', 25))
result_Label.pack()


app.mainloop()
