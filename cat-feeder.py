from pathlib import Path
import tkinter as tk
from tkinter import PhotoImage


def on_yes():
    result_label.config(
        text="It's not enough, give them more food!",
        fg=COLOR_TEXT_DARK,
    )


def on_no():
    result_label.config(
        text="Go feed it!",
        fg=COLOR_TEXT_DARK,
    )

COLOR_BG_LIGHT = "#FDF6E3"
COLOR_TEXT_DARK = "#3D2B1F"
COLOR_YES_BG = "#8FBC8F"
COLOR_YES_HOVER = "#A2C4A2"
COLOR_NO_BG = "#E07A5F"
COLOR_NO_HOVER = "#F28482"
COLOR_BTN_TEXT = "#050505"


root = tk.Tk()
root.title("Cat Feeder Reminder")
root.geometry("360x480")
root.resizable(False, False)
root.configure(bg=COLOR_BG_LIGHT)

image_path = Path(__file__).parent / "cat.png"

if image_path.exists():
    raw_image = PhotoImage(file=str(image_path))
    img_width = raw_image.width()
    img_height = raw_image.height()
    max_dim = max(img_width, img_height)

    if max_dim > 200:
        scale_factor = round(max_dim / 200)
        cat_image = raw_image.subsample(scale_factor, scale_factor)
    else:
        cat_image = raw_image

    image_label = tk.Label(root, image=cat_image, bg=COLOR_BG_LIGHT)
else:
    image_label = tk.Label(
        root, text="🐱", font=("Arial", 90), bg=COLOR_BG_LIGHT
    )

image_label.pack(pady=(30, 15))

question_label = tk.Label(
    root,
    text="Have you fed your cats?",
    font=("Segoe UI", 16, "bold"),
    bg=COLOR_BG_LIGHT,
    fg=COLOR_TEXT_DARK,
)
question_label.pack(pady=10)

button_frame = tk.Frame(root, bg=COLOR_BG_LIGHT)
button_frame.pack(pady=15)

yes_button = tk.Button(
    button_frame,
    text="Yes",
    width=10,
    font=("Segoe UI", 11, "bold"),
    bg=COLOR_YES_BG,
    fg=COLOR_BTN_TEXT,
    activebackground=COLOR_YES_HOVER,
    activeforeground=COLOR_BTN_TEXT,
    relief="flat",
    borderwidth=0,
    command=on_yes,
)
yes_button.pack(side="left", padx=10)

no_button = tk.Button(
    button_frame,
    text="No",
    width=10,
    font=("Segoe UI", 11, "bold"),
    bg=COLOR_NO_BG,
    fg=COLOR_BTN_TEXT,
    activebackground=COLOR_NO_HOVER,
    activeforeground=COLOR_BTN_TEXT,
    relief="flat",
    borderwidth=0,
    command=on_no,
)
no_button.pack(side="left", padx=10)

result_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 13),
    bg=COLOR_BG_LIGHT,
    fg=COLOR_TEXT_DARK,
    wraplength=300,
    justify="center",
)
result_label.pack(pady=25)

root.mainloop()
