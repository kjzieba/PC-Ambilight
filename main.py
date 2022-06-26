import sys
import gui
import send_data

if __name__ == '__main__':

    if len(sys.argv) == 3 or len(sys.argv) == 4:

        try:
            number_of_diodes_in_column = int(sys.argv[1])
            number_of_diodes_in_row = int(sys.argv[2])

            if len(sys.argv) == 4:

                if sys.argv[3] == 'gui':
                    gui.gui(number_of_diodes_in_column, number_of_diodes_in_row)
                    exit(0)

                else:
                    print("Wrong arguments!")
                    exit(2)

            send_data.start(number_of_diodes_in_column, number_of_diodes_in_row)

        except:
            print("Wrong arguments!")
            exit(1)

    else:
        print("Wrong number of arguments")
        exit(1)

    exit(0)
