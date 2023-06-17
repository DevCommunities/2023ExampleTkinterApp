import customtkinter
from random import choice

customtkinter.set_appearance_mode("dark")

# Rock, Paper, Scissors function (ฟังก์ชั่นค้อน,กระดาษ,กรรไกร)
def play_game(player_choice):
    computer_choice = choice(["Rock", "Paper", "Scissors"])
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.configure(text=f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n{result}",font=("Helvetica", 40, "bold"))

# Create the main window (สร้างหน้าต่างหลัก)
window = customtkinter.CTk()
window.title("Rock Paper Scissors")

# Create the game title (สร้างชื่อเกม)
title_label = customtkinter.CTkLabel(window, text="Rock Paper Scissors", font=("Helvetica", 60, "bold"))
title_label.pack(pady=20)

# Create the buttons (สร้างปุ่ม)
# Rock button (ปุ่มหิน)
rock_button = customtkinter.CTkButton(window, text="Rock", font=("Helvetica", 30, "bold"), width=250,height=100,corner_radius=1000,border_color="#FFFFFF",border_width=10,text_color="#1a458a",fg_color="#006C6C",hover_color="#FFFFC9", command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

# Paper button (ปุ่มกระดาษ)
paper_button = customtkinter.CTkButton(window, text="Paper", font=("Helvetica", 30, "bold"), width=250,height=100,corner_radius=1000,border_color="#FFFFFF",border_width=10,text_color="#f8c134",fg_color="#006C6C",hover_color="#FFFFC9", command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

# Scissors button (ปุ่มกรรไกร)
scissors_button = customtkinter.CTkButton(window, text="Scissors", font=("Helvetica", 30, "bold"), width=250,height=100,corner_radius=1000,border_color="#FFFFFF",border_width=10,text_color="#1a458a",fg_color="#006C6C",hover_color="#FFFFC9", command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)

# Create the result label (สร้างป้ายกำกับผลลัพธ์)
result_label = customtkinter.CTkLabel(window, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Start the main loop (เริ่มลูปวนหลัก)
window.mainloop()