from tkinter import *
import screen_capture


# --- function update color ---

def update_color(x, colour):
    a = '#%02x%02x%02x' % colour
    x['bg'] = a


def get_data(root, name_all, label):
    i = 0
    data = screen_capture.get_screen_data()
    for a in data:
        for b in a:
            colour = (int(b[2]), int(b[1]), int(b[0]))
            if i < len(name_all):
                a = '#%02x%02x%02x' % colour
                label[name_all[i]]['bg'] = a
            i += 1
    root.after(10, get_data, root, name_all, label)


# --- gui ---

def gui():
    root = Tk()

    # --- creating labels ----
    num_of_col = 20
    num_of_rows = 20

    name_l = []
    name_r = []
    name_t = []
    name_b = []
    i = 1
    j = 0

    while i <= num_of_rows:
        name_l.append('%i,0' % (i))
        name_r.append('%i,%i' % (i, num_of_col + 1))
        i += 1

    i = 1
    while i <= num_of_col:
        name_t.append('0,%i' % (i))
        name_b.append('%i,%i' % (num_of_rows + 1, i))
        i += 1

    name_all = name_l + name_r + name_t + name_b
    label = {}

    i = 0
    for name in name_all:
        position = name.split(',')

        lb = Label(root, text=name)
        lb.grid(row=int(position[0]), column=int(position[1]))
        label[name] = lb
        i += 1

    get_data(root, name_all, label)

    root.mainloop()
