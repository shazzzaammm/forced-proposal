import tkinter
import customtkinter
import pyautogui
from PIL import Image

WIDTH = 1920 // 2
HEIGHT = 1080 // 2
QUESTION = "Will I get an A?"
IMAGE_PATH = "images/a_plus.jpg"

geometry = str(WIDTH) + "x" + str(HEIGHT)

root_tk = customtkinter.CTk()
root_tk.geometry(geometry)
root_tk.title("I have a question")

customtkinter.set_appearance_mode("System")


def defer(e):
    mouse_x, mouse_y = e.x_root, e.y_root
    widget_x, widget_y = e.widget.winfo_rootx(), e.widget.winfo_rooty()
    widget_width = e.widget.winfo_width()
    widget_height = e.widget.winfo_height()
    widget_center_x = widget_x + widget_width / 2
    widget_center_y = widget_y + widget_height / 2

    deltaX = mouse_x - widget_center_x
    deltaY = mouse_y - widget_center_y
    pyautogui.moveRel(deltaX, deltaY, 0.5)


def success():
    frame.destroy()
    img = customtkinter.CTkImage(Image.open(IMAGE_PATH), size=(WIDTH, HEIGHT))
    image_label = customtkinter.CTkLabel(root_tk, text="", image=img)
    image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def easter_egg():
    frame.destroy()
    img = customtkinter.CTkImage(
        Image.open("images/easter_egg.jpg"), size=(WIDTH, HEIGHT)
    )
    image_label = customtkinter.CTkLabel(root_tk, text="", image=img)
    image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


frame = customtkinter.CTkFrame(root_tk, width=WIDTH / 1.5, height=HEIGHT / 1.5)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label = customtkinter.CTkLabel(
    frame,
    text=QUESTION,
    font=customtkinter.CTkFont("Sans Serif", WIDTH // 45),
)

label.place(relx=0.5, rely=0.175, anchor=tkinter.CENTER)
button_font = customtkinter.CTkFont("Sans Serif", WIDTH // 60)
no_button = customtkinter.CTkButton(
    master=frame,
    corner_radius=10,
    text="No",
    width=WIDTH / 8,
    height=HEIGHT / 10,
    font=button_font,
    command=easter_egg,
)
no_button.place(relx=0.35, rely=0.75, anchor=tkinter.E)
no_button.bind("<Motion>", defer)
no_button.bind("<Enter>", defer)

yes_button = customtkinter.CTkButton(
    master=frame,
    corner_radius=10,
    text="Yes",
    command=success,
    width=WIDTH / 8,
    height=HEIGHT / 10,
    font=button_font,
)
yes_button.place(relx=0.65, rely=0.75, anchor=tkinter.W)
pyautogui.FAILSAFE = False
root_tk.mainloop()
