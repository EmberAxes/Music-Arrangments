import tkinter as tk
# https://realpython.com/python-gui-tkinter/
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

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

frame_b.pack()           # Order of frames is order of appearance
frame_a.pack()

### Framing visual options
for relief_name, relief in border_effects.items():
    frame3 = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame3.pack(side=tk.TOP)
    label = tk.Label(master=frame3, text=relief_name)
    label.pack()

### Placing frames in locations
frm_color = tk.Frame(width=20, height=20)
frm_red = tk.Frame(master=frm_color, width = 6, height=6, bg="red")
frm_org = tk.Frame(master=frm_color, width = 8, height=8, bg="orange")
frm_yel = tk.Frame(master=frm_color, width = 10, height=10, bg="yellow")
frm_grn = tk.Frame(master=frm_color, width = 12, height=12, bg="green")
frm_blu = tk.Frame(master=frm_color, width = 14, height=14, bg="blue")
frm_pur = tk.Frame(master=frm_color, width = 16, height=16, bg="purple")

frm_red.pack(side=tk.TOP, fill=tk.X)
frm_org.pack(side=tk.LEFT)
frm_yel.pack(side=tk.RIGHT)
frm_grn.pack(side=tk.TOP)
frm_blu.pack(side=tk.BOTTOM)
frm_pur.pack(fill=tk.Y)
frm_color.pack(side=tk.BOTTOM)


window.mainloop() # This is what actully makes the window
