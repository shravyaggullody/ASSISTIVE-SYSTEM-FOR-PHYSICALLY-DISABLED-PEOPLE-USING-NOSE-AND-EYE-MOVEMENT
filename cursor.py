from tkinter import *
import subprocess

# Function to execute the script
def execute_script():
    try:
        subprocess.Popen(["python", "C:\\Users\\dell1\\OneDrive\\Desktop\\final_eye\\Mouse_Cursor_Control_Handsfree-master - Copy\\mouse-cursor-control.py"])
    except FileNotFoundError:
        label.config(text="Error: File not found")

# Function to darken the button color on hover
def on_enter(e):
    button_execute.config(bg="#c96b8e")  # Darker shade of the button color on hover

# Function to restore the original button color when mouse leaves
def on_leave(e):
    button_execute.config(bg="#e481a4")  # Original button color

# Create the main window
window = Tk()
window.title("Assistive system for physically disabled people using nose and eye movement")

# Load the background image
bg_image = PhotoImage(file="cursor.png")  # Replace "cursor.png" with the actual file path

# Resize the background image to fit the screen
zoom_factor = 1 # Adjust the zoom factor as needed
bg_image = bg_image.subsample(zoom_factor, zoom_factor)

# Set the window geometry to cover the entire screen
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

# Create a label to hold the background image
background_label = Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the button to execute the script
button_execute = Button(window, text="START", command=execute_script, bg="#e481a4", fg="white", font=("Arial", 20), padx=20, pady=10, relief="raised", borderwidth=2)
button_execute.place(relx=0.655, rely=0.5, anchor=CENTER)

# Bind hover events to button
button_execute.bind("<Enter>", on_enter)
button_execute.bind("<Leave>", on_leave)

# Run the main event loop
window.mainloop()
