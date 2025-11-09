import tkinter as tk

window = tk.Tk()

### Labels
label = tk.Label(
    text="This is a label",
    fg="purple",  # Set the text color to whatever, foreground
    bg="white",  # Set the background color to whatever, background
    width = 10,
    height = 10
)
label.pack()      # Need this to put the label together

### Buttons
button = tk.Button(text="Click!", width=25, height=5)
button.pack()

### Entry aka get user input
entry = tk.Entry(
    fg="orange", 
    bg="black"
)
entry.insert(0, "widget")    # at index 0 put widget
entry.delete(4)              # delete the character at index 4
entry.pack()


window.mainloop() # This is what actully makes the window
