import sys
import gui
import send_data

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'gui':
            gui.gui()
        else:
            pass
    else:
        send_data.start()
