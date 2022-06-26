import customtkinter as ctk
import tkinter as tk
import random

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

class Drop:
    def __init__(self, z, speed, gravity):
        self.y = random.randint(-100, -50)
        self.x = random.randint(0, 430)
        self.z = random.randint(0, z)
        self.len = translate(self.z, 0, z, 10, 25)
        self.speed = translate(self.z, 0, z, 5, speed)
        self.speed_ = self.speed
        self.gravity = translate(self.z, 0, z, 0, gravity)
    
    def update(self):
        self.y+=self.speed_
        self.speed_+=self.gravity
        if self.y > 280:
            self.y = random.randint(-200, -100)
            self.x = random.randint(0, 430)
            self.speed_ = self.speed


class App:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Rain Sim")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, background="#3A5189", width=430, height=280)
        self.canvas.place(x=10, y=10, width=430, height=280)

        self.z_index = 5
        self.speed = 15
        self.gravity = 0.2
        self.amount = 300

        self.drops = []
        for i in range(self.amount):
            self.drops.append(Drop(self.z_index, self.speed, self.gravity))
        self.drop_ele = []

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
        self.speed_slider = ctk.CTkSlider(self.root, to=50, from_=10, command=self.change_speed, number_of_steps=45)
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
        self.amount_slider.set(300)

        ctk.CTkButton(self.root, command=self.start_sim, text="Restart Simulation").place(x=150, y=510, width=145, height=30)
        for d in self.drops:
            dr = self.canvas.create_line(d.x, d.y, d.x, d.y+d.len, fill="#122332", width=3)
        self.drop_ele = list(self.canvas.find_all())
        self.update()

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
    
    def update(self):
        for index, d in enumerate(self.drops):
            d.update()
            # self.canvas.move(self.drop_ele[index], 0, d.speed_)
            # coords = self.canvas.coords(self.drop_ele[index])
            # if coords[1] > 280:
            #     self.canvas.coords(self.drop_ele[index], )
            self.canvas.coords(self.drop_ele[index], d.x, d.y, d.x, d.y+d.len)
        self.root.after(5, self.update)

    def start_sim(self):
        pass

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()