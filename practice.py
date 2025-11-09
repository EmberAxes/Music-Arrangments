import tkinter as tk

window = tk.Tk()

### Labels
label = tk.Label(
    text="This is a label",
    fg="purple",  # Set the text color to whatever, foreground
    bg="white",  # Set the background color to whatever, background
    width = 10,
    height = 5
)
label.pack()      # Need this to put the label together

### Buttons
button = tk.Button(text="Click!", width=5, height=1)
button.pack()

### Entry aka get user input
entry = tk.Entry(
    fg="orange", 
    bg="black"
)
entry.insert(0, "widget")    # at index 0 put widget
entry.delete(4)              # delete the character at index 4
entry.pack()

# ### Text entry, multiple lines
# text_box = tk.Text()

# text_box.insert("0.0","World ")
# text_box.insert(tk.END, "ending")
# text_box.insert(tk.END, "\nNew line!")
# text_box.pack()

### Framing
frame_a = tk.Frame()
frame_b = tk.Frame()
lab_a = tk.Label(master=frame_a, text="Frame A")
lab_b = tk.Label(master=frame_b, text="Frame B")
lab_a.pack()
lab_b.pack()
frame_a.pack()
frame_b.pack()

window.mainloop() # This is what actully makes the window
