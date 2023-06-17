import customtkinter as ctk

root = ctk.CTk() # สร้างหน้าต่าง
root.title("Calculator") # ตั้งชื่อแอป

show = ctk.StringVar()
show_result = ctk.CTkLabel(root, textvariable=show, anchor='e', height=100, width=560,fg_color='#27374D').grid(row=0, column=0, columnspan=4) # สร้างช่องแสดงผล

expression = '' 
show.set(0) # ตั้งค่าเริ่มต้นเป็น 0

def input_buttons(nums): # set เลขที่กดเพิ่มเข้าไปใน expression
    global expression
    global show
    expression = expression+nums
    show.set(expression)

def calculation(): # คำนวนเลขโดยใช้ eval()
    try:
        global expression
        global show
        expression = expression.replace('^', '**')
        show.set(eval(expression))
    except:
        show.set('Error') # Error
        expression=''
        
def clear(): # เคลียร์ผลลัพธ์กลับไปที่ 0
    global expression 
    global show
    expression=0 
    show.set(expression)
    expression=''

# สร้างปุ่ม
button = ctk.CTkButton(root, text='C', command=clear, height=50, width=280, fg_color='#526D82').grid(row=1, column=0, columnspan=2)
button = ctk.CTkButton(root, text='^', command=lambda :input_buttons('^'), height=50, fg_color='#394867').grid(row=1, column=2)
button = ctk.CTkButton(root, text='/', command=lambda :input_buttons('/'), height=50, fg_color='#394867').grid(row=1, column=3)
button = ctk.CTkButton(root, text='7', command=lambda :input_buttons('7'), height=50, fg_color='#394867').grid(row=2, column=0)
button = ctk.CTkButton(root, text='8', command=lambda :input_buttons('8'), height=50, fg_color='#394867').grid(row=2, column=1)
button = ctk.CTkButton(root, text='9', command=lambda :input_buttons('9'), height=50, fg_color='#394867').grid(row=2, column=2)
button = ctk.CTkButton(root, text='*', command=lambda :input_buttons('*'), height=50, fg_color='#394867').grid(row=2, column=3)
button = ctk.CTkButton(root, text='4', command=lambda :input_buttons('4'), height=50, fg_color='#394867').grid(row=3, column=0)
button = ctk.CTkButton(root, text='5', command=lambda :input_buttons('5'), height=50, fg_color='#394867').grid(row=3, column=1)
button = ctk.CTkButton(root, text='6', command=lambda :input_buttons('6'), height=50, fg_color='#394867').grid(row=3, column=2)
button = ctk.CTkButton(root, text='-', command=lambda :input_buttons('-'), height=50, fg_color='#394867').grid(row=3, column=3)
button = ctk.CTkButton(root, text='1', command=lambda :input_buttons('1'), height=50, fg_color='#394867').grid(row=4, column=0)
button = ctk.CTkButton(root, text='2', command=lambda :input_buttons('2'), height=50, fg_color='#394867').grid(row=4, column=1)
button = ctk.CTkButton(root, text='3', command=lambda :input_buttons('3'), height=50, fg_color='#394867').grid(row=4, column=2)
button = ctk.CTkButton(root, text='+', command=lambda :input_buttons('+'), height=50, fg_color='#394867').grid(row=4, column=3)
button = ctk.CTkButton(root, text='.', command=lambda :input_buttons('.'), height=50, fg_color='#394867').grid(row=5, column=0)
button = ctk.CTkButton(root, text='0', command=lambda :input_buttons('0'), height=50, fg_color='#394867').grid(row=5, column=1)
button = ctk.CTkButton(root, text='=', command=calculation, height=50, width=280, fg_color='#526D82').grid(row=5, column=2, columnspan=2)

root.mainloop()