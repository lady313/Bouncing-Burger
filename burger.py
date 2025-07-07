import tkinter as tk

# Setup the main window
root = tk.Tk()
root.title("Square Burger - Lara Gimeno")

canvas = tk.Canvas(root, width=600, height=400, bg="#f0f0f0")
canvas.pack()

# Initial position for Lara Gimeno's burger
x0, y0 = 100, 100
width, height = 180, 150

# Define Lara's unique square burger parts
top_bun = canvas.create_rectangle(x0, y0, x0+width, y0+30, fill="#f4a460", outline="#cd853f", width=2)
onion = canvas.create_oval(x0+10, y0+30, x0+width-10, y0+45, fill="#dda0dd", outline="#9932cc")
bacon = canvas.create_rectangle(x0+15, y0+45, x0+width-15, y0+60, fill="#8b0000", outline="#5c0000")
egg = canvas.create_oval(x0+25, y0+60, x0+width-25, y0+80, fill="#fffacd", outline="#f5deb3")
patty = canvas.create_rectangle(x0+20, y0+80, x0+width-20, y0+100, fill="#654321", outline="#3e2723")
bottom_bun = canvas.create_rectangle(x0, y0+100, x0+width, y0+130, fill="#f4a460", outline="#cd853f", width=2)

# Add centered name
name_text = canvas.create_text(x0+width//2, y0+65, text="Lara Gimeno", font=("Arial", 12, "bold"), fill="black")

# Group all parts of Lara's burger
burger_parts = [top_bun, onion, bacon, egg, patty, bottom_bun, name_text]

# Movement values
dx, dy = 3, 1.5
animation_running = False  # Initially not running
animation_started = False  # Track if already started

def move_burger():
    global dx, dy
    if animation_running:
        for part in burger_parts:
            canvas.move(part, dx, dy)

        x, y = canvas.coords(name_text)
        if x <= 90 or x >= 510:
            dx *= -1
        if y <= 60 or y >= 340:
            dy *= -1

    canvas.after(20, move_burger)

def pause_animation():
    global animation_running
    animation_running = False

def resume_animation():
    global animation_running
    animation_running = True

def start_animation():
    global animation_running, animation_started
    if not animation_started:
        animation_started = True
        move_burger()
    animation_running = True

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Pause", command=pause_animation, width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Resume", command=resume_animation, width=10).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Start", command=start_animation, width=10).grid(row=0, column=2, padx=5)

# Start the Tkinter main loop
root.mainloop()
