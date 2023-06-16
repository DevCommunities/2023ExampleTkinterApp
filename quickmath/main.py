import customtkinter
from playsound import playsound
import random # ใช้ในการสุ่มเลข
import time # ใช้ในการหน่วงเวลา

customtkinter.set_default_color_theme("dark-blue") # ตั้งค่าโทนสีเป็น dark-blue

# สร้างตัวแอปขึ้นมา
app = customtkinter.CTk() # ตัวแปร app จะเป็นตัวแอปที่เราสร้างขึ้นมา
app.title("QuickMath") # ตั้งชื่อแอป
app.geometry("700x350") # ตั้งขนาดหน้าต่างของแอป

# สร้างข้อความหลักให้ผู้ใช้เห็น เป็นชื่อแอป QuickMath
main_text = customtkinter.CTkLabel(app, text="QuickMath🔥", font=("Arial", 30))
main_text.pack(pady=(20, 0)) # pady คือ ระยะห่างของ widget จาก widget อื่นๆ ในแกน y หรือก็ตือ (pad-y)
sub_text = customtkinter.CTkLabel(app, text="⭐คณิตคิดเร็ว เกมคณิตของคนจริง⭐", font=("Tahoma", 15))
sub_text.pack(pady=(5, 0)) # pady รับค่าเป็น pad บน กับ pad ล่าง ในกรณีนี้เราไม่ต้องการให้มีระยะห่างด้านล่าง จึงใส่ 5, 0

# สร้างโจทย์ แล้วเอาโจทย์มาแสดงในหน้าต่าง
def generate_question(): # ฟังชั่นสำหรับสร้างโจทย์
    operation = random.choice(["+", "-", "*", "/"]) # เลือกเครื่องหมายการคำนวณแบบสุ่ม
    a, b = random.randint(1, 10), random.randint(1, 10) # เลือกตัวเลขแบบสุ่ม 1 - 100

    problem = f"{a} {operation} {b}" # สร้างโจทย์
    return problem

problem = generate_question() # สร้างโจทย์ 
problem_text = customtkinter.CTkLabel(app, text=problem, font=("Arial", 40)) # แล้วเอาโจทย์มาแสดงในหน้าต่าง
problem_text.pack(pady=(10, 0)) # pady รับค่าเป็น pad บน กับ pad ล่าง ในกรณีนี้เราอยาก เว้นระยะห่างด้านบน จึงใส่ 10, 0

def check_input(user_input): # ตรวจสอบคำตอบว่าถูกหรือไม่
    if user_input == "": # ถ้าผู้ใช้ไม่ได้พิมพ์คำตอบ
        return # ไม่ต้องส่งค่าอะไรกลับ
    
    problem = problem_text._text # ดึงค่าโจทย์จาก sub_text
    answer = round(float(eval(problem)), 2) # คำนวณคำตอบจากโจทย์ แปลงเป็น float ก่อน แล้วค่อย round ทศนิยม 2 ตำแหน่ง
    print(answer, user_input) # แสดงคำตอบจากโจทย์ และคำตอบที่ผู้ใช้ตอบ

    if float(answer) == float(user_input): # ถ้าคำตอบที่ผู้ใช้ตอบ ตรงกับคำตอบจากโจทย์
        sub_text.configure(text="ถูกต้องนะครับ", text_color="green") # ให้แสดงข้อความว่า "ถูกต้องนะครับ" และเปลี่ยนสีเป็นสีเขียว
    else:
        sub_text.configure(text=f"ผิดนะครับ {problem} ตอบ {answer}", text_color="red") # ถ้าผิดเป็นสีแดง
        
        file_root = __file__.replace("main.py", "") # หาตำแหน่งไฟล์ที่เราเปิดอยู่
        audio_path = f'{file_root}/truetham.mp3' # ตั้งตำแหน่งไฟล์เสียง
        playsound(audio_path) # เล่นไฟล์เสียง

    entry.delete(0, "end") # ลบข้อความในช่องรับค่าข้อความ เพื่อให้ผู้ใช้สามารถพิมพ์คำตอบใหม่ได้
    problem = generate_question() # สร้างโจทย์ใหม่
    problem_text.configure(text=problem) # แสดงโจทย์ใหม่
    
    return # ไม่ต้องส่งค่าอะไรกลับ

# ใส่ช่องรับค่าข้อความ
entry = customtkinter.CTkEntry(app, placeholder_text="ใส่คำตอบของคุณ")
entry.pack(pady=20) # pady คือ ระยะห่างของ widget จาก widget อื่นๆ
entry.bind("<Return>", lambda event: check_input(entry.get())) # ใส่ event เมื่อกด enter ให้รันฟังชั่น check_input โดยให้ส่งค่า entry.get() ไปด้วย (ค่าที่อยู่ในช่องรับค่าข้อความ) เพื่อดูว่าผู้ใช้ตอบถูกหรือไม่

app.mainloop()