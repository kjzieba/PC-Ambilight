import serial
import screen_capture

LEFT = 0
RIGHT = 1
TOP = 2


def wait_until_received(arduino):
    arduino.read()
    arduino.reset_input_buffer()


def start(number_of_diodes_in_column, number_of_diodes_in_row):
    arduino = serial.Serial(port='COM3', baudrate=19200, timeout=1)

    while True:
        data = screen_capture.get_screen_data(number_of_diodes_in_column, number_of_diodes_in_row)

        for d in reversed(data[LEFT]):
            arduino.write(bytes([d[2], d[1], d[0]]))

        for d in data[TOP]:
            arduino.write(bytes([d[2], d[1], d[0]]))

        for d in data[RIGHT]:
            arduino.write(bytes([d[2], d[1], d[0]]))

        wait_until_received(arduino)
