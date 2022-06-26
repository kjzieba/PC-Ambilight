import numpy as np
import mss


# this function captures the screen and converts it to numpy array
def capture_screen():
    # get screen capture with mss
    with mss.mss() as sct:
        # get the screen
        ss = sct.grab(sct.monitors[1])
        img_np = np.array(ss)
    # lower the resolution
    img_np = img_np[::10, ::10, :]
    return img_np


# this function extracts the borders from the screen
def extract_borders(img_np):
    border_l = img_np[3:-3, :3, :]
    border_r = img_np[3:-3, -3:, :]
    border_t = img_np[:3, :, :]
    border_b = img_np[-3:, :, :]
    return border_l, border_r, border_t, border_b


# this function divides the borders into n parts
def divide_borders(img_np_borders, n):
    img_np_borders_divided = np.split(img_np_borders, n, axis=2)
    # convert to numpy array
    img_np_borders_divided = np.array(img_np_borders_divided)
    return img_np_borders_divided


# this function gets the average color of a numpy array
def get_average_color_x(img_np, n):
    img_np_average_color = []
    size = img_np.shape[1]
    for i in range(1, n + 1):
        img_np_average_color.append(np.average(img_np[:, ((size // n) * (i - 1)):((size // n) * i), :], axis=(0, 1)))
    return img_np_average_color


def get_average_color_y(img_np, n):
    img_np_average_color = []
    size = img_np.shape[0]
    for i in range(1, n + 1):
        img_np_average_color.append(
            np.average(img_np[((size // n) * (i - 1)):((size // n) * i), :, :], axis=(0, 1)))
    return img_np_average_color


def get_screen_data(number_of_diodes_in_column, number_of_diodes_in_row):
    img_np = capture_screen()
    borders = extract_borders(img_np)

    img_np_borders_average_color_l = get_average_color_y(borders[0], number_of_diodes_in_column)
    img_np_borders_average_color_r = get_average_color_y(borders[1], number_of_diodes_in_column)
    img_np_borders_average_color_t = get_average_color_x(borders[2], number_of_diodes_in_row)
    img_np_borders_average_color_b = get_average_color_x(borders[3], number_of_diodes_in_row)

    return (img_np_borders_average_color_l, img_np_borders_average_color_r, img_np_borders_average_color_t,
            img_np_borders_average_color_b)
