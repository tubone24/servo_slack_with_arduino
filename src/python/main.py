"""
Overview:
  Run Arduino Servo from the command line
Usage:
  main.py [-h|--help] [-v|--version]
  main.py move <angle> [--port <port>] [--baudrate <baudrate>]
  main.py wipe <delay> <time> [--port <port>] [--baudrate <baudrate>]

Options:
  move           : move a servo
  <angle>        : the angle to movie a servo
  <delay>        : delay time wiping servo
  <time>         : wipe repeat time
  -h, --help     : show this help message and exit
  -v, --version  : show version
  --baudrate     : baudrate with serial comm
  --port         : port with serial comm
"""

from time import sleep
import serial
from docopt import docopt

__version__ = "0.1.0"


def move_servo_angle(args):
    if not args["--baudrate"]:
        baudrate = 9600
    else:
        baudrate = int(args["<baudrate>"])
    if not args["--port"]:
        port = "COM3"
    else:
        port = args["<port>"]

    my_serial = serial.Serial()
    my_serial.port = port
    my_serial.baudrate = baudrate
    my_serial.setDTR(False)
    my_serial.open()
    my_serial.write(args["<angle>"].encode())
    my_serial.close()


def wipe_servo(args):
    if not args["--baudrate"]:
        baudrate = 9600
    else:
        baudrate = int(args["<baudrate>"])
    if not args["--port"]:
        port = "COM3"
    else:
        port = args["<port>"]

    my_serial = serial.Serial()
    my_serial.port = port
    my_serial.baudrate = baudrate
    for _ in range(int(args["<time>"])):
        my_serial.setDTR(False)
        my_serial.open()
        my_serial.write(b"20")
        my_serial.close()
        sleep(int(args["<delay>"]))
        my_serial.setDTR(False)
        my_serial.open()
        my_serial.write(b"90")
        my_serial.close()
        sleep(int(args["<delay>"]))
        my_serial.setDTR(False)
        my_serial.open()
        my_serial.write(b"160")
        my_serial.close()
        sleep(int(args["<delay>"]))


def check_args_num(args) -> bool:
    try:
        int(args["<angle>"])
        return True
    except ValueError:
        raise ValueError("Set only integer, this param is the angle to move a servo.")


def show_version():
    """Show version"""
    print("servo_slack_with_arduino: v{version}".format(version=__version__))


def main(args):
    if args["move"]:
        check_args_num(args)
        move_servo_angle(args)
    if args["wipe"]:
        wipe_servo(args)
    elif args["--version"]:
        show_version()


if __name__ == "__main__":
    args = docopt(__doc__)
    main(args)
