# servo_slack_with_arduino

## background

Since it is necessary to freely move the Arduino servo motor with Slash command from Slack, create a command line tool.

## install

### Set your Arduino

Servo power supply is Arduino 5v or separate supply and connect control signal to any digital PIN (code default 9 PIN).

![breadboard](docs/images/breadboard.svg)

### Install Arduino IDE & write a code on board

1. Download & Install [Arduino IDE](https://www.arduino.cc/en/main/software)
2. Connect your Arduino with USB 2.0.
3. Open [src/arduino/servo.ino](src/arduino/servo.ino) on Arduino IDE and write a code on board.

### Install Python dependencies

```
$ pip install -r requirements.txt
```

## Usage

Enjoy running [Python code](src/python/main.py)!

```
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
```

## demo

![demo](docs/images/arduino.gif)
