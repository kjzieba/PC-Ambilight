from tkinter import *
import screen_capture


# This function gets the data from screen capture module, reads and changes colors of all labels every given time
def get_data(root, name_all, label, number_of_diodes_in_col, number_of_diodes_in_row):

    i = 0
    data = screen_capture.get_screen_data(number_of_diodes_in_col, number_of_diodes_in_row)

    for side in data:
        for components in side:
            # color from screen_capture is in BGR standard, so we have to change this standard to RGB
            colour = (int(components[2]), int(components[1]), int(components[0]))
            if i < len(name_all):
                side = '#%02x%02x%02x' % colour
                label[name_all[i]]['bg'] = side
            i += 1

    # This function runs function every given time
    # Arguments: (time_in_ms, name_of_function, function_argument_1,  function_argument_2, ...)
    root.after(100, get_data, root, name_all, label, number_of_diodes_in_col, number_of_diodes_in_row)


# This function runs gui
def gui(number_of_diodes_in_col, number_of_diodes_in_row):
    root = Tk()

    name_l = []
    name_r = []
    name_t = []
    name_b = []

    i = 1
    while i <= number_of_diodes_in_col:
        name_l.append('%i,0' % (i))
        name_r.append('%i,%i' % (i, number_of_diodes_in_row + 1))
        i += 1

    i = 1
    while i <= number_of_diodes_in_row:
        name_t.append('0,%i' % (i))
        name_b.append('%i,%i' % (number_of_diodes_in_col + 1, i))
        i += 1

    name_all = name_l + name_r + name_t + name_b
    label = {}

    i = 0
    # There, we add labels to the dictionary in the proper position
    for name in name_all:
        position = name.split(',')

        lb = Label(root, text=name)
        lb.grid(row=int(position[0]), column=int(position[1]))
        label[name] = lb
        i += 1

    # There we run get_data function with
    get_data(root, name_all, label, number_of_diodes_in_col, number_of_diodes_in_row)

    root.mainloop()
