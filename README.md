# 🐱 Cat Feeder Reminder
A tiny desktop app built with Python and Tkinter. It shows a picture of a cat
and asks: **"Have you fed your cats?"**

This is a beginner-friendly first project — no external dependencies needed
to run it, just Python's built-in `tkinter` library.

## Project structure
├── main.py
├── cat.png
└── README.md

## Running it in VS Code
1. Make sure Python 3 is installed (`python3 --version` in a terminal).
   - **Tkinter usually comes bundled with Python**, but on Linux you may
     need to install it separately: `sudo apt install python3-tk'
2. Open this folder in VS Code (`File > Open Folder...`).
3. Open `main.py` and click the **Run** ▶ button, or run in the terminal: python3 main.py
4. A window should pop up with a cat and two buttons. 

## Using your own cat photo
Replace `cat.png` with any PNG image of your own cat — just keep the file
name the same (or update the `image_path` line in `main.py`). Tkinter's
built-in `PhotoImage` supports `.png`, `.gif`, and `.pgm`/`.ppm` files
natively — no extra libraries required.

> If you want to use a `.jpg` file instead, you'll need Pillow:
> `pip install Pillow`, then swap `PhotoImage` for
> `PIL.ImageTk.PhotoImage` in `main.py`.

## Ideas to build on later
- Track feeding times with a timestamp and save them to a file
- Add a "how many cats?" counter so each cat gets tracked separately
- Turn it into a daily reminder that pops up automatically
- Rebuild it as a web app (HTML/CSS/JS) once you're comfortable with the concept
