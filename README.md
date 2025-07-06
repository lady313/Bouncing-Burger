# Bouncing-Burger
Bouncing burger

import tkinter as tk

# Setup the main window
root = tk.Tk()
root.title("Realistic 3D Burger - Lady C. Archibido")

canvas = tk.Canvas(root, width=600, height=400, bg="#f0f0f0")
canvas.pack()

# Initial position for the burger
x0, y0 = 150, 100
width, height = 180, 150

# Realistic 3D burger components

# Top Bun (rounded rectangle)
top_bun = canvas.create_oval(x0, y0, x0 + width, y0 + 30, fill="#f4a460", outline="#cd853f", width=2)

# Lettuce (wavy irregular shape using arcs for texture)
lettuce = canvas.create_polygon(x0 + 10, y0 + 30, x0 + width - 10, y0 + 30, 
                                x0 + width, y0 + 45, x0 + 10, y0 + 45, 
                                fill="#98fb98", outline="#3cb371")

# Tomato (semi-circle with rounded edges)
tomato = canvas.create_arc(x0 + 20, y0 + 45, x0 + width - 20, y0 + 60, start=0, extent=180, fill="#ff6347", outline="#ff4500")

# Cheese slice (rectangle with a slight angle to simulate perspective)
cheese = canvas.create_polygon(x0 + 20, y0 + 60, x0 + width - 20, y0 + 60, 
                               x0 + width - 10, y0 + 80, x0 + 10, y0 + 80, 
                               fill="#ffeb3b", outline="#fbc02d")

# Patty (thicker and round disk shape)
patty = canvas.create_oval(x0 + 20, y0 + 80, x0 + width - 20, y0 + 100, fill="#654321", outline="#3e2723")

# Bottom Bun (rounded rectangle)
bottom_bun = canvas.create_oval(x0, y0 + 100, x0 + width, y0 + 130, fill="#f4a460", outline="#cd853f", width=2)

# Add centered name for Lady C.
name_text = canvas.create_text(x0 + width // 2, y0 + 70, text="Lady C. Archibido", font=("Arial", 12, "bold"), fill="black")

# Group all parts of Lady C.'s burger
lady_parts = [top_bun, lettuce, tomato, cheese, patty, bottom_bun, name_text]

# Movement values for Lady C.
dx, dy = 3, 1.5
animation_running = True

# Function to move the burger
def move_burger():
    global dx, dy, animation_running
    if animation_running:
        # Move all parts of the burger
        for part in lady_parts:
            canvas.move(part, dx, dy)

        # Get position from name text (center)
        x, y = canvas.coords(name_text)

        # Bounce off borders (simple border collision)
        if x <= 90 or x >= 510:
            dx *= -1
        if y <= 60 or y >= 340:
            dy *= -1

    # Recursively call the function to keep moving
    canvas.after(20, move_burger)

# Pause the animation
def pause_animation():
    global animation_running
    animation_running = False

# Resume the animation
def resume_animation():
    global animation_running
    animation_running = True
    

# Stop the animation
def stop_animation():
    global dx, dy, animation_running
    animation_running = False

# Buttons for pause, resume, and stop
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

pause_btn = tk.Button(button_frame, text="Pause", command=pause_animation, width=10)
pause_btn.grid(row=0, column=0, padx=5)

resume_btn = tk.Button(button_frame, text="Resume", command=resume_animation, width=10)
resume_btn.grid(row=0, column=1, padx=5)

stop_btn = tk.Button(button_frame, text="Stop", command=stop_animation, width=10)
stop_btn.grid(row=0, column=2, padx=5)

# Start the animation
move_burger()

root.mainloop()
