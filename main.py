import customtkinter as ctk
import tkinter as tk

class App:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Rain Sim")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        self.canvas = ctk.CTkCanvas(self.root, background="#3A5189")
        self.canvas.place(x=10, y=10, width=430, height=280)

        self.z_index = 0
        self.speed = 0
        self.gravity = 0
        self.amount = 0

        font = ("Consolas", 15)

        ctk.CTkLabel(self.root, text="Z-Index Range", anchor=tk.CENTER, text_font=font).place(x=10, y=300, width=215, height=25)
        self.z_index_val = ctk.CTkLabel(self.root, text="0", anchor=tk.CENTER, text_font=font)
        self.z_index_val.place(x=225, y=300, width=215, height=25)
        self.z_index_slider = ctk.CTkSlider(self.root, to=15, from_=1, command=self.change_z_index, number_of_steps=14)
        self.z_index_slider.place(x=10, y=330, width=430, height=10)
        self.z_index_slider.set(5)
        
        ctk.CTkLabel(self.root, text="Speed Range", anchor=tk.CENTER, text_font=font).place(x=10, y=350, width=215, height=25)
        self.speed_val = ctk.CTkLabel(self.root, text="0", anchor=tk.CENTER, text_font=font)
        self.speed_val.place(x=225, y=350, width=215, height=25)
        self.speed_slider = ctk.CTkSlider(self.root, to=50, from_=5, command=self.change_speed, number_of_steps=45)
        self.speed_slider.place(x=10, y=385, width=430, height=10)
        self.speed_slider.set(15)
        
        ctk.CTkLabel(self.root, text="Gravity Range", anchor=tk.CENTER, text_font=font).place(x=10, y=405, width=215, height=25)
        self.gravity_val = ctk.CTkLabel(self.root, text="0", anchor=tk.CENTER, text_font=font)
        self.gravity_val.place(x=225, y=405, width=215, height=25)
        self.gravity_slider = ctk.CTkSlider(self.root, to=0.5, from_=0.1, command=self.change_gravity)
        self.gravity_slider.place(x=10, y=440, width=430, height=10)
        self.gravity_slider.set(0.2)
        
        ctk.CTkLabel(self.root, text="Amount", anchor=tk.CENTER, text_font=font).place(x=10, y=460, width=215, height=25)
        self.amount_val = ctk.CTkLabel(self.root, text="0", anchor=tk.CENTER, text_font=font)
        self.amount_val.place(x=225, y=460, width=215, height=25)
        self.amount_slider = ctk.CTkSlider(self.root, to=750, from_=100, command=self.change_amount, number_of_steps=650)
        self.amount_slider.place(x=10, y=490, width=430, height=10)
        self.amount_slider.set(500)

    def change_z_index(self, val):
        self.z_index = int(val)
        self.z_index_val.config(text=f"{int(val)}")
        
    def change_speed(self, val):
        self.speed = int(val)
        self.speed_val.config(text=f"{int(val)}")
        
    def change_gravity(self, val):
        self.gravity = round(val, 2)
        self.gravity_val.config(text=f"{round(val, 2)}")
        
    def change_amount(self, val):
        self.amount = int(val)
        self.amount_val.config(text=f"{int(val)}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()