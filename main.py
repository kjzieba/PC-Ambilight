import sys
import gui

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'gui':
            gui.gui()
        else:
            pass
    else:
        pass